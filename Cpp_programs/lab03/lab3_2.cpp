#include <iostream>
using namespace std;

void wypisz(const int* tab, size_t n) {
    for(size_t i = 0; i < n; i++) {
        cout << tab[i] << " ";
    }
    cout << endl;
}

void wypelnij(int* tab, size_t n, int wartosc) {
    for(size_t i = 0; i < n; i++) {
        tab[i] = wartosc;
    }
}

void odwroc_tablice(int* tab, size_t n) {
    for(size_t i = 0; i < n / 2; i++) {
        int tmp = tab[n - 1 - i];
        tab[n - 1 - i] = tab[i];
        tab[i] = tmp;
    }
}

void rozszerz(int*& tab, size_t& n, size_t nowy_rozmiar) {
    int* nowy = new int[nowy_rozmiar];
    for(size_t i = 0; i < n; i++) {
        nowy[i] = tab[i];
    }
    delete[] tab; 
    tab = nowy;
    n = nowy_rozmiar;
}

bool ustaw_element(int* tab, size_t n, size_t i, int wartosc) {
    if(i < n) {
        tab[i] = wartosc;
        return true;
    }
    else {
        return false;
    }
}

int main() {
    size_t rozmiar = 3;
    int* tab = new int[rozmiar]; 
    
    wypelnij(tab, rozmiar, 7);
    cout << "Po wypelnieniu: ";
    wypisz(tab, rozmiar);

    tab[0] = 0;
    odwroc_tablice(tab, rozmiar);
    cout << "Po odwroceniu (pierwszy to 0): ";
    wypisz(tab, rozmiar); 

    ustaw_element(tab, rozmiar, 2, 10);
    ustaw_element(tab, rozmiar, 5, 12); 
    cout << "Po modyfikacjach: ";
    wypisz(tab, rozmiar); 
    delete[] tab;

    return 0;
}