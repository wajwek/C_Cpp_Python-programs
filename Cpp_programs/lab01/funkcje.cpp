#include <iostream>
#include <string>
using namespace std;

double srednia(double a, double b) {
    return (a + b) / 2.0;
}

void witaj() {
    cout << "Cześć! To jest funkcja witaj()." << endl;
}

void ustawNaZero(int x) {
    x = 0;
    cout << "W funkcji: " << x << endl;
}

int min(int a, int b) {
    if(a <= b) {
        return a;
    }
    else if(b < a) {
        return b;
    }
    return 0;
}

int max(int a, int b) {
    if(a >= b) {
        return a;
    }
    else if(b > a) {
        return b;
    }
    return 0;
}

int main() {
    
    witaj();
    int a, b;
    cout << "Podaj dwie liczby: " << endl;
    cin >> a >> b;
    double avg = srednia(a, b);
    cout << "Średnia: " << avg << endl;
    int x = 10;
    ustawNaZero(x);
    cout << "W main: " << x << endl;
    int minimum = min(a, b);
    int maximum = max(a, b);
    cout << "min: " << minimum << " max: " << maximum << endl;

}