#include <fstream>
#include "../lib/lib.h"
using std::fstream;


constexpr size_t MAX_LENGTH = 100000000;
static int array[MAX_LENGTH];
int main() {
    fstream data("data/input.csv", std::ios::in);
    fstream result("data/insertion.csv", std::ios::app);

    size_t length;
    int max, min;
    data >> length >> max >> min;
    utils::randomize_array(min, max, length, array);

    long long start_time_stamp = utils::get_time();
    sort::insertion(array, length);

    result << (utils::get_time() - start_time_stamp) << ',' << length << '\n';
    return 0;
}
