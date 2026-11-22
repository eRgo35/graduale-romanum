# Missa VIII *De Angelis*

Booklet with the Ordinary of Missa VIII in modern notation, Latin text with
Polish translation in parallel columns. Pitch and layout follow the Vatican II
Hymnal (2011); Credo III, not part of the Hymnal's Mass VIII, is pitched like
the Gloria.

| Chant | Mode | gabc source |
|---|---|---|
| Kyrie (+ ninefold final invocation) | V | `gabc/kyrie.gabc`, `gabc/kyrie-ix.gabc` |
| Gloria | V | `gabc/gloria.gabc` |
| Credo III | V | `../shared/gabc/credo-iii.gabc` |
| Sanctus | VI | `gabc/sanctus.gabc` |
| Agnus Dei | VI | `gabc/agnus.gabc` |
| Ite, missa est | V | `gabc/ite.gabc` |

The sprinkling rite (Asperges me I/II, Vidi aquam) before Mass, Credo III and
the Marian antiphons after Mass are shared with the other booklets and live in
`../shared/`.

## Layout

- `gabc/`: square-notation sources from GregoBase.
- `scores/`: generated `.ly` scores (style in `../shared/common.ily`).
- `missa-viii.tex`: LuaLaTeX booklet embedding the scores via `lyluatex`.
- `missa-viii.pdf`: built booklet.

The converter is `../tools/gabc2ly.py`.

## Build

```sh
make         # regenerate changed scores, then build missa-viii.pdf
make clean   # remove build-ly/ cache and LaTeX outputs
```

Per-chant converter options (pitch, key signature, line breaks) are set in the
`Makefile`. Transpose a chant by changing its `--do` pitch, e.g. `--do bes`.
