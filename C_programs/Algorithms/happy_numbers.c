#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>

int sum_of_squares(int x) {
    int sum = 0; 
    while (x > 0) {
        int digit = x % 10;
        sum += digit * digit;
        x /= 10;
    }
    return sum;
}

bool is_in_array(const int *numbers, int capacity, int target) {
    for (int i = 0; i < capacity; i++) {
        if (numbers[i] == target) {
            return true;
        }
    }
    return false;
}

bool is_happy(int x) {
    if (x <= 1) {
        return true;
    }

    int count = 1;
    int capacity = 4;
    int *numbers = malloc(sizeof(int) * capacity);
    if (!numbers) {
        return false;
    }

    int i = 0;
    while (x != 1) {
        if (count == capacity) {
            capacity *= 2;
            int *temp = (int *)realloc(numbers, sizeof(int) * capacity);
            if (!temp) {
                free(numbers);
                return false;
            }
            numbers = temp;
        }
        numbers[i] = x;
        x = sum_of_squares(x);
        if (is_in_array(numbers, count, x)) {
            free(numbers);
            return false;
        }
        i++;
        count++;
    }
    free(numbers);
    return true;
}

int main(void) {
    int range;
    printf("Enter range: \n");
    if (scanf("%d", &range) != 1) {
        printf("Invalid input.\n");
        return 1;
    }

    for (int i = 0; i <= range; i++) {
        if (is_happy(i)) {
            printf("%d \n", i);
        }
    }
    return 0;
}
