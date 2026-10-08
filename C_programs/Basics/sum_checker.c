#include <stdio.h>
#include <stdlib.h>
#include <string.h> 

// Function that adds two numbers to each other
int add_function(int a, int b) {
    return a + b;
}

int main() {
    int a;
    int b;
    int check1;
    int check2;
    printf("Podaj liczby do dodania:\n");
    printf("Pierwsza liczba ->");
    check1 = scanf("%d", &a);
    printf("Druga liczba ->");
    check2 = scanf("%d", &b);
    if (check1 == 0 && check2 == 0){
        printf("Suma: %d", add_function(a, b));
    }
    else {
        printf("Zły format wejścia, zamykanie programu");
    }
    
}
