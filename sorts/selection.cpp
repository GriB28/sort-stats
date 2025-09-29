#include <fstream>
#include <chrono>
#include <random>

#include "../lib/sorts.h"
using std::fstream;


void make_array(const int &min, const int &max, const size_t &length, int *array_link) {
    for (size_t i = 0; i < length; i++) {
        const unsigned seed = std::chrono::steady_clock::now().time_since_epoch().count();
        static std::default_random_engine e(seed);
        std::uniform_int_distribution<int> d(min, max);
        array_link[i] = d(e);
    }
}


constexpr size_t MAX_LENGTH = 100000000;
static int array[MAX_LENGTH];
int main() {
    fstream data("data/input.csv", std::ios::in);
    fstream result("data/selection.csv", std::ios::app);

    size_t length;
    int max, min;
    data >> length >> max >> min;
    make_array(min, max, length, array);

    auto start = std::chrono::high_resolution_clock::now();
    sort::selection(array, length);
    auto end = std::chrono::high_resolution_clock::now();

    result << (end - start).count() << ',' << length << '\n';
    return 0;
}
