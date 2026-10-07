#include <stdio.h>
#include <stdlib.h>

int* generate_array(int range) {
    int *arr = malloc(sizeof(int) * (range + 1));
    if (!arr) {
        printf("Memory allocation failed.\n");
        exit(1);
    }
    return arr;
}

void sieve_primes(int *arr, int range) {
    for (int x = 0; x <= range; x++) {
        arr[x] = x;
    }
    arr[1] = 0; // 1 is not prime
    for (int i = 2; i <= range; i++) {
        if (arr[i] == 0) {
            continue;
        }
        for (int j = i * i; j <= range; j += i) {
            arr[j] = 0;
        }
    }

    for (int x = 0; x <= range; x++) {
        if (arr[x] != 0) {
            printf("[%d] ", arr[x]);
        }
    }
}

int main(void) {
    int range;

    printf("Set range: \n");
    if (scanf("%d", &range) != 1) {
        printf("Invalid input.\n");
        return 1;
    }

    if (range < 2) {
        printf("Range must be at least 2.\n");
        return 1;
    }
    int *arr = generate_array(range);
    sieve_primes(arr, range);

    free(arr);
    
    return 0;
}
