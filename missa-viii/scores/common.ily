\version "2.24.0"

% Wrap a transcribed melody.  `do` is the sounding pitch of the chant "do"
% (the C-clef line, entered as c''); the Makefile sets it per chant.
% Free rhythm, stemless noteheads, treble clef sung an octave lower, and every
% accidental that differs from the key signature is printed (chant accidentals
% do not carry through a modern "measure").
chantMusic =
#(define-music-function (do music) (ly:pitch? ly:music?)
   #{
     \transpose c'' $do {
       \clef "treble_(8)"
       \cadenzaOn
       \accidentalStyle forget
       \autoBeamOff
       $music
     }
   #})

chantScore =
#(define-scheme-function (melody words) (ly:music? ly:music?)
   #{
     \score {
       <<
         \new Voice = "chant" $melody
         \new Lyrics \lyricsto "chant" $words
       >>
       \layout {
         indent = 0
         ragged-last = ##t
         \context {
           \Score
           \override SpacingSpanner.spacing-increment = #0.75
         }
         \context {
           \Staff
           \remove Time_signature_engraver
           \hide Stem
           \hide Flag
           \override BarLine.hair-thickness = #1.3
           % slurs arch over flat signs instead of running through them
           \override Slur.details.accidental-collision = #50
         }
         \context {
           \Voice
           % syllables follow \melisma/\melismaEnd, not slurs (one syllable may
           % carry several slur groups)
           melismaBusyProperties = #'(melismaBusy)
           \override Slur.direction = #UP
           \override Slur.thickness = #1.4
           \override Script.padding = #0.3
         }
         \context {
           \Lyrics
           \override LyricText.font-size = #0.5
           \override LyricSpace.minimum-distance = #1.2
           \override LyricHyphen.minimum-distance = #0.8
         }
       }
     }
   #})
