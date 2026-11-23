CHANTS := kyrie gloria sanctus agnus ite
SCORES := $(CHANTS:%=scores/%.ly)
SHARED := $(wildcard ../shared/*.tex ../shared/gabc/*.gabc)

# Per-chant converter options (pitch and layout follow the Vatican II Hymnal).
# --do is the sounding pitch of the chant "do" (the C-clef line); the
# treble_(8) clef shows it an octave higher.  Kyrie and Ite: do = D above
# middle C, b-flat signature (G major); Gloria: do = G below middle C (G major);
# Sanctus, Agnus: do = A below middle C, b-flat signature (D major).
# Change --do to transpose, e.g. --do "es'" for Kyrie/Ite in A-flat.
# Asperges and Credo III live in ../shared/ (options in ../shared/Makefile).
MASS_I := --do "d'" --key-flat
MASS_V := --do a --key-flat
FLAGS_kyrie   := $(MASS_I) --break-sections
FLAGS_gloria  := --do g --intonation
FLAGS_sanctus := $(MASS_V)
FLAGS_agnus   := $(MASS_V) --break-sections
FLAGS_ite     := $(MASS_I)

missa-ix.pdf: missa-ix.tex ordinarium.tex $(SCORES) $(SHARED) build-ly/.common
	$(MAKE) -C ../shared
	lualatex -shell-escape -interaction=nonstopmode -halt-on-error missa-ix.tex

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
	rm -rf build-ly missa-ix.aux missa-ix.log missa-ix.pdf

.PHONY: clean scores
