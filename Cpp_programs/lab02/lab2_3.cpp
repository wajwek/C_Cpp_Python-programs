#include <iostream>
using namespace std;

int* kopiuj(int* tab, int n) {
    int* new_tab2 = new int[n];
    for (int i = 0; i < n; i++) {
        new_tab2[i] = tab[i];
    }
    return new_tab2;
}

void usun(int*& ptr) {
    delete ptr;
    ptr = nullptr;
}

int main() {
    double* p = new double;
    *p = 43.2131212;

    cout << "Wartoś double: " << *p << endl;

    delete p;

    int n;
    cout << "Podaj liczbe elementów: ";
    cin >> n; 
    cout << endl;
    int* tab = new int[n];
    double sum = 0.0;
    for(int i = 0; i < n; i++) {
        cout << "Podaj liczbę: " << endl;
        cin >> tab[i];
        sum += tab[i];
    }
    double avg = sum / n;
    for(int i = 0; i < n; i++) {
        if (tab[i] > avg) {
            cout << "Liczba większa od średniej: " << tab[i] << endl;
        }
    }
    int* new_tab = kopiuj(tab, n);
    cout << "Skopiowana tablica: " << endl;
    for(int i = 0; i < n; i++) {
        cout << new_tab[i] << endl;
    }
    delete[] tab;
    delete[] new_tab;

    int a = 10;
    int* b = new int;
    *b = a;
    usun(b);
    if (b == nullptr) {
        cout << "nullptr" << endl;
    }
    return 0;
}