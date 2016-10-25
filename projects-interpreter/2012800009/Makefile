all: main

main: main.o
	@g++ -o main main.o

main.o: main.cpp
	@g++ -c main.cpp -o main.o
	
run: main
	@./main
	
clean:
	@rm main *.o
