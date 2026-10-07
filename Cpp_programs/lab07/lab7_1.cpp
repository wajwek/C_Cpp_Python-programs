#include <iostream>
#include <memory>
#include <vector>
using namespace std;

class Person : public enable_shared_from_this<Person> {
    private:
        string _imie;
        weak_ptr<Person> _mentor;
        vector<shared_ptr<Person>> _lista;
    public:
        Person(string imie) {
            _imie = imie;
            cout << "Utworzono obiekt " << _imie << endl;
        }
        ~Person() {
            cout << "Unicestwiono obiekt " << _imie << endl;
        }
        void addMentee(shared_ptr<Person> p) {
            _lista.push_back(p);
            p->_mentor = shared_from_this();
        }
        void printRelations() {
            cout << "Imie: " << _imie << endl;
            if (!_mentor.expired()) {
                cout << "Mentor: " << _mentor.lock()->_imie << endl;
            }
            cout << "Lista podopiecznych: " << endl;
            for(int i = 0; i < _lista.size(); i++) {
                cout <<" [ " << _lista[i]->_imie << " ]" << endl;
            }
        }
};

int main() {
    shared_ptr<Person> mentor = make_shared<Person>("Maciej");
    shared_ptr<Person> podopieczny1 = make_shared<Person>("Jan");
    shared_ptr<Person> podopieczny2 = make_shared<Person>("Marek");

    mentor->addMentee(podopieczny1);
    mentor->addMentee(podopieczny2);

    cout << "\nRelacje mentora:" << endl;
    mentor->printRelations();

    cout << "\nRelacje podopiecznego 1:" << endl;
    podopieczny1->printRelations();

    cout << "\nRelacje podopiecznego 2:" << endl;
    podopieczny2->printRelations();

    cout << "\nKoniec main" << endl;

    return 0;
}