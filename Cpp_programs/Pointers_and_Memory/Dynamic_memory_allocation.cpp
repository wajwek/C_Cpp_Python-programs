#include <iostream>
using namespace std;

int* copyArray(int* tab, int n) {
    int* new_tab2 = new int[n];
    for (int i = 0; i < n; i++) {
        new_tab2[i] = tab[i];
    }
    return new_tab2;
}

void deletePtr(int*& ptr) {
    delete ptr;
    ptr = nullptr;
}

int main() {
    double* p = new double;
    *p = 43.2131212;

    cout << "Double value: " << *p << endl;

    delete p;

    int n;
    cout << "Enter number of elements: ";
    cin >> n; 
    cout << endl;
    int* tab = new int[n];
    double sum = 0.0;
    for(int i = 0; i < n; i++) {
        cout << "Enter number: " << endl;
        cin >> tab[i];
        sum += tab[i];
    }
    double avg = sum / n;
    for(int i = 0; i < n; i++) {
        if (tab[i] > avg) {
            cout << "Number greater than average: " << tab[i] << endl;
        }
    }
    int* new_tab = copyArray(tab, n);
    cout << "Copied array: " << endl;
    for(int i = 0; i < n; i++) {
        cout << new_tab[i] << endl;
    }
    delete[] tab;
    delete[] new_tab;

    int a = 10;
    int* b = new int;
    *b = a;
    deletePtr(b);
    if (b == nullptr) {
        cout << "nullptr" << endl;
    }
    return 0;
}
