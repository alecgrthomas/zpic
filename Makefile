# Find all subdirectories with a Makefile
SUBDIRS := $(shell find . -mindepth 1 -maxdepth 1 -type d -exec test -e '{}/Makefile' \; -print)

.PHONY: all clean $(SUBDIRS)

all: $(SUBDIRS)

$(SUBDIRS):
	$(MAKE) -C $(@F)

