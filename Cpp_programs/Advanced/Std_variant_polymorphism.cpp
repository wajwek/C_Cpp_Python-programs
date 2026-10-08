#include <iostream>
#include <variant>
#include <vector> 
#include <string>
using namespace std;

class DataAggregator {
    private:
        vector<variant<int, float, string>> _list;
    public:
        void addData(initializer_list<variant<int, float, string>> list) {
            for (const auto& element : list) {
                _list.push_back(element);
            }
        }
        void print() {
            for(const auto& element : _list) {
                visit([](auto&& val) {cout << val << " ";}, element);
            }
            cout << endl;
        }
        float sumNumeric() {
            float sum = 0.0f;
            for(const auto& element : _list) {
                visit([&sum](auto&& arg) {
                    using T = decay_t<decltype(arg)>;
                    if constexpr (is_same<T, int>::value || is_same<T, float>::value) {
                        sum += arg;
                    }
                }, element);
            }
            return sum;
        }
};

int main () {

    DataAggregator aggregator;
    aggregator.addData({10, 3.14f, "tekst", 20, "test", 1.5f});
    cout << "List contents: ";
    aggregator.print();
    cout << "Sum of values: " << aggregator.sumNumeric() << endl;

    return 0;
}
