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
    float srednia_ocen; 
    StatusStudenta status;
    int index;
};

void wypisz(const Student& s) {
    string nazwyStatusow[4] = {"Aktywny", "Absolwent", "Urlopowany", "Skreslony"};
    cout << "Student: " << s.imie << " " << s.nazwisko << ", Ideks: " << s.index << ", Średnia ocen: " << s.srednia_ocen << ", Status: " << nazwyStatusow[s.status] << endl; 
}

void wczytajStudenta(Student& s1){
    cout << "Podaj dane: (Imie, Nazwisko, Ideks, Średnia ocen, Status [0=Aktywny, 1=Absolwent, 2=Urlopowany, 3=Skreslony])" << endl;
    int tmp_status;
    cin >> s1.imie >> s1.nazwisko >> s1.index >> s1.srednia_ocen;
    cin >> tmp_status;
    s1.status = static_cast<StatusStudenta>(tmp_status); //cin nie daje nam czytać czegoś co jest standardowym typem bo nie wie jak przyporządkować, u nas jest to StatusStudenta
}

int main() {
    Student grupa[3];
    for(int i = 0; i < 3; i++) {
        wczytajStudenta(grupa[i]);
    }
    for(int i = 0; i < 3; i++) {
        wypisz(grupa[i]);
    }
}    
