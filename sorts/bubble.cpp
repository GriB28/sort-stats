#include <fstream>
#include <string>
#include "../lib/lib.h"
using std::fstream;
using std::string;


static int array[utils::MAX_LENGTH];
int main() {
    fstream data("data/input.csv", std::ios::in);

    size_t length, iterations;
    int max, min;
    short array_type;
    string output_file, graph_name, Ox, Oy;
    data >> output_file >> graph_name >> Ox >> Oy;
    data >> length >> max >> min >> array_type >> iterations;

    auto *result = new fstream("data/" + output_file + ".csv", std::ios::out);
    utils::prepare_result_file(result, graph_name, Ox, Oy);

    for (size_t iteration = 0; iteration < iterations; iteration++) {
        size_t local_length = length + iteration;
        switch (array_type) {
            case 0:
                utils::random_array(min, max, local_length, array);
                break;
            case 1:
                utils::ascending_array(min, max, local_length, array);
                break;
            case 2:
                utils::descending_array(min, max, local_length, array);
                break;
            default:
                break;
        }

        const long long start_time_stamp = utils::get_time();
        sort::bubble(array, local_length);
        const long long stop_time_stamp = utils::get_time();

        utils::add_result(local_length, stop_time_stamp - start_time_stamp);
    }
    delete result;
    return 0;
}
