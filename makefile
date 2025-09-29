FLAGS = -std=c++17

all:
	echo "you have to use one of these names: bubble_0, bubble_1, bubble_2, insertion, selection, merge, hoar, quick"

bubble_0:
	g++ sorts/bubble.cpp lib/sorts.cpp -O0 -o bin/bubble_0
bubble_1:
	g++ sorts/bubble.cpp lib/sorts.cpp -O1 -o bin/bubble_1
bubble_2:
	g++ sorts/bubble.cpp lib/sorts.cpp -O2 -o bin/bubble_2

insertion:
	g++ sorts/insertion.cpp lib/sorts.cpp -O0 -o bin/insertion

selection:
	g++ sorts/selection.cpp lib/sorts.cpp -O0 -o bin/selection
