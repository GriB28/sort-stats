#include "sorts.h"
#include <cstddef>
using std::size_t;


void sort::bubble(int *list, const size_t &length) {
    for (size_t i = 0; i < length - 1; i++) {
        bool breaker = true;
        for (size_t j = 0; j < length - i - 1; j++) {
            if (list[j] > list[j + 1]) {
                breaker = false;
                const int t = list[j + 1];
                list[j + 1] = list[j];
                list[j] = t;
            }
        }
        if (breaker) break;
    }
}

void sort::insertion(int *list, const size_t &length) {
    for (size_t i = 1; i < length; i++) {
        const int current_value = list[i];
        size_t j = i - 1;
        while (j > 0 && list[j] > current_value) {
            list[j + 1] = list[j];
            j--;
        }
        list[j + 1] = current_value;
    }
}

void sort::selection(int *list, const size_t &length) {
    for (size_t i = 0; i < length; i++) {
        int local_min = list[i];
        for (size_t j = i + 1; j < length; j++) {
            if (local_min > list[j]) {
                const int t = list[j];
                list[j] = local_min;
                local_min = t;
            }
        }
        list[i] = local_min;
    }
}

void sort::count(int *list, const size_t &length) {
    int min = list[0], max = list[0];
    for (size_t i = 1; i < length; i++) {
        if (list[i] < min) min = list[i];
        if (list[i] > max) max = list[i];
    }

    auto *counter = new int[max - min + 1];
    for (size_t i = 0; i < max - min + 1; i++) counter[i] = 0;
    for (size_t i = 0; i < length; i++) counter[list[i] - min]++;

    size_t index = 0;
    for (int i = 0; i <= max - min; i++)
        while (counter[i]-- > 0)
            list[index++] = i + min;
    delete[] counter;
}

void sort::merge(int *list, const size_t &length) {

}