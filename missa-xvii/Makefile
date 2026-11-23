CHANTS := kyrie sanctus agnus ite
SCORES := $(CHANTS:%=scores/%.ly)
SHARED := $(wildcard ../shared/*.tex ../shared/gabc/*.gabc)

# Per-chant converter options (pitch and layout follow the Vatican II Hymnal).
# --do is the sounding pitch of the chant "do" (the C-clef line); the
# treble_(8) clef shows it an octave higher.  Kyrie: do = D (D major);
# Sanctus: do = B-flat (E-flat major); Agnus: do = middle C (F major).
# Ite (not in the Hymnal): do = A, in the Kyrie's D-major signature.
# Change --do to transpose, e.g. --do "c'" for the Kyrie in C major.
# Asperges and Credo I live in ../shared/ (options in ../shared/Makefile).
FLAGS_kyrie   := --do "d'" --break-sections
FLAGS_sanctus := --do bes --key-flat
FLAGS_agnus   := --key-flat --break-sections
FLAGS_ite     := --do a --key-flat

missa-xvii.pdf: missa-xvii.tex ordinarium.tex $(SCORES) $(SHARED) build-ly/.common
	$(MAKE) -C ../shared
	lualatex -shell-escape -interaction=nonstopmode -halt-on-error missa-xvii.tex

# lyluatex caches by score text only; drop the cache when the shared style changes.
build-ly/.common: ../shared/common.ily
	rm -rf build-ly
	mkdir -p build-ly
	touch $@

scores/%.ly: gabc/%.gabc ../tools/gabc2ly.py
	python3 ../tools/gabc2ly.py $(FLAGS_$*) $< $@

# Scores only (the Kyriale embeds them).
scores: $(SCORES)

clean:
	rm -rf build-ly missa-xvii.aux missa-xvii.log missa-xvii.pdf

.PHONY: clean scores
