# Missa XVII *In Dominicis Adventus et Quadragesimae*

Booklet with the Ordinary of Missa XVII (Sundays of Advent and Lent) in modern
notation, Latin text with Polish translation in parallel columns. Pitch and
layout follow the Vatican II Hymnal (2011), which gives the Kyrie written out
nine-fold. No Gloria in Advent and Lent. The Ite, missa est is that of
Mass XV, as the Graduale Romanum (1961) prescribes; it is not in the Hymnal and
is set in the Kyrie's key signature.

| Chant | Mode | gabc source |
|---|---|---|
| Asperges me | VII | `../shared/gabc/asperges.gabc` |
| Kyrie (nine-fold) | I | `gabc/kyrie.gabc` |
| Credo I | IV | `../shared/gabc/credo-i.gabc` |
| Sanctus | V | `gabc/sanctus.gabc` |
| Agnus Dei | V | `gabc/agnus.gabc` |
| Ite, missa est (= Mass XV) | IV | `gabc/ite.gabc` |

## Layout

- `gabc/`: square-notation sources from GregoBase.
- `../tools/gabc2ly.py`: gabc → LilyPond converter; run with `--help` for options.
- `scores/`: generated `.ly` scores; `../shared/common.ily` holds the shared style.
- `missa-xvii.tex`: LuaLaTeX booklet embedding the scores via `lyluatex`.
- `missa-xvii.pdf`: built booklet.

## Build

```sh
make         # regenerate changed scores, then build missa-xvii.pdf
make clean   # remove build-ly/ cache and LaTeX outputs
```

Per-chant converter options (pitch, key signature, line breaks) are set in the
`Makefile`. Transpose a chant by changing its `--do` pitch, e.g. `--do "c'"`.
