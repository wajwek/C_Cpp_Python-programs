#include <iostream>
#include <string>
#include <iomanip>
using namespace std;

struct Person {
    string firstName;
    string lastName;
    int phoneNumber;
};

int main() {
    Person p1;
    cout << "Enter your details: First name, Last name, Phone number" << endl;
    cin >> p1.firstName >> p1.lastName >> p1.phoneNumber;
    cout << "Your details are: " << endl;
    cout << p1.firstName << " " << p1.lastName << ", tel. " << p1.phoneNumber << endl;
    string line;
    cout << "Repeat details, all separated by space" << endl;
    cin.ignore();
    getline(cin, line);
    cout << "Entered details: " << line << endl;
    int a = 3;
    int b = 4;
    double avg = (a + b) / 2.0;
    cout << "Grade average: " << fixed << setprecision(2) << avg << endl;
    return 0;
}
