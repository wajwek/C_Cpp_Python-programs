#include <iostream>
using namespace std;
#include <string>
class BankAccount {
    private:
        string ownerName;
        double balance;
    public:
        BankAccount(string imie, double kwota) {
            ownerName = imie;
            balance = kwota;
        }
        
        void deposit(double kwota) {
            if(kwota > 0) {
                balance += kwota;
            }
        }

        bool withdraw(double amount) {
            if(balance - amount >= 0) {
                balance -= amount;
                return true;
            }
            return false;
        }

        void print() {
            cout << "Wlasiciciel: " << ownerName << " Saldo: " << balance << endl;            
        }

        ~BankAccount() {
            cout << "Konto [" << ownerName << "] zamkniete" << endl;
        }
};

int main() {
    BankAccount konto1("Maciej", 9000);
    BankAccount konto2("Jan", 1200);
    konto1.print();
    konto1.deposit(1000);
    konto1.print();
    konto2.print();
    konto2.withdraw(1000);
    konto2.print();
    return 0;
}