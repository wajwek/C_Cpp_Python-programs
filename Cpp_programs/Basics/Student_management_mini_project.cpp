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
    float gradeAverage; 
    StudentStatus status;
    int index;
};

void printStudent(const Student& s) {
    string statusNames[4] = {"Active", "Graduate", "OnLeave", "Expelled"};
    cout << "Student: " << s.firstName << " " << s.lastName << ", Index: " << s.index << ", Grade average: " << s.gradeAverage << ", Status: " << statusNames[s.status] << endl; 
}

void readStudent(Student& s1){
    cout << "Enter data: (First name, Last name, Index, Grade average, Status [0=Active, 1=Graduate, 2=OnLeave, 3=Expelled])" << endl;
    int tmp_status;
    cin >> s1.firstName >> s1.lastName >> s1.index >> s1.gradeAverage;
    cin >> tmp_status;
    s1.status = static_cast<StudentStatus>(tmp_status);
}

int main() {
    Student group[3];
    for(int i = 0; i < 3; i++) {
        readStudent(group[i]);
    }
    for(int i = 0; i < 3; i++) {
        printStudent(group[i]);
    }
    return 0;
}
