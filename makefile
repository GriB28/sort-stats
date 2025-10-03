FLAGS = -std=c++17

all:
	echo "you have to use one of these names: bubble_0, bubble_1, bubble_2, insertion, selection, merge, hoar, quick"

bubble_0:
	g++ sorts/bubble.cpp lib/sorts.cpp lib/utils.cpp -O0 -o bin/bubble_0
bubble_1:
	g++ sorts/bubble.cpp lib/sorts.cpp lib/utils.cpp -O1 -o bin/bubble_1
bubble_2:
	g++ sorts/bubble.cpp lib/sorts.cpp lib/utils.cpp -O2 -o bin/bubble_2
bubble_3:
	g++ sorts/bubble.cpp lib/sorts.cpp lib/utils.cpp -O3 -o bin/bubble_3

insertion:
	g++ sorts/insertion.cpp lib/sorts.cpp lib/utils.cpp -O0 -o bin/insertion

selection:
	g++ sorts/selection.cpp lib/sorts.cpp lib/utils.cpp -O0 -o bin/selection

merge:
	g++ sorts/merge.cpp lib/sorts.cpp lib/utils.cpp -O0 -o bin/merge

quick:
	g++ sorts/quick.cpp lib/sorts.cpp lib/utils.cpp -O0 -o bin/quick

heap:
	g++ sorts/heap.cpp lib/sorts.cpp lib/utils.cpp -O0 -o bin/heap