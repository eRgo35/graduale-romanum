CHANTS := asperges kyrie kyrie-ix gloria credo sanctus agnus ite
SCORES := $(CHANTS:%=scores/%.ly)

# Per-chant converter options (pitch and layout follow the Vatican II Hymnal).
# --do is the sounding pitch of the chant "do" (the C-clef line); the
# treble_(8) clef shows it an octave higher.  Kyrie, Gloria, Credo and Ite:
# do = A (D major; the Credo, absent from the Hymnal's Mass VIII, follows the
# Gloria); Asperges, Sanctus, Agnus: do = middle C (the default).
# Change --do to transpose, e.g. --do "bes" for Kyrie/Gloria in E-flat.
MASS_V := --do a --key-flat
FLAGS_kyrie    := $(MASS_V) --break-sections --continued
FLAGS_kyrie-ix := $(MASS_V)
FLAGS_gloria   := $(MASS_V) --intonation
FLAGS_credo    := $(MASS_V) --intonation
FLAGS_ite      := $(MASS_V)
FLAGS_agnus    := --break-sections

missa-viii.pdf: missa-viii.tex $(SCORES) build-ly/.common
	lualatex -shell-escape -interaction=nonstopmode -halt-on-error missa-viii.tex

# lyluatex caches by score text only; drop the cache when the shared style changes.
build-ly/.common: scores/common.ily
	rm -rf build-ly
	mkdir -p build-ly
	touch $@

scores/%.ly: gabc/%.gabc tools/gabc2ly.py
	python3 tools/gabc2ly.py $(FLAGS_$*) $< $@

clean:
	rm -rf build-ly missa-viii.aux missa-viii.log missa-viii.pdf

.PHONY: clean
