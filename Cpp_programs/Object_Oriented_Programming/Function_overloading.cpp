#include <iostream>
#include <string>
using namespace std;

int sum(int a, int b) {
    return a + b;
}

int sum(int a, int b, int c) {
    return a + b + c;
}

double sum(double a, double b) {
    return a + b;
}

void swapValues(int& a, int& b) {
    int tmp = a;
    cout << "Before swap: a -> " << a << " b -> " << b << endl; 
    a = b;
    b = tmp;
    cout << "After swap: a -> " << a << " b -> " << b << endl;
}

void swapValues(double& a, double& b) {
    double tmp = a;
    cout << "Before swap: a -> " << a << " b -> " << b << endl; 
    a = b;
    b = tmp;
    cout << "After swap: a -> " << a << " b -> " << b << endl;
}

int maximum(int& a, int& b) {
    if(a > b) {
        return a;
    }
    else if (b > a) {
        return b;
    }
    else {
        cout << "No max: " << a << " and " << b << endl;
        return 0;
    }
}

double maximum(double& a, double& b) {
    if(a > b) {
        return a;
    }
    else {
        return b;
    }
}

string maximum(string& a, string& b) {
    if(a > b) {
        return a;
    }
    else {
        return b;
    }
}

int main() {
    int a = 10;
    int b = 23;
    int c = 20;
    cout << "Sum of " << a << " and " << b << " is " << sum(a, b) << endl;
    cout << sum(a, b, c) << endl;
    swapValues(a, b);
    
    double e = 7;
    double f = 19;
    cout << "Sum of " << e << " and " << f << " is " << sum(e, f) << endl;
    swapValues(e, f);

    cout << maximum(a, b) << endl;
    cout << maximum(e, f) << endl;
    string name = "Ala";
    string verb = "has";
    cout << "Larger: " << maximum(name, verb) << endl;

    return 0;
}
