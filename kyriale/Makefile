# Kyriale: all chants in one A5 book (kyriale.pdf) and the same book imposed
# on A4 sheets for duplex printing, fold and staple (kyriale-druk.pdf).
MASSES  := $(wildcard ../missa-*)
SOURCES := $(wildcard ../missa-*/ordinarium.tex ../missa-*/gabc/*.gabc \
                      ../shared/*.tex ../shared/gabc/*.gabc) ../tools/gabc2ly.py
LATEX   := lualatex -shell-escape -interaction=nonstopmode -halt-on-error

all: kyriale.pdf kyriale-druk.pdf

# Three LaTeX runs: contents, index and \pageref settle on the last one.
kyriale.pdf: kyriale.tex $(SOURCES) build-ly/.common
	for d in $(MASSES); do $(MAKE) -C $$d scores || exit 1; done
	$(MAKE) -C ../shared
	$(LATEX) kyriale.tex
	makeindex kyriale
	$(LATEX) kyriale.tex
	$(LATEX) kyriale.tex

kyriale-druk.pdf: kyriale-druk.tex kyriale-druk.lua kyriale.pdf
	$(LATEX) kyriale-druk.tex

# lyluatex caches by score text only; drop the cache when the shared style changes.
build-ly/.common: ../shared/common.ily
	rm -rf build-ly
	mkdir -p build-ly
	touch $@

clean:
	rm -rf build-ly kyriale.pdf kyriale-druk.pdf \
	  $(foreach e,aux log toc out idx ind ilg,kyriale.$(e) kyriale-druk.$(e))

.PHONY: all clean
