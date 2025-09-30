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
void utils::ascending_array(const int &min, const int &max, const size_t &length, int *array_link) {
    randomize_array(min, max, length, array_link);
    sort::merge(array_link, length);
}
void utils::descending_array(const int &min, const int &max, const size_t &length, int *array_link) {
    ascending_array(min, max, length, array_link);
    for (size_t i = 0; i < length; i++) {
        if (i == length - i - 1) continue;
        const int t = array_link[i];
        array_link[i] = array_link[length - i - 1];
        array_link[length - i - 1] = t;
    }
}
