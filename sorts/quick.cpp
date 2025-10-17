#include <iostream>
#include <fstream>
#include <string>
#include "../lib/lib.h"
using std::cout;
using std::fstream;
using std::string;


static int array[utils::MAX_LENGTH];
int main() {
    cout << "reading config...\n";
    fstream data("data/input.csv", std::ios::in);

    size_t length, iterations;
    int max, min;
    short array_type, averaging;
    string output_file, graph_name, Ox, Oy;
    data >> output_file >> graph_name >> Ox >> Oy;
    data >> length >> max >> min >> array_type >> averaging >> iterations;

    auto *result = new fstream("data/" + output_file + ".csv", std::ios::out);
    utils::prepare_result_file(result, graph_name, Ox, Oy);

    cout << "configuring is over.\nstarting calculating...\n";
    for (size_t iteration = 0; iteration < iterations; iteration++) {
        const long percent = 1000 * iteration / iterations;
        cout << "\r\bprogress: " << iteration << " / " << iterations << " (" << percent / 10 << '.' << percent % 10 << "%)";
        size_t local_length = length + iteration;
        double measured_time = 0;

        for (short _ = 0; _ < averaging; _++) {
            utils::generate_array(array_type, min, max, local_length, array);
            const long long start_time_stamp = utils::get_time();
            sort::quick(array, local_length);
            const long long stop_time_stamp = utils::get_time();
            measured_time += stop_time_stamp - start_time_stamp;
        }

        utils::add_result(local_length, measured_time / averaging);
    }
    cout << "\r\bcompleted\n";
    delete result;
    return 0;
}
