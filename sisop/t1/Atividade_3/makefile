
# 

CC = gcc

all: m0 m1 m2 m3 fibo

m0: mulmat0.o
	$(CC) -o m0 mulmat0.o

mulmat0.o: mulmat0.c mulmat.h
	$(CC) -c mulmat0.c

m1: mulmat1.o
	$(CC) -o m1 mulmat1.o

mulmat1.o: mulmat1.c mulmat.h
	$(CC) -c mulmat1.c

m2: mulmat2.o
	$(CC) -o m2 mulmat2.o

mulmat2.o: mulmat2.c mulmat.h
	$(CC) -c mulmat2.c

m3: mulmat3.o
	$(CC) -o m3 mulmat3.o

mulmat3.o: mulmat3.c mulmat.h
	$(CC) -c mulmat3.c

fibo: fibonacci.c
	$(CC) -o fibo fibonacci.c

clean: 
	rm -f *.o *~ m0 m1 m2 m3 fibo


