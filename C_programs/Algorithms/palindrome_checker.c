#include <stdio.h>
#include <stdbool.h>
#include <stdlib.h>
#include <string.h>

typedef struct {
    char *str;
    int len;
} StringData;

StringData read_string(void) {
    int capacity = 16;
    int len = 0;
    char *str = malloc(capacity * sizeof(char));
    if (!str) {
        printf("Memory allocation failed.\n");
        exit(1);
    }

    int c;
    while ((c = getchar()) != '\n' && c != EOF) {
        if (len + 1 >= capacity) {
            capacity *= 2;
            char *temp = realloc(str, capacity * sizeof(char));
            if (!temp) {
                free(str);
                printf("Memory reallocation failed.\n");
                exit(1);
            }
            str = temp;
        }
        str[len++] = (char)c;
    }
    str[len] = '\0';

    StringData data;
    data.str = str;
    data.len = len;
    return data;
}

bool is_palindrome(const char *str, int len) {
    int start = 0;
    int end = len - 1;
    while (start < end) {
        if (str