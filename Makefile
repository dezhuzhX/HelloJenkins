hello: hello.o
	cc -o hello hello.o
all:
hello.o: hello.c
	cc -c hello.c
test:
	./hello
clean:
	rm -rf hello hello.o

