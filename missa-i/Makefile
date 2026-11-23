CHANTS := kyrie gloria sanctus agnus ite ite-paschale
SCORES := $(CHANTS:%=scores/%.ly)
SHARED := $(wildcard ../shared/*.tex ../shared/gabc/*.gabc)

# Per-chant converter options (pitch and layout follow the Vatican II Hymnal).
# --do is the sounding pitch of the chant "do" (the C-clef line); the
# treble_(8) clef shows it an octave higher.  The whole Mass: do = B-flat
# (B-flat major); the Ites, absent from the Hymnal, follow the Kyrie.
# Change --do to transpose, e.g. --do "c'" for C major.
# Asperges and Credo III live in ../shared/ (options in ../shared/Makefile).
MASS_I := --do bes
FLAGS_kyrie        := $(MASS_I)
FLAGS_gloria       := $(MASS_I) --intonation
FLAGS_sanctus      := $(MASS_I)
FLAGS_agnus        := $(MASS_I)
FLAGS_ite          := $(MASS_I)
FLAGS_ite-paschale := $(MASS_I)

missa-i.pdf: missa-i.tex ordinarium.tex $(SCORES) $(SHARED) build-ly/.common
	$(MAKE) -C ../shared
	lualatex -shell-escape -interaction=nonstopmode -halt-on-error missa-i.tex

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
	rm -rf build-ly missa-i.aux missa-i.log missa-i.pdf

.PHONY: clean scores
