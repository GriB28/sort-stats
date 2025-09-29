#ifndef SORT_STATS_SORTS_H
#define SORT_STATS_SORTS_H
#include <cstddef>
using std::size_t;

namespace sort {
    void bubble(int *list, const size_t &length);
    void insertion(int *list, const size_t &length);
    void selection(int *list, const size_t &length);
    void count(int *list, const size_t &length);
    void merge(int *list, const size_t &length);
}
#endif