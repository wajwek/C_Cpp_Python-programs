#include <iostream>
#include <string>
using namespace std;

enum StatusStudenta {
    Aktywny,
    Absolwent,
    Urlopowany,
    Skreslony
};

struct Student {
    string imie;
    string nazwisko;
    int rok_studiow;
    float srednia_ocen; 
    StatusStudenta status;
    int index;
};

void wypisz(const Student& s) {
    string nazwyStatusow[4] = {"Aktywny", "Absolwent", "Urlopowany", "Skreslony"};
    cout << "Student: " << s.imie << " " << s.nazwisko << ", Rocznik: " << s.rok_studiow << ", Status: " << s.status << endl; 
}

int main() {
    Student s1 = {"Maciej", "Wrzesinski", 2025, 4.5};
    cout << "Podaj dane: " << endl;
    cin >> s1.imie >> s1.nazwisko >> s1.rok_studiow >> s1.srednia_ocen;
    cout << "Student: " << s1.imie << " " << s1.nazwisko << ", Rocznik: " << s1.rok_studiow << ", Avg: " << s1.srednia_ocen << endl;

    Student s2{"Jan", "Kowalski", 2025, 4.5, Absolwent, 233333};

    Student grupa[3];
    grupa[0] = {"Maciej", "Wrzesinski", 2025, 4.5};
    grupa[1] = {"Karrol", "Kowalski", 2025, 4.5};
    grupa[2] = {"Wiktor", "Zioło", 2025, 4.5};

    wypisz(grupa[0]);
    wypisz(grupa[1]);
    wypisz(grupa[2]);

}    
    