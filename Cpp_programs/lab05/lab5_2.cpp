#include <iostream>
using namespace std;

class IntArray {
    private:
        int* arr;
        size_t rozmiar;
    public:
        IntArray(size_t n) {
            rozmiar = n;
            int* tab = new int[n];
            arr = tab;
            for(int i = 0; i < rozmiar; i++) {
                arr[i] = 0;
            }
        }

        IntArray(const IntArray& other) {
            rozmiar = other.rozmiar;
            arr = new int[rozmiar];
            for(size_t i = 0; i < rozmiar; i++) {
                arr[i] = other.arr[i];
            }
        }

        IntArray& operator=(const IntArray& other) {
            if(this == &other) return *this;
            delete[] arr;
            arr = new int[other.rozmiar];
            for(int i = 0; i < other.rozmiar; i++) {
                arr[i] = other.arr[i];
            }
            rozmiar = other.rozmiar;
            return *this;
        }

        void set(size_t i, int val) {
            if(i < rozmiar) {
                arr[i] = val;
            }
            else {
                throw out_of_range("Poza zakresem");
            }
        }
        
        int get(size_t i) {
            if(i < rozmiar) {
                return arr[i];
            }
            else {
                throw out_of_range("Poza zakresem");
            }
        }
        void print() {
            for(int j = 0; j < rozmiar; j++) {
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


    IntArray arr2 = arr; //kopiowanie
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
    cout << "Przed" << endl;
    arr3.print();
    cout << endl;
    arr3 = arr2; //przypisanie
    cout << "Po" << endl;
    arr3.print();

    cout << endl << "Test" << endl;
    //arr3.set(100, 5);
    cout << endl << "Test 2" << endl;
    //arr3.get(100);
    return 0;
}