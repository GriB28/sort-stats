#include <iostream>
#include <cstdlib>
#include "sorts.h"
using std::cin;
using std::cout;
using std::system;


constexpr size_t MAX_LENGTH = 10000;
int main() {
    size_t n;
    cout << "length: ";
    cin >> n;
    cout << "array: ";
    int array[MAX_LENGTH];
    for (size_t i = 0; i < n; i++)
        cin >> array[i];

    sort::bubble(array, n);

    for (size_t i = 0; i < n; i++)
        cout << array[i] << ' ';
    cout << '\n';

    system("python3 plotmaker.py auto ");
    return 0;
}
