#include <iostream>
#include <memory>
#include <vector>
using namespace std;

class Person : public enable_shared_from_this<Person> {
    private:
        string _name;
        weak_ptr<Person> _mentor;
        vector<shared_ptr<Person>> _mentees;
    public:
        Person(string name) {
            _name = name;
            cout << "Created object " << _name << endl;
        }
        ~Person() {
            cout << "Destroyed object " << _name << endl;
        }
        void addMentee(shared_ptr<Person> p) {
            _mentees.push_back(p);
            p->_mentor = shared_from_this();
        }
        void printRelations() {
            cout << "Name: " << _name << endl;
            if (!_mentor.expired()) {
                cout << "Mentor: " << _mentor.lock()->_name << endl;
            }
            cout << "Mentees list: " << endl;
            for(int i = 0; i < _mentees.size(); i++) {
                cout <<" [ " << _mentees[i]->_name << " ]" << endl;
            }
        }
};

int main() {
    shared_ptr<Person> mentor = make_shared<Person>("Maciej");
    shared_ptr<Person> podopieczny1 = make_shared<Person>("Jan");
    shared_ptr<Person> podopieczny2 = make_shared<Person>("Marek");

    mentor->addMentee(podopieczny1);
    mentor->addMentee(podopieczny2);

    cout << "\nMentor relations:" << endl;
    mentor->printRelations();

    cout << "\nMentee 1 relations:" << endl;
    podopieczny1->printRelations();

    cout << "\nMentee 2 relations:" << endl;
    podopieczny2->printRelations();

    cout << "\nEnd of main" << endl;

    return 0;
}
