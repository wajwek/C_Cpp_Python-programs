#include <iostream>
using namespace std;

int main() {
    int grades[6] = {5,4,3,5,4,2};
    float avg = 0;
    grades[2] = 5;
    float sum = 0;
    for(int i = 0; i < 6; i++) {
        sum += grades[i];
    }
    avg = sum / 6.0;
    cout << "Grade average: " << avg << endl;
    cout << "Grades: ";
    for(int i = 0; i < 6; i++) {
        cout << grades[i] << ",";
    }
    cout << endl;
    double measurements[4] = {12.3, 15.7, 14.1, 13.9};
    int range = 4;
    float new_avg = 0;
    sum = 0.0;
    float max = 0.0;
    float min = 1000.0;
    for(int i = 0; i < range; i++) {
        sum += measurements[i];
        if(measurements[i] > max) {
            max = measurements[i];
        }
        else if(measurements[i] < min) {
            min = measurements[i];
        }
    }
    new_avg = sum / range;
    cout << "Measurements average: " << new_avg << endl;
    cout << "Min: " << min << " Max: " << max << endl;
    return 0;
}
