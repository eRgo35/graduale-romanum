# Graduale Romanum

Gregorian chant from the Graduale Romanum transcribed into modern notation
(LilyPond) and typeset as printable booklets (LuaLaTeX), with Latin text and
Polish translation.

## Contents

| Directory | Contents |
|---|---|
| [`missa-viii/`](missa-viii/) | Missa VIII *De Angelis*: Asperges me, Kyrie, Gloria, Sanctus, Agnus Dei, Ite missa est |

Each directory is self-contained: gabc sources, generated LilyPond scores,
the booklet source and its own `Makefile`.

## Requirements

- Python 3
- LilyPond >= 2.24 in `PATH`
- LuaLaTeX with `lyluatex`, `paracol`, `titlesec`, `fontspec`, Libertinus Serif
