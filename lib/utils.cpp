#include "lib.h"
#include <chrono>
#include <random>


long long utils::get_time() {
    return std::chrono::duration_cast<std::chrono::microseconds>(
        std::chrono::steady_clock::now().time_since_epoch()
        ).count();
}


int utils::randomize_an_int(const int &min, const int &max) {
    const unsigned seed = std::chrono::steady_clock::now().time_since_epoch().count();
    static std::default_random_engine e(seed);
    std::uniform_int_distribution<int> d(min, max);
    return d(e);
}


void utils::randomize_array(const int &min, const int &max, const size_t &length, int *array_link) {
    for (size_t i = 0; i < length; i++)
        array_link[i] = randomize_an_int(min, max);
}