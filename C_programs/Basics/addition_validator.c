#include <stdio.h>
#include <stdlib.h>
#include <string.h>

// Function that adds two numbers together
int add_function(int a, int b) {
    return a + b;
}

int main(void) {
    int a;
    int b;
    int check1;
    int check2;
    printf("Enter numbers to add:\n");
    printf("First number -> ");
    check1 = scanf("%d", &a);
    printf("Second number -> ");
    check2 = scanf("%d", &b);

    if (check1 == 1 && check2 == 1) {
        printf("Sum: %d\n", add_function(a, b));
    } else {
        printf("Invalid input format, exiting program.\n");
    }

    return 0;
}
