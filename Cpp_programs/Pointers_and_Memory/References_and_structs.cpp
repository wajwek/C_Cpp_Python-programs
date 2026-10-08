#include <iostream>
#include <array>
#include <string>
using namespace std;

struct Person {
    string firstName;
    int age;
};

void ageUp(Person& p) {
    p.age += 1;
}

bool findElement(const int* t, int size, int target, int& index) {
    for(int i = 0; i < size; i++) {
        if(t[i] == target) {
            index = i;
            return true;
        }
    }
    return false;
}

void setToZero1(int x) {
    x = 0;
}

void setToZero(int* x) {
    *x = 0;
}

void setToZero2(int& x) {
    x = 0;
}

void doubleValues(int* t) {
    int i = 0;
    while (i < 5) {
        *(t + i) *= 2;
        i++;
    }
}

void doubleValues(array<int,5>& t) {
    for(int i = 0; i < t.size(); i++) {
        t[i] *= 2;
    }
}

void swapValues(int& a, int& b) {
    int tmp = a;
    a = b;
    b = tmp;
}

int main() {
    int x = 10;
    setToZero1(x);
    cout << x << endl;
    setToZero(&x);
    cout << x << endl;
    x = 10;
    setToZero2(x);
    cout << x << endl;
    
    int t[5] = {1, 2, 3, 4, 5};
    doubleValues(t);
    array<int,5> t2 = {1, 2, 3, 4, 5};
    doubleValues(t2);

    int a = 10;
    int b = 20;
    swapValues(a, b);
    cout << "a: " << a << " b: " << b << endl;

    Person p1 = {"Maciej", 18};
    cout << "Old age: " << p1.age << endl; 
    ageUp(p1);
    cout << "New age: " << p1.age << endl;

    int index = 4;
    bool searchResult = findElement(t, 5, 6, index);
    cout << "Search finished, result: " << boolalpha << searchResult << " Index: " << index << endl;

    return 0;
}
