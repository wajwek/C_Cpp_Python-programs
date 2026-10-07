from random import randint

def generate_tab():
    arr = []
    for i in range(20):
        arr.append(randint(1, 10))
    return arr

test = generate_tab()
print(test)
length = len(test)

def counting_sort(arr, n):
    new_arr = [0] * n
    for i in range(n):
        new_arr[arr[i]] += 1
    sum_tab = [0] * n
    sum_tab[0] = new_arr[0]
    for i in range(1, n):
        sum_tab[i] = new_arr[i] + sum_tab[i - 1]
    print(new_arr)
    print(sum_tab)
    sorted_arr = [0] * n
    for i in range(n - 1, -1, -1):
        sorted_arr[sum_tab[arr[i]] - 1] = arr[i]
        sum_tab[arr[i]] -= 1
    print(sorted_arr)

counting_sort(test, length)

