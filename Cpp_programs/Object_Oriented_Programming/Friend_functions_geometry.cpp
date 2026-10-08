#include <iostream>
#include <cmath>
using namespace std;

class Triangle {
    private:
        double a, b, c;
    public:
        Triangle(double e, double d, double f) {
            if((e > 0) && (d > 0) && (f > 0)) {
                a = e;
                b = d;
                c = f;
            }
            else {
                a = 1;
                b = 1;
                c = 1;
            }
        }
        void print() {
            cout << "Side 1: " << a << endl;
            cout << "Side 2: " << b << endl;
            cout << "Side 3: " << c << endl;
        }
        friend double area(const Triangle&);
};

double area(const Triangle& t) {
    double s = (t.a + t.b + t.c) / 2;
    double areaVal = sqrt(s * (s - t.a) * (s - t.b) * (s - t.c));
    return areaVal;
}

int main() {
    Triangle tab[3] {
        Triangle(3, 4, 5),
        Triangle(5, 5, 6),
        Triangle(5, 5, 5)
    };
    for(int i = 0; i < 3; i++) {
        double a = area(tab[i]);
        cout << "Area " << i << " -> " << a << endl;
        tab[i].print();
    }
    return 0;
}
