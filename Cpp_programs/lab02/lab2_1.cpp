#include <iostream>
using namespace std;

void wypisz_napis(const char *napis) {
    int i = 0;
    while (*(napis + i) != 0) {
        cout << *(napis + i) << endl;
        i++;
    }
}

int main() {
    int a = 10;
    int *pointer_a = &a;

    cout << "Adres: " << pointer_a << endl;
    cout << "Wartość: " << a << endl;
    cout << "Wartość wskaźnika: " << *pointer_a << endl;

    *pointer_a = 15;
    int t[5] = {1, 2, 3, 4, 5};
    int sum = 0;
    cout << "Tablica: " << endl;
    for (int i = 0; i < 5; i++) {
        cout << *(t + i) << endl;
        sum += *(t + i);
    }
    cout << "Suma: " << sum << endl;
    char tekst[] = "Programowanie";
    int i = 0;
    while (*(tekst + i) != 0) {
        cout << *(tekst + i) << endl;
        i++;
    }
    cout << "Liczba znaków: " << i << endl; 
    wypisz_napis(tekst);
    return 0;
}