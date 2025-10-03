#include "lib.h"
#include <chrono>
#include <random>


long long utils::get_time() {
    return std::chrono::duration_cast<std::chrono::microseconds>(
        std::chrono::steady_clock::now().time_since_epoch()
        ).count();
}

void utils::generate_array(const short &type, const int &min, const int &max, const size_t &length, int *array_link) {
    switch (type) {
        case 0:
            random_array(min, max, length, array_link);
            break;
        case 1:
            ascending_array(min, max, length, array_link);
            break;
        case 2:
            descending_array(min, max, length, array_link);
            break;
        default:
            break;
    }
}


int utils::randomize_an_int(const int &min, const int &max) {
    const unsigned seed = std::chrono::steady_clock::now().time_since_epoch().count();
    static std::default_random_engine e(seed);
    std::uniform_int_distribution<int> d(min, max);
    return d(e);
}
void utils::random_array(const int &min, const int &max, const size_t &length, int *array_link) {
    for (size_t i = 0; i < length; i++)
        array_link[i] = randomize_an_int(min, max);
}

void utils::ascending_array(const int &min, const int &max, const size_t &length, int *array_link) {
    random_array(min, max, length, array_link);
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


void utils::prepare_result_file(fstream *&filestream, const string &graph_name, const string &x_axis_name, const string &y_axis_name) {
    stream_link = filestream;
    *stream_link << '#' << graph_name << '\t' << x_axis_name << '\t' << y_axis_name << '\n';
}

void utils::add_result(const size_t &length, const long long &dtime) { *stream_link << length << ',' << dtime << '\n'; }
