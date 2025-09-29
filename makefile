FLAGS = -D _DEBUG -ggdb3 -std=c++17 -O0

all:
	g++ main.cpp sorts.cpp -o sort-stats