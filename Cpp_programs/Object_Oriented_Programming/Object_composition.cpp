#include <iostream>
#include <string>
using namespace std;

class Address {
    private:
        string _street;
        string _postalCode;
        string _city;
        string _country;
    public:
        Address(string street, string postalCode, string city, string country) {
            _street = street;
            _postalCode = postalCode;
            _city = city;
            _country = country;
        }
        void print() {
            cout << "St. " << _street << "; ";
            cout << _postalCode << " " << _city << " " << _country << endl;
        }
};

class Company {
    private:
        string _name;
        size_t _taxId;
        Address _address;
    public:
        Company(string name, size_t taxId, string street, string postalCode, string city, string country)
            : _name(name), _taxId(taxId), _address(street, postalCode, city, country) {
        }

        void print() {
            cout << _name << " Tax ID: " << _taxId << endl;
            cout << "Address: "; _address.print();
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
