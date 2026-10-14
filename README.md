# Graduale Romanum

Gregorian chant from the Graduale Romanum transcribed into modern notation
(LilyPond) and typeset as printable booklets (LuaLaTeX), with Latin text and
Polish translation.

## Contents

| Directory | Contents |
|---|---|
| [`missa-viii/`](missa-viii/) | Missa VIII *De Angelis*: Asperges me, Kyrie, Gloria, Credo III, Sanctus, Agnus Dei, Ite missa est |

Each directory is self-contained: gabc sources, generated LilyPond scores,
the booklet source and its own `Makefile`. Sources, transcribers and reference
editions are credited in [`ATTRIBUTION.md`](ATTRIBUTION.md).

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
