#!/usr/bin/env python3
"""Convert a GregoBase gabc file into a modern-notation LilyPond score.

Usage: gabc2ly.py [options] input.gabc output.ly
  --do PITCH         sounding LilyPond pitch of the chant "do" (default c' = middle C;
                     the treble_(8) clef prints it an octave higher)
  --key-flat         print the one-flat key signature (transposed with the music)
  --intonation       italic lyrics up to the first double bar (celebrant's intonation)
  --break-sections   start a new line after every double bar (::)
  --continued        end with a double bar instead of a final bar (another
                     score of the same chant follows)

Mapping (square notation -> modern transcription, Vatican II Hymnal style):
  neume note                      -> stemless quarter notehead
  punctum mora (.)                -> stemless half notehead
  horizontal episema, one note    -> tenuto line
  horizontal episema, 2+ notes    -> "rit." over the group
  notes between "/" or " "        -> one slur; long notes stand alone,
                                     consecutive long notes share a slur
  divisio , ; : ::                -> tick, half bar, full bar, double bar
                                     (the last double bar is a final bar)
The clef line of the c-clef is C5 before transposition.  A flat (x) or natural
(y) lasts until the next divisio or the end of the word, as in chant books; its
sign is printed on the first affected note only.
Vertical episema, quilisma, oriscus, stropha, virga and liquescence are signs
of the square notation and are rendered as plain notes.
"""
import argparse
import re

STEPS = "cdefgab"
HALF_BAR = r"\once \override Staff.BarLine.bar-extent = #'(-1 . 1) \bar " + '"|"'
BAR = {",": r"\bar " + "\"'\"", "`": r"\bar " + "\"'\"", ";": HALF_BAR,
       ":": r'\bar "|"', "::": r'\bar "||"'}


def note_name(step, octave, acc):
    name = STEPS[step] + ("es" if acc == "x" else "") + ("!" if acc == "y" else "")
    return name + ("'" * (octave - 3) if octave >= 3 else "," * (3 - octave))


class Note:
    def __init__(self, pitch):
        self.pitch = pitch
        self.long = False
        self.episema = False


class Piece:
    def __init__(self):
        self.c_index = None      # gabc letter index that carries C5
        self.accidentals = {}    # letter index -> 'x' | 'y'
        self.seen_flat = set()   # steps that were flattened earlier
        self.flat_shown = set()  # letter indices whose flat sign is printed in this scope
        self.music = []          # LilyPond music tokens
        self.lyrics = []         # LilyPond lyric tokens
        self.last_note_pos = None
        self.extender_due = False  # last syllable was a melisma ending a word

    def pitch(self, index):
        rel = index - self.c_index
        step, octave = rel % 7, 5 + rel // 7
        acc = self.accidentals.get(index, "")
        hide = ""
        if acc == "x":
            self.seen_flat.add(step)
            # like the Hymnal: the flat is printed once per word/divisio scope
            if index in self.flat_shown:
                hide = r"\tweak Accidental.stencil ##f "
            self.flat_shown.add(index)
        elif step in self.seen_flat:
            acc = "y"            # print a natural after an earlier flat
        return hide + note_name(step, octave, acc)

    def reset_accidentals(self):
        self.accidentals.clear()
        self.flat_shown.clear()

    # -- notes of one syllable ---------------------------------------------
    def neume(self, code):
        """Return the notes of one syllable as a list of slur groups."""
        groups = [[]]
        code = re.sub(r"\[[^\]]*\]", "", code)   # brackets, spacing tweaks
        i = 0
        while i < len(code):
            ch = code[i]
            low = ch.lower()
            if "a" <= low <= "m":
                nxt = code[i + 1:i + 2]
                if nxt and nxt in "xy#":
                    if nxt == "#":
                        raise SystemExit("sharp signs are not supported")
                    self.accidentals[ord(low) - 97] = nxt
                    i += 2
                    if code[i:i + 1] == "?":
                        i += 1
                    continue
                groups[-1].append(Note(self.pitch(ord(low) - 97)))
                i += 1
            elif ch in "/ ":
                if groups[-1]:
                    groups.append([])
                i += 1
            elif ch in "._":
                n = len(re.match(re.escape(ch) + "+", code[i:]).group())
                for note in groups[-1][-n:]:
                    if ch == ".":
                        note.long = True
                    else:
                        note.episema = True
                i += n
            elif ch in "vVswWoOqrR'!-@~<>0123456789":
                i += 1
            else:
                raise SystemExit(f"unsupported gabc sign {ch!r} in ({code})")
        # long notes stand alone; a run of long notes shares one slur
        split = []
        for group in groups:
            run = []
            for note in group:
                if run and run[-1].long != note.long:
                    split.append(run)
                    run = []
                run.append(note)
            if run:
                split.append(run)
        return split

    def emit_notes(self, groups, rubric):
        tokens = []
        notes = [n for g in groups for n in g]
        for group in groups:
            rit = sum(n.episema for n in group) > 1
            for k, note in enumerate(group):
                tok = note.pitch + ("2" if note.long else "4")
                if note.episema and not rit:
                    tok += "--"
                if len(group) > 1 and k == 0:
                    tok += "("
                if len(group) > 1 and k == len(group) - 1:
                    tok += ")"
                if rit and k == 0:
                    tok += r'^\markup \italic "rit."'
                if note is notes[0] and rubric:
                    tok += r'^\markup \italic "%s"' % rubric
                if len(notes) > 1 and note is notes[0]:
                    tok += r" \melisma"
                if len(notes) > 1 and note is notes[-1]:
                    tok += r" \melismaEnd"
                tokens.append(tok)
        self.music.append(" ".join(tokens))
        self.last_note_pos = len(self.music) - 1

    def close_word(self):
        if self.extender_due:
            self.lyrics.append("__")
            self.extender_due = False


RUBRIC = re.compile(r"<i>(.*?)</i>|<sp>R/</sp>\.?|<sp>V/</sp>\.?")


def split_text(text):
    """Return (sung text, rubric, number of asterisks) for a gabc syllable text."""
    rubrics = []
    for m in RUBRIC.finditer(text):
        if m.group(1) is not None:
            rubrics.append(m.group(1).replace("~", " "))
        else:
            rubrics.append("℟." if "R/" in m.group() else "℣.")
    text = RUBRIC.sub("", text)
    text = re.sub(r"</?[a-z]+>", "", text)
    text = text.replace("{", "").replace("}", "").replace("~", "")
    stars = text.count("*")
    text = text.replace("*", "").strip()
    return text, " ".join(rubrics), stars


def convert(src, break_sections=False, intonation=False):
    header, body = src.split("%%", 1)
    title = re.search(r"^name:(.*);", header, re.M).group(1).strip()
    piece = Piece()
    words = 0                    # words begun so far
    word_open = False            # previous syllable may continue the word
    if intonation:
        piece.lyrics.append(r"\override LyricText.font-shape = #'italic")
    for m in re.finditer(r"([^()]*)\(([^)]*)\)", body):
        raw_text, code = m.group(1), m.group(2).strip()
        new_word = raw_text[:1].isspace()
        text, rubric, stars = split_text(raw_text)

        clef = re.fullmatch(r"c([1-4])", code)
        if clef:
            piece.c_index = 1 + 2 * int(clef.group(1))
            continue
        if re.fullmatch(r"[zZ][+-]?", code):
            piece.music.append(r"\break")
            continue
        bar = re.fullmatch(r"(::|[,;:`])[0-9]?", code)
        if bar:
            piece.reset_accidentals()
            if stars:            # e.g. "*(:)" -- mark the preceding syllable
                last = max(j for j, t in enumerate(piece.lyrics) if t.startswith('"'))
                piece.lyrics[last] = piece.lyrics[last][:-1] + " " + "*" * stars + '"'
            piece.close_word()
            piece.music.append(BAR[bar.group(1)])
            if bar.group(1) == "::":
                if intonation:
                    piece.lyrics.append(r"\revert LyricText.font-shape")
                    intonation = False
                if break_sections:
                    piece.music.append(r"\break")
            if rubric and piece.last_note_pos is not None:
                piece.music[piece.last_note_pos] += r'^\markup \italic "%s"' % rubric
            word_open = False
            continue
        if new_word or not text:
            piece.reset_accidentals()
        groups = piece.neume(code)
        if not groups:
            continue
        melisma = sum(len(g) for g in groups) > 1
        if text:
            if new_word:
                piece.close_word()
                words += 1
                # \cadenzaOn only breaks lines where explicitly allowed
                if piece.music and not piece.music[-1].startswith(("\\bar", "\\break", "\\once")):
                    piece.music.append(r"\allowBreak")
            if words == 1:       # gabc capitalises the whole first word
                text = text[0] + text[1:].lower() if new_word else text.lower()
            text = re.sub(r"\s+([:;!?])", r"\1", text)
            if word_open and not new_word:
                piece.lyrics.append("--")
            if stars:
                text = "*" * stars + " " + text
            piece.lyrics.append('"%s"' % text.replace('"', '\\"'))
            piece.extender_due = melisma
            word_open = True
        else:
            piece.lyrics.append("_")   # melisma continued after a divisio
            piece.extender_due = False
        piece.emit_notes(groups, rubric)
    piece.close_word()
    while piece.music and piece.music[-1] == r"\break":
        piece.music.pop()
    return title, piece


def to_ly(title, piece, source_name, do, key_flat):
    lines = [
        "% Generated by tools/gabc2ly.py from gabc/" + source_name
        + " -- edit the gabc, not this file.",
        "% " + title,
        r'\version "2.24.0"',
        r'\include "common.ily"',
        "",
        r"melody = \chantMusic %s {" % do,
    ]
    if key_flat:
        lines.append(r"  \key f \major")
    lines += ["  " + t for t in piece.music]
    lines += ["}", "", r"words = \lyricmode {"]
    lines += ["  " + " ".join(piece.lyrics)]
    lines += ["}", "", r"\chantScore \melody \words", ""]
    return "\n".join(lines)


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--do", default="c'")
    ap.add_argument("--key-flat", action="store_true")
    ap.add_argument("--intonation", action="store_true")
    ap.add_argument("--break-sections", action="store_true")
    ap.add_argument("--continued", action="store_true")
    ap.add_argument("input")
    ap.add_argument("output")
    args = ap.parse_args()
    with open(args.input, encoding="utf-8") as f:
        title, piece = convert(f.read(), args.break_sections, args.intonation)
    if not args.continued and piece.music and piece.music[-1] == BAR["::"]:
        piece.music[-1] = r'\bar "|."'
    with open(args.output, "w", encoding="utf-8") as f:
        f.write(to_ly(title, piece, args.input.rsplit("/", 1)[-1], args.do, args.key_flat))


if __name__ == "__main__":
    main()
