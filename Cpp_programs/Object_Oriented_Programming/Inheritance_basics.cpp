#include <iostream>
#include <string>
using namespace std;

class Person{
    private:
        string name;
        string surname;
    public:
        Person(string n, string s) {
            name = n;
            surname = s;
        }
        void print() {
            cout << "Name: " << name << " Surname: " << surname << endl;
        }
        string getFullName() {
            return name + " " + surname;
        }
};

class Employee : public Person {
    private:
        double salary;
    public:
        Employee(string n, string s, double p) : Person(n, s) {
            salary = p;
        }
        void print() {
            Person::print();
            cout << "Salary: " << salary << endl;
        }
};

int main() {
    Employee pracownik1 = {"Maciej", "Kowalski", 4900};
    Employee pracownik2 = {"Jan", "Kabacki", 12900};

    pracownik1.print();
    pracownik2.print();
    
    cout << "Full name: " << pracownik1.getFullName() << endl;
    return 0;
}
