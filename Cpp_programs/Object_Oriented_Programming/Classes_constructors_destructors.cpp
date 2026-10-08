#include <iostream>
#include <string>
using namespace std;

class BankAccount {
    private:
        string ownerName;
        double balance;
    public:
        BankAccount(string name, double amount) {
            ownerName = name;
            balance = amount;
        }
        
        void deposit(double amount) {
            if(amount > 0) {
                balance += amount;
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
            cout << "Owner: " << ownerName << " Balance: " << balance << endl;            
        }

        ~BankAccount() {
            cout << "Account [" << ownerName << "] closed" << endl;
        }
};

int main() {
    BankAccount account1("Maciej", 9000);
    BankAccount account2("Jan", 1200);
    account1.print();
    account1.deposit(1000);
    account1.print();
    account2.print();
    account2.withdraw(1000);
    account2.print();
    return 0;
}
