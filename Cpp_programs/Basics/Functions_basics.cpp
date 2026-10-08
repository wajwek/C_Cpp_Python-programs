#include <iostream>
#include <string>
using namespace std;

double average(double a, double b) {
    return (a + b) / 2.0;
}

void greet() {
    cout << "Hello! This is the greet function." << endl;
}

void setToZero(int x) {
    x = 0;
    cout << "Inside function: " << x << endl;
}

int minVal(int a, int b) {
    if(a <= b) {
        return a;
    }
    else if(b < a) {
        return b;
    }
    return 0;
}

int maxVal(int a, int b) {
    if(a >= b) {
        return a;
    }
    else if(b > a) {
        return b;
    }
    return 0;
}

int main() {
    
    greet();
    int a, b;
    cout << "Enter two numbers: " << endl;
    cin >> a >> b;
    double avg = average(a, b);
    cout << "Average: " << avg << endl;
    int x = 10;
    setToZero(x);
    cout << "In main: " << x << endl;
    int minimum = minVal(a, b);
    int maximum = maxVal(a, b);
    cout << "min: " << minimum << " max: " << maximum << endl;

}
