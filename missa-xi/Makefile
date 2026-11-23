CHANTS := kyrie gloria sanctus agnus ite
SCORES := $(CHANTS:%=scores/%.ly)
SHARED := $(wildcard ../shared/*.tex ../shared/gabc/*.gabc)

# Per-chant converter options (pitch and layout follow the Vatican II Hymnal).
# --do is the sounding pitch of the chant "do" (the C-clef line); the
# treble_(8) clef shows it an octave higher.  Kyrie and Ite: do = middle C
# (F major signature, final D); Gloria: do = F above middle C (B-flat major,
# final G); Sanctus: do = E (A major, final F-sharp); Agnus: do = D (D major,
# final E).  Change --do to transpose, e.g. --do "d'" for the Kyrie a tone up.
# Asperges and Credo I live in ../shared/ (options in ../shared/Makefile).
FLAGS_kyrie     := --do "c'" --key-flat --break-sections
FLAGS_gloria    := --do "f'" --key-flat --intonation
FLAGS_sanctus   := --do "e'" --key-flat
FLAGS_agnus     := --do "d'" --break-sections
FLAGS_ite       := --do "c'" --key-flat

missa-xi.pdf: missa-xi.tex ordinarium.tex $(SCORES) $(SHARED) build-ly/.common
	$(MAKE) -C ../shared
	lualatex -shell-escape -interaction=nonstopmode -halt-on-error missa-xi.tex

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
	rm -rf build-ly missa-xi.aux missa-xi.log missa-xi.pdf

.PHONY: clean scores
