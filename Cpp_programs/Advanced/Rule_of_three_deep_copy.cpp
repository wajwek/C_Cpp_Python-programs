#include <iostream>
using namespace std;

class IntArray {
    private:
        int* arr;
        size_t size;
    public:
        IntArray(size_t n) {
            size = n;
            int* tab = new int[n];
            arr = tab;
            for(int i = 0; i < size; i++) {
                arr[i] = 0;
            }
        }

        IntArray(const IntArray& other) {
            size = other.size;
            arr = new int[size];
            for(size_t i = 0; i < size; i++) {
                arr[i] = other.arr[i];
            }
        }

        IntArray& operator=(const IntArray& other) {
            if(this == &other) return *this;
            delete[] arr;
            arr = new int[other.size];
            for(int i = 0; i < other.size; i++) {
                arr[i] = other.arr[i];
            }
            size = other.size;
            return *this;
        }

        void set(size_t i, int val) {
            if(i < size) {
                arr[i] = val;
            }
            else {
                throw out_of_range("Out of range");
            }
        }
        
        int get(size_t i) {
            if(i < size) {
                return arr[i];
            }
            else {
                throw out_of_range("Out of range");
            }
        }
        void print() {
            for(int j = 0; j < size; j++) {
                cout << arr[j] << ", ";
            }
        }
        ~IntArray() {
            delete[] arr;
        }
};

int main() {
    IntArray arr(5);
    arr.set(0, 10);
    arr.set(1, 20);
    arr.set(2, 30);
    arr.print();
    cout << endl;

    IntArray arr2 = arr; // copying
    arr2.set(0, 40);
    cout << "Arr1: "; 
    arr.print();
    cout << endl;
    cout << "Arr2: "; 
    arr2.print();

    cout << endl;
    IntArray arr3(2);
    arr3.set(0, 5);
    arr3.set(1, 5);
    cout << "Before" << endl;
    arr3.print();
    cout << endl;
    arr3 = arr2; // assignment
    cout << "After" << endl;
    arr3.print();

    return 0;
}
