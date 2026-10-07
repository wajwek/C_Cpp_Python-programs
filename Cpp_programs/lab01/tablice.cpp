#include <iostream>
using namespace std;

int main() {
    int oceny[6] = {5,4,3,5,4,2};
    float avg = 0;
    oceny[2] = 5;
    float suma = 0;
    for(int i = 0; i < 6; i++) {
        suma += oceny[i];
    }
    avg = suma / 6.0;
    cout << "Średnia ocen: " << avg << endl;
    cout << "Oceny: ";
    for(int i = 0; i < 6; i++) {
        cout << oceny[i] << ",";
    }
    cout << endl;
    double pomiary[4] = {12.3, 15.7, 14.1, 13.9};
    int range = 4;
    float new_avg = 0;
    suma = 0.0;
    float max = 0.0;
    float min = 1000.0;
    for(int i = 0; i < range; i++) {
        suma += pomiary[i];
        if(pomiary[i] > max) {
            max = pomiary[i];
        }
        else if(pomiary[i] < min) {
            min = pomiary[i];
        }
    }
    new_avg = suma / range;
    cout << "Średnia pomiarów: " << new_avg << endl;
    cout << "Min: " << min << " Max: " << max << endl;
    return 0;
}