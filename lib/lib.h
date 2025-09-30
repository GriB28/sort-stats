#ifndef SORT_STATS_H
#define SORT_STATS_H
#include <cstddef>
using std::size_t;

namespace sort {
    void bubble(int *list, const size_t &length);
    void insertion(int *list, const size_t &length);
    void selection(int *list, const size_t &length);
    void count(int *list, const size_t &length);

    void merge(int *list, const size_t &length);
    void merge(int *list, const size_t &left, const size_t &right);
    void do_merge(int *list, const size_t &left, const size_t &middle, const size_t &right);
    void quick(int *list, const size_t &length);
    void quick(int *list, const size_t &low, const size_t &high);
    void do_heap(int *list, const size_t &length, const size_t &index);
    void heap(int *list, const size_t &length);
}

namespace utils {
    long long get_time();
    int randomize_an_int(const int &min, const int &max);
    void randomize_array(const int &min, const int &max, const size_t &length, int *array_link);
}

#endif