# Kyriale

Every chant of the repository in one A5 book, `kyriale.pdf`:

1. *Ritus aspersionis*: Asperges me I and II, Vidi aquam
2. *Ordinarium Missae*: Masses I, VIII, IX, XI and XVII (each Mass points to
   its Credo by page number)
3. *Credo*: Credo I and III
4. *Antiphonae B. M. V.*: Alma Redemptoris Mater, Ave Regina caelorum,
   Regina caeli, Salve Regina, each in the simple and the solemn tone
5. *Missa pro defunctis*: the full Requiem with its propers, plus the
   absolution (Libera me) and In paradisum

There's also a table of contents, an index of chants (each Ordinary chant
listed by Mass, and Masses also by name), running heads and page numbers.

`kyriale-druk.pdf` is the same book imposed for saddle stitching: A4
landscape sheets with two pages per side, in booklet order (`kyriale-druk.lua`).
Print duplex, flipping on the short edge, then fold the stack in half, staple
on the fold and trim the fore-edge. Pages are shifted towards the spine to
compensate for creep (inner sheets stick out further at the fore-edge), so
every page keeps the same outer margin after trimming. The shift is the
sheet's position from the outside times `\creep` in `kyriale-druk.tex`: the
thickness of one sheet, 0.1 mm by default (80 g/m² paper).

The book embeds the same scores and texts as the single-Mass booklets: each
Mass's `../missa-*/ordinarium.tex` and the fragments in `../shared/`. Only the
page layout differs (`kyriale.tex`: A5, staff size 14).

## Build

```sh
make         # kyriale.pdf (lualatex, makeindex, lualatex x2) and kyriale-druk.pdf
make clean
```
