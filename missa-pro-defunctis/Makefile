CHANTS := introitus kyrie graduale tractus sequentia offertorium sanctus agnus \
          communio requiescant libera paradisum
SCORES := $(CHANTS:%=scores/%.ly)
SHARED := ../shared/booklet.tex ../shared/macros.tex

# Per-chant converter options.  --do is the sounding pitch of the chant "do"
# (the C-clef line); the treble_(8) clef shows it an octave higher.
# Kyrie: pitch and key as in the Vatican II Hymnal (do = middle C, F major,
# final F).  The other chants have no Hymnal model and are pitched for a
# congregation (highest note about D4-E4); the propers mostly end on G.
# --key-flat only where the chant's B is mostly flat (Kyrie, Introit, Libera me).
# Introit: do = D (G major, final G); Gradual: do = B-flat (B-flat major,
# final G); Tract: do = C (final G); Dies irae: do = C (final D); Offertory:
# do = F (F major, final G); Sanctus and Agnus: do = E-flat (E-flat major);
# Communio, Requiescant, In paradisum: do = C; Libera me: do = D (G major,
# final E).  Change --do to transpose, e.g. --do "d'".
FLAGS_introitus   := --do "d'" --key-flat --break-sections
FLAGS_kyrie       := --do "c'" --key-flat
FLAGS_graduale    := --do bes --break-sections
FLAGS_tractus     := --do "c'" --break-sections
FLAGS_sequentia   := --do "c'" --break-sections
FLAGS_offertorium := --do "f'" --break-sections
FLAGS_sanctus     := --do "es'"
FLAGS_agnus       := --do "es'" --break-sections
FLAGS_communio    := --do "c'" --break-sections
FLAGS_requiescant := --do "c'"
FLAGS_libera      := --do "d'" --key-flat --break-sections
FLAGS_paradisum   := --do "c'" --break-sections

missa-pro-defunctis.pdf: missa-pro-defunctis.tex ordinarium.tex $(SCORES) $(SHARED) build-ly/.common
	lualatex -shell-escape -interaction=nonstopmode -halt-on-error missa-pro-defunctis.tex

# lyluatex caches by score text only; drop the cache when the shared style changes.
build-ly/.common: ../shared/common.ily
	rm -rf build-ly
	mkdir -p build-ly
	touch $@

scores/%.ly: gabc/%.gabc ../tools/gabc2ly.py
	python3 ../tools/gabc2ly.py $(FLAGS_$*) $< $@

# Scores only.
scores: $(SCORES)

clean:
	rm -rf build-ly missa-pro-defunctis.aux missa-pro-defunctis.log missa-pro-defunctis.pdf

.PHONY: clean scores
