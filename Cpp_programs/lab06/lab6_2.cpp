#include <iostream>
#include <string>
using namespace std;

class User {
    private:
        string _username;
        string _email;
        static int _count;
    public:
        User(string username, string email) {
            _username = username;
            _email = email;
            _count++;
        }
        void print() {
            cout << "Username: " << _username << "; Email: " << _email << endl;
        }
        static int getCount() {
            return _count;
        }
        ~User() {
            _count--;
        }
};

int User::_count = 0;

int main() {
    cout << "Przed: " << User::getCount() << endl;

    User user1("maciej", "maciej@wp.pl");
    cout << "Count 1: " << User::getCount() << endl;

    {
        User user2("anna", "anna@wp.com");
        User user3("piotr", "piotr@wp.com");
        user2.print();
        user3.print();
        cout << "Count w bloku: " << User::getCount() << endl;
    }

    cout << "Po 1 bloku: " << User::getCount() << endl;

    {
        User user4("kuba", "kuba@wp.com");
        user4.print();
    }

    cout << "Po 2 bloku: " << User::getCount() << endl;
    // count jest 1 ponieważ user2,3,4 zostały zniszczone po wyjściu z klamerek, całkiem ciekawe
    return 0;
}