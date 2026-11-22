# Chants shared by several booklets.  Each booklet's Makefile runs this one
# before LaTeX.  Per-chant converter options as in the booklet Makefiles.
# Vidi aquam is pitched as in the Vatican II Hymnal; the other chants without
# a Hymnal model are pitched for a congregation (highest note about D4-E4).
CHANTS := asperges asperges-ii vidi-aquam credo-i credo-iii \
          alma-simplex alma ave-regina-simplex ave-regina \
          regina-caeli-simplex regina-caeli salve-regina-simplex salve-regina
SCORES := $(CHANTS:%=scores/%.ly)

FLAGS_asperges-ii          := --do "es'"
FLAGS_vidi-aquam           := --do bes
FLAGS_credo-i              := --do "f'" --key-flat --intonation
FLAGS_credo-iii            := --do a --key-flat --intonation
FLAGS_alma                 := --do g --key-flat
FLAGS_ave-regina-simplex   := --key-flat
FLAGS_ave-regina           := --do g
FLAGS_regina-caeli-simplex := --key-flat
FLAGS_regina-caeli         := --key-flat

all: $(SCORES)

scores/%.ly: gabc/%.gabc ../tools/gabc2ly.py
	python3 ../tools/gabc2ly.py $(FLAGS_$*) $< $@

.PHONY: all
