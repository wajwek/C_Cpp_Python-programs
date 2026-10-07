#include <iostream>
#include <string>
using namespace std;

class Address {
    private:
        string _ulica;
        string _kod_pocztowy;
        string _miasto;
        string _kraj;
    public:
        Address(string ulica, string kod, string miasto, string kraj) {
            _ulica = ulica;
            _kod_pocztowy = kod;
            _miasto = miasto;
            _kraj = kraj;
        }
        void print() {
            cout << "ul. " << _ulica << "; ";
            cout << _kod_pocztowy << " " << _miasto << " " << _kraj << endl;
        }
};

class Company {
    private:
        string _nazwa;
        size_t _nip;
        Address _adres;
    public:
        Company(string nazwa, size_t nip, string ulica, string kod, string miasto, string kraj)
            : _nazwa(nazwa), _nip(nip), _adres(ulica, kod, miasto, kraj) {
        }

        void print() {
            cout << _nazwa << " NIP: " << _nip << endl;
            cout << "Adres: "; _adres.print();
        }
};


int main() {
    Company polfarm("Polfarm", 12961976519, "Jana Pawla II", "04-821", "Kedzierzyn-kozle", "Polska");
    Company pko("PKO Bank Polski", 5260300339, "Pulawska 15", "02-515", "Warszawa", "Polska");
    Company orlen("Orlen", 7740001454, "Chemikow 7", "09-411", "Plock", "Polska");

    polfarm.print();
    pko.print();
    orlen.print();
    return 0;
}