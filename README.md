# Graduale Romanum

Gregorian chant from the Graduale Romanum transcribed into modern notation
(LilyPond) and typeset as printable booklets (LuaLaTeX), with Latin text and
Polish translation.

## Contents

| Directory | Contents |
|---|---|
| [`missa-i/`](missa-i/) | Missa I *Lux et origo* (Eastertide): Kyrie, Gloria, Credo III, Sanctus, Agnus Dei, Ite missa est (+ paschal Ite with alleluia) |
| [`missa-viii/`](missa-viii/) | Missa VIII *De Angelis*: Kyrie, Gloria, Credo III, Sanctus, Agnus Dei, Ite missa est |
| [`missa-ix/`](missa-ix/) | Missa IX *Cum jubilo* (feasts of Our Lady): Kyrie, Gloria, Credo III, Sanctus, Agnus Dei, Ite missa est |
| [`missa-xi/`](missa-xi/) | Missa XI *Orbis factor* (Sundays per annum): Kyrie, Gloria, Credo I, Sanctus, Agnus Dei, Ite missa est |
| [`missa-xvii/`](missa-xvii/) | Missa XVII (Sundays of Advent and Lent): Kyrie, Credo I, Sanctus, Agnus Dei, Ite missa est |
| [`missa-pro-defunctis/`](missa-pro-defunctis/) | Missa pro defunctis (Requiem), full traditional set: Introitus, Kyrie, Graduale, Tractus, Sequentia Dies irae, Offertorium, Sanctus, Agnus Dei, Communio, Requiescant in pace; absolution with Libera me; In paradisum |
| [`kyriale/`](kyriale/) | The whole collection as one A5 book (`kyriale.pdf`): contents, sprinkling rite, the five Masses, Credo I and III, Marian antiphons, the Requiem, index of chants, running heads. `kyriale-druk.pdf` is the same book imposed on A4 sheets for duplex printing and folding into a booklet |
| [`shared/`](shared/) | Chants printed in every booklet: before Mass Asperges me (I and II) and Vidi aquam; after Mass the Marian antiphons Alma Redemptoris Mater, Ave Regina caelorum, Regina caeli and Salve Regina, each in the simple and the solemn tone. Also Credo I and III, the booklet preamble and the LilyPond style |
| [`tools/`](tools/) | `gabc2ly.py`, the gabc → LilyPond converter (`--help` for options) |

Each `missa-*` directory holds its gabc sources, generated LilyPond scores,
booklet source, built PDF and `Makefile`. Its booklet `\input`s the shared
parts from `shared/`. Sources, transcribers and reference editions are
credited in [`ATTRIBUTION.md`](ATTRIBUTION.md).

## Build

```sh
make                 # build every booklet and the Kyriale
make -C missa-ix     # build one booklet (also regenerates shared scores)
make clean
```

## Requirements

- Python 3
- LilyPond >= 2.24 in `PATH`
- LuaLaTeX with `lyluatex`, `paracol`, `titlesec`, `fontspec`, `babel-latin`
  (+ Latin hyphenation patterns), Libertinus Serif

Fedora:

```sh
sudo dnf install lilypond texlive-lyluatex texlive-luaoptions texlive-minibox \
  texlive-paracol texlive-babel-latin texlive-hyphen-latin texlive-libertinus-fonts
```

## License

*Ad maiorem Dei gloriam.* Free for any use, without conditions: the work in
this repository is dedicated to the public domain under
[CC0 1.0 Universal](LICENSE).

This covers the repository's own work (scores, booklets, converter). Material
from third parties keeps its own terms; see [`ATTRIBUTION.md`](ATTRIBUTION.md),
notably the Polish liturgical texts from the *Mszał rzymski dla diecezji
polskich*.
