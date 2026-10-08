#include <iostream>
#include <string>
using namespace std;

enum StudentStatus {
    Active,
    Graduate,
    OnLeave,
    Expelled
};

struct Student {
    string firstName;
    string lastName;
    int studyYear;
    float gradeAverage; 
    StudentStatus status;
    int index;
};

void printStudent(const Student& s) {
    string statusNames[4] = {"Active", "Graduate", "OnLeave", "Expelled"};
    cout << "Student: " << s.firstName << " " << s.lastName << ", Year: " << s.studyYear << ", Status: " << statusNames[s.status] << endl; 
}

int main() {
    Student s1 = {"Maciej", "Wrzesinski", 2025, 4.5};
    cout << "Enter data: " << endl;
    cin >> s1.firstName >> s1.lastName >> s1.studyYear >> s1.gradeAverage;
    cout << "Student: " << s1.firstName << " " << s1.lastName << ", Year: " << s1.studyYear << ", Avg: " << s1.gradeAverage << endl;

    Student s2{"Jan", "Kowalski", 2025, 4.5, Graduate, 233333};

    Student group[3];
    group[0] = {"Maciej", "Wrzesinski", 2025, 4.5};
    group[1] = {"Karol", "Kowalski", 2025, 4.5};
    group[2] = {"Wiktor", "Ziolo", 2025, 4.5};

    printStudent(group[0]);
    printStudent(group[1]);
    printStudent(group[2]);
    return 0;
}
