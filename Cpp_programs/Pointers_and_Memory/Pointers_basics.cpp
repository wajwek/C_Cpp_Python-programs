#include <iostream>
using namespace std;

void printString(const char *str) {
    int i = 0;
    while (*(str + i) != 0) {
        cout << *(str + i) << endl;
        i++;
    }
}

int main() {
    int a = 10;
    int *pointer_a = &a;

    cout << "Address: " << pointer_a << endl;
    cout << "Value: " << a << endl;
    cout << "Pointer value: " << *pointer_a << endl;

    *pointer_a = 15;
    int t[5] = {1, 2, 3, 4, 5};
    int sum = 0;
    cout << "Array: " << endl;
    for (int i = 0; i < 5; i++) {
        cout << *(t + i) << endl;
        sum += *(t + i);
    }
    cout << "Sum: " << sum << endl;
    char text[] = "Programming";
    int i = 0;
    while (*(text + i) != 0) {
        cout << *(text + i) << endl;
        i++;
    }
    cout << "Character count: " << i << endl; 
    printString(text);
    return 0;
}
