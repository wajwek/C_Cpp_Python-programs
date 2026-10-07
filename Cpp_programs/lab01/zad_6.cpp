#include <iostream>
#include <string>
#include <iomanip>
using namespace std;

struct Osoba {
    string imie;
    string nazwisko;
    int numer_tel;
};

int main() {
    Osoba o1;
    cout << "Podaj swoje dane: Imie, Nazwisko, nr telefonu" << endl;
    cin >> o1.imie >> o1.nazwisko >> o1.numer_tel;
    cout << "Twoje dane to: " << endl;
    cout << o1.imie << " " << o1.nazwisko << ", tel. " << o1.numer_tel << endl;
    string linia;
    cout << "Powtórz dane, wszystko po spacji" << endl;
    cin.ignore();
    getline(cin, linia);
    cout << "Podane dane: " << linia << endl;
    int a = 3;
    int b = 4;
    double avg = (a + b) / 2.0;
    cout << "Średnia ocen: " << fixed << setprecision(2) << avg << endl;
    return 0;
}