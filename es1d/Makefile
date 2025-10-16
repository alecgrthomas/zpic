# GCC options
CC = gcc
CFLAGS = -Ofast -std=c99 -Wall -pedantic
LDFLAGS = -lm

# Intel icc compiler
#CC = icc
#CFLAGS = -restrict -Ofast -std=c99 -pedantic
#LDFLAGS =

# Clang options
# CC = clang
# CFLAGS = -Ofast -std=c99 -pedantic
# LDFLAGS = -lm

INPUT_FILES = $(wildcard input/*)

SOURCE = charge.c field.c particles.c grid.c fft.c random.c timer.c main.c simulation.c \
         zdf.c

TARGET = zpic

DOCSBASE = docs

DOCS = $(DOCSBASE)/html/index.html

OBJ = $(SOURCE:.c=.o)

all : $(SOURCE) $(TARGET)

docs : $(DOCS)

$(TARGET) : $(OBJ) $(INPUT_FILES)
	$(CC) $(CFLAGS) $(OBJ) $(LDFLAGS) -o $@

main.o: main.c $(INPUT_FILES)
	$(CC) $(CFLAGS) -c main.c -o main.o

%.o: %.c
	$(CC) $(CFLAGS) -c $< -o $@


$(DOCS) : $(SOURCE)
	@doxygen ./Doxyfile

clean:
	@touch $(TARGET) $(OBJ)
	rm -f $(TARGET) $(OBJ)
	rm -rf $(DOCSBASE)
