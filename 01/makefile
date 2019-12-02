SH=/bin/bash
FC=ifort
FFLAGS=-C -g
F90_FILES=$(wildcard aoc*.f90)
OBJ_FILES=$(F90_FILES:.f90=.o)

default: main.bin
	
%.o: %.f90
	$(FC) $(FFLAGS) -c -o $@ $<
	
io.o: 
	$(FC) $(FFLAGS) -c ../tools/io.f90 -o io.o

main.bin: io.o $(OBJ_FILES)
	$(FC) -o $@ $^

clean:
	rm -f *.o
	rm -f *.bin
	rm -f *.mod

run: clean main.bin
	./main.bin