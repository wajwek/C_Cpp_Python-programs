#include <iostream>
#include <array>
#include <string>
using namespace std;

struct Osoba {
    string imie;
    int wiek;
};

void postarzej(Osoba& o) {
    o.wiek += 1;
}

bool znajdz_element(const int* t, int rozmiar, int szukana, int& indeks) {
    for(int i = 0; i < rozmiar; i++) {
        if(t[i] == szukana) {
            indeks = i;
            return true;
        }
    }
    return false;
}

void ustaw_na_zero1(int x) {
    x = 0;
}

void ustaw_na_zero(int* x) {
    *x = 0;
}

void ustaw_na_zero2(int& x) {
    x = 0;
}

void podwajanie(int* t) {
    int i = 0;
    while (i < 5) {
        *(t + i) *= 2;
        i++;
    }
}

void podwajanie(array<int,5>& t) {
    for(int i; i < t.size(); i++) {
        t[i] *= 2;
    }
}

void zamien(int& a, int& b) {
    int tmp = a;
    a = b;
    b = tmp;
}

int main() {
    int x = 10;
    ustaw_na_zero1(x);
    cout << x << endl;
    ustaw_na_zero(&x);
    cout << x << endl;
    x = 10;
    ustaw_na_zero2(x);
    cout << x << endl;
    
    int t[5] = {1, 2, 3, 4, 5};
    podwajanie(t);
    array<int,5> t2 = {1, 2, 3, 4, 5};
    podwajanie(t2);

    int a = 10;
    int b = 20;
    zamien(a, b);
    cout << "a: " << a << " b: " << b << endl;

    Osoba o1 = {"Maciej", 18};
    cout << "Stary wiek: " << o1.wiek << endl; 
    postarzej(o1);
    cout << "Nowy wiek: " << o1.wiek << endl;

    int indeks = 4;
    bool szukanie = znajdz_element(t, 5, 6, indeks);
    cout << "Szukanie zakończone, wynik:  " << boolalpha << szukanie << " Indeks: " << indeks << endl;

    return 0;
}