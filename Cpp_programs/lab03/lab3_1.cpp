#include <iostream>
#include <string>
using namespace std;


int suma(int a, int b) {
    return a + b;
}

int suma(int a, int b, int c) {
    return a + b + c;
}

double suma(double a, double b) {
    return a + b;
}

void zamien(int& a, int& b) {
    int tmp = a;
    cout << "Przed zmianą: a -> " << a << " b -> " << b << endl; 
    a = b;
    b = tmp;
    cout << "Po zmianie: a -> " << a << " b -> " << b << endl;
}

void zamien(double& a, double& b) {
    double tmp = a;
    cout << "Przed zmianą: a -> " << a << " b -> " << b << endl; 
    a = b;
    b = tmp;
    cout << "Po zmianie: a -> " << a << " b -> " << b << endl;
}

int maksimum(int& a, int& b) {
    if(a > b) {
        return a;
    }
    else if (b > a) {
        return b;
    }
    else {
        cout << "Brak max: " << a << " i " << b << endl;
        return 0;
    }
}

double maksimum(double& a, double& b) {
    if(a > b) {
        return a;
    }
    else {
        return b;
    }
}

string maksimum(string& a, string& b) {
    if(a > b) {
        return a;
    }
    else 
    {
        return b;
    }
}


int main() {
    int a = 10;
    int b = 23;
    int c = 20;
    cout << "Suma: " << a << " i " << b << " to " << suma(a, b) << endl;
    cout << suma(a, b, c) << endl;
    zamien(a, b);
    
    double e = 7;
    double f = 19;
    cout << "Suma: " << e << " i " << f << " to " << suma(e, f) << endl;
    zamien(e, f);

    cout << maksimum(a, b) << endl;
    cout << maksimum(e, f) << endl;
    string imie = "Ala";
    string czasownik = "ma";
    cout << "Większe: " << maksimum(imie, czasownik) << endl;




    return 0;
}