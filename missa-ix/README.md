# Missa IX *Cum jubilo*

Booklet with the Ordinary of Missa IX (feasts of the Blessed Virgin Mary) in
modern notation, Latin text with Polish translation in parallel columns. Pitch
and layout follow the Vatican II Hymnal (2011); the Ite, absent from the
Hymnal, is pitched like the Kyrie (same mode and melody).

| Chant | Mode | gabc source |
|---|---|---|
| Sprinkling rite (Asperges me, Vidi aquam) | VII, IV, VIII | `../shared/gabc/` |
| Kyrie (ninefold) | I | `gabc/kyrie.gabc` |
| Gloria | VII | `gabc/gloria.gabc` |
| Credo III | V | `../shared/gabc/credo-iii.gabc` |
| Sanctus | V | `gabc/sanctus.gabc` |
| Agnus Dei | V | `gabc/agnus.gabc` |
| Ite, missa est | I | `gabc/ite.gabc` |
| Marian antiphons | various | `../shared/gabc/` |

## Layout

- `gabc/`: square-notation sources from GregoBase.
- `scores/`: generated `.ly` scores (`../shared/common.ily` holds the shared style).
- `missa-ix.tex`: LuaLaTeX booklet embedding the scores via `lyluatex`.
- `missa-ix.pdf`: built booklet.

## Build

```sh
make         # regenerate changed scores, then build missa-ix.pdf
make clean   # remove build-ly/ cache and LaTeX outputs
```

Per-chant converter options (pitch, key signature, line breaks) are set in the
`Makefile`. Transpose a chant by changing its `--do` pitch, e.g. `--do bes`.
