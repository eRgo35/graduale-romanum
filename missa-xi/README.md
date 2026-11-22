# Missa XI *Orbis factor*

Booklet with the Ordinary of Missa XI (Sundays per annum) in modern notation,
Latin text with Polish translation in parallel columns. Pitch and layout follow
the Vatican II Hymnal (2011); the Ite, not in the Hymnal's Mass XI, is pitched
like the Kyrie (same melody).

| Chant | Mode | gabc source |
|---|---|---|
| Asperges me / Vidi aquam (sprinkling rite) | VII, IV, VIII | `../shared/` |
| Kyrie (ninefold) | I | `gabc/kyrie.gabc` |
| Gloria | II | `gabc/gloria.gabc` |
| Credo I | IV | `../shared/` |
| Sanctus | II | `gabc/sanctus.gabc` |
| Agnus Dei | I | `gabc/agnus.gabc` |
| Ite, missa est | I | `gabc/ite.gabc` |

## Layout

- `gabc/`: square-notation sources from GregoBase.
- `scores/`: generated `.ly` scores (style in `../shared/common.ily`).
- `missa-xi.tex`: LuaLaTeX booklet embedding the scores via `lyluatex`.
- `missa-xi.pdf`: built booklet.

The sprinkling rite, Credo I and the Marian antiphons are shared with the
other booklets and live in `../shared/`; the converter is `../tools/gabc2ly.py`.

## Build

```sh
make         # regenerate changed scores, then build missa-xi.pdf
make clean   # remove build-ly/ cache and LaTeX outputs
```

Per-chant converter options (pitch, key signature, line breaks) are set in the
`Makefile`. Transpose a chant by changing its `--do` pitch, e.g. `--do "d'"`.
