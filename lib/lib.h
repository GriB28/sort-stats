#ifndef SORT_STATS_H
#define SORT_STATS_H
#include <cstddef>
#include <fstream>
#include <string>
using std::size_t;
using std::fstream;
using std::string;

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
    void heap(int *list, const size_t &length);
    void do_heap(int *list, const size_t &length, const size_t &index);
}

namespace utils {
    constexpr size_t MAX_LENGTH = 100000;
    static fstream *stream_link = nullptr;

    long long get_time();
    void generate_array(const short &type, const int &min, const int &max, const size_t &length, int *array_link);

    int randomize_an_int(const int &min, const int &max);
    void random_array(const int &min, const int &max, const size_t &length, int *array_link);

    void ascending_array(const int &min, const int &max, const size_t &length, int *array_link);
    void descending_array(const int &min, const int &max, const size_t &length, int *array_link);

    void prepare_result_file(fstream *&filestream, const string &graph_name, const string &x_axis_name, const string &y_axis_name);
    void add_result(const size_t &length, const double &dtime);
}


#endif