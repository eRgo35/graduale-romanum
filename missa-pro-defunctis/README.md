# Missa pro defunctis

Booklet with the chants of the traditional Requiem Mass, the absolution
(*Libera me*) and the antiphon *In paradisum*, in modern notation, Latin text
with Polish translation in parallel columns. Sources are the GregoBase
transcriptions of the Graduale Romanum / Liber Usualis (1961); the Kyrie is
pitched and slurred after the Vatican II Hymnal (2011), the other chants are
pitched for a congregation.

| Chant | Mode | gabc source |
|---|---|---|
| Introitus *Requiem aeternam* (Ps. *Te decet hymnus*) | VI | `gabc/introitus.gabc` |
| Kyrie (ninefold) | VI | `gabc/kyrie.gabc` |
| Graduale *Requiem aeternam* (V. *In memoria aeterna*) | II | `gabc/graduale.gabc` |
| Tractus *Absolve, Domine* | VIII | `gabc/tractus.gabc` |
| Sequentia *Dies irae* | I | `gabc/sequentia.gabc` |
| Offertorium *Domine Jesu Christe* (V. *Hostias*) | II | `gabc/offertorium.gabc` |
| Sanctus (= Sanctus XVIII) | | `gabc/sanctus.gabc` |
| Agnus Dei (*dona eis requiem*) | | `gabc/agnus.gabc` |
| Communio *Lux aeterna* (V. *Requiem aeternam*) | VIII | `gabc/communio.gabc` |
| *Requiescant in pace* | | `gabc/requiescant.gabc` |
| Responsorium *Libera me, Domine* (absolution) | I | `gabc/libera.gabc` |
| Antiphona *In paradisum* | VII | `gabc/paradisum.gabc` |

## Layout

- `gabc/`: square-notation sources from GregoBase.
- `scores/`: generated `.ly` scores (style in `../shared/common.ily`).
- `missa-pro-defunctis.tex`: LuaLaTeX booklet (title page) embedding `ordinarium.tex`.
- `ordinarium.tex`: the chant blocks with the parallel Latin/Polish text.
- `missa-pro-defunctis.pdf`: built booklet.

The converter is `../tools/gabc2ly.py`.

## Build

```sh
make         # regenerate changed scores, then build missa-pro-defunctis.pdf
make clean   # remove build-ly/ cache and LaTeX outputs
```

Per-chant converter options (pitch, key signature, line breaks) are set in the
`Makefile`. Transpose a chant by changing its `--do` pitch, e.g. `--do "d'"`.
