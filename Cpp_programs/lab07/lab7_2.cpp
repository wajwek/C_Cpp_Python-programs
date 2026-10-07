#include <iostream>
#include <fstream>
#include <cmath>
#include <thread>
#include <mutex>

using namespace std;
mutex coutMutex;
mutex fileMutex;

bool isPrime(int num) {
    if(num < 2) {
        return false;
    }

    for(int i = 2; i <= sqrt(num); i++) {
        if(num % i == 0) {
            return false;
        }
    }
    return true;
};

void findPrimesInRange(int start, int end, const string& filename) {
    {
        lock_guard<mutex> lock(coutMutex);
        cout << "Wątek rozpoczęty: [" << start << "-" << end << "]" << endl;
    }

    {
        lock_guard<mutex> lock(fileMutex);
        ofstream out(filename, ios::app);
        for(int i = start; i <= end; i++) {
            if(isPrime(i)) {
                out << i << endl;
            }
        }
    }

    {
        lock_guard<mutex> lock(coutMutex);
        cout << "Wątek zakończony: [" << start << "-" << end << "]" << endl;
    }
}

int main() {
    thread t1(findPrimesInRange, 1, 250000, "./wynik.txt");
    thread t2(findPrimesInRange, 250001, 500001, "./wynik.txt");
    thread t3(findPrimesInRange, 500001, 750000, "./wynik.txt");
    thread t4(findPrimesInRange, 750001, 1000000, "./wynik.txt");

    t1.join();
    t2.join();
    t3.join();
    t4.join();

    return 0;
}