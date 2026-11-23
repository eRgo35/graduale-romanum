# Build every booklet.
BOOKLETS := $(wildcard missa-*) kyriale

all:
	for d in $(BOOKLETS); do $(MAKE) -C $$d || exit 1; done

clean:
	for d in $(BOOKLETS); do $(MAKE) -C $$d clean || exit 1; done

.PHONY: all clean
