#include <iostream>
#include <string>
#include <vector>
using namespace std;

class Student {
    private:
        string name;
        vector<int> grades;
    public:
        Student(string imie) {
            name = imie;
        }
        void addGrade(int grade) {
            if(grade >= 2 && grade <= 5) {
                grades.push_back(grade);
            }
        }
        double average(){
            double suma = 0;
            double avg = 0;
            for(int i = 0; i < grades.size(); i++) {
                suma += grades[i];
            }
            avg = suma / grades.size();
            return avg;
        }
        void print() {
            cout << "Student: " << name << endl;
            cout << "Grades avg: " << average() << endl;
        }
        ~Student() {
            cout << "Student [" << name << "] usuniety" << endl;
        }
};

int main() {

    Student* tab[3];

    tab[0] = new Student("Maciej");
    tab[1] = new Student("Wojciech");
    tab[2] = new Student("Mateusz");

    tab[0]->addGrade(3);
    tab[1]->addGrade(5);
    tab[2]->addGrade(4);
    tab[2]->addGrade(3);
    double max = 0.0;
    int idx;
    for(int i = 0; i < 3; i++) {
        tab[i]->print();
        if(tab[i]->average() > max) {
            max = tab[i]->average();
            idx = i;
        }
    }
    cout << "Najlepszy ";
    tab[idx]->print();
    
    return 0;
}