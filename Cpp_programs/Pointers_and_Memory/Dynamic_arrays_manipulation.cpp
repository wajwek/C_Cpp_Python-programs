#include <iostream>
using namespace std;

void printArray(const int* tab, size_t n) {
    for(size_t i = 0; i < n; i++) {
        cout << tab[i] << " ";
    }
    cout << endl;
}

void fillArray(int* tab, size_t n, int value) {
    for(size_t i = 0; i < n; i++) {
        tab[i] = value;
    }
}

void reverseArray(int* tab, size_t n) {
    for(size_t i = 0; i < n / 2; i++) {
        int tmp = tab[n - 1 - i];
        tab[n - 1 - i] = tab[i];
        tab[i] = tmp;
    }
}

void resizeArray(int*& tab, size_t& n, size_t new_size) {
    int* nowy = new int[new_size];
    for(size_t i = 0; i < n; i++) {
        nowy[i] = tab[i];
    }
    delete[] tab; 
    tab = nowy;
    n = new_size;
}

bool setElement(int* tab, size_t n, size_t i, int value) {
    if(i < n) {
        tab[i] = value;
        return true;
    }
    else {
        return false;
    }
}

int main() {
    size_t size = 3;
    int* tab = new int[size]; 
    
    fillArray(tab, size, 7);
    cout << "After filling: ";
    printArray(tab, size);

    tab[0] = 0;
    reverseArray(tab, size);
    cout << "After reversing (first is 0): ";
    printArray(tab, size); 

    setElement(tab, size, 2, 10);
    setElement(tab, size, 5, 12); 
    cout << "After modifications: ";
    printArray(tab, size); 
    delete[] tab;

    return 0;
}
