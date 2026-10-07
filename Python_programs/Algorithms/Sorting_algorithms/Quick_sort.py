test = [9,2,15,8,34,3, 1, 7]
l = 0
r = len(test) - 1
def quick_sort(tab, left, right):
    if left >= right:
        return tab
    pivot = tab[(right + left) // 2]
    p_left = left
    p_right = right
    while p_left <= p_right:
        while tab[p_left] < pivot:
            p_left += 1
        while tab[p_right] > pivot:
            p_right -= 1
        if p_left <= p_right:
            tab[p_left], tab[p_right] = tab[p_right], tab[p_left]
            p_left += 1
            p_right -= 1
    quick_sort(tab, left, p_left - 1)
    quick_sort(tab, p_left, right)
    return tab
print(quick_sort(test, l, r))