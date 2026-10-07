#include "narzedzia.h"
#include <iostream>
int* utworz_tablice(int n) {
 int* t = new int[n];
 for (int i = 0; i < n; ++i)
 t[i] = i * 2;
 return t;
}
void wypisz(const int* t, int n) {
 for (int i = 0; i < n; ++i)
 std::cout << t[i] << " ";
 std::cout << std::endl;
}
void usun(int*& ptr) {
 delete[] ptr;
 ptr = nullptr;
}

