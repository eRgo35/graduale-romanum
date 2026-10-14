# Missa VIII *De Angelis*

Booklet with the Ordinary of Missa VIII in modern notation, Latin text with
Polish translation in parallel columns. Pitch and layout follow the Vatican II
Hymnal (2011).

| Chant | Mode | gabc source |
|---|---|---|
| Asperges me | VII | `gabc/asperges.gabc` |
| Kyrie (+ ninefold final invocation) | V | `gabc/kyrie.gabc`, `gabc/kyrie-ix.gabc` |
| Gloria | V | `gabc/gloria.gabc` |
| Sanctus | VI | `gabc/sanctus.gabc` |
| Agnus Dei | VI | `gabc/agnus.gabc` |
| Ite, missa est | V | `gabc/ite.gabc` |

## Layout

- `gabc/`: square-notation sources from GregoBase.
- `tools/gabc2ly.py`: gabc → LilyPond converter; run with `--help` for options.
- `scores/`: generated `.ly` scores; `common.ily` holds the shared style.
- `missa-viii.tex`: LuaLaTeX booklet embedding the scores via `lyluatex`.
- `missa-viii.pdf`: built booklet.
- `14-06-15_0.pdf`: Vatican II Hymnal reference pages.

## Build

```sh
make         # regenerate changed scores, then build missa-viii.pdf
make clean   # remove build-ly/ cache and LaTeX outputs
```

Per-chant converter options (pitch, key signature, line breaks) are set in the
`Makefile`. Transpose a chant by changing its `--do` pitch, e.g. `--do bes`.
