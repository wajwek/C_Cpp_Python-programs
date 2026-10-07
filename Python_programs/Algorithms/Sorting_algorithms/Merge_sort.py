test = [9,2,15,8,34,3, 1, 7]
l = 0
r = len(test) - 1
def merge_sort(tab, l, r):
    if l == r:
        return [tab[l]]
    mid = (l + r) // 2
    tab = merge(merge_sort(tab, l, mid), merge_sort(tab, mid + 1, r))
    return tab
def merge(left, right):
    i = j = 0
    tab = []
    l_left = len(left)
    l_right = len(right)
    while i < l_left and j < l_right:
        if left[i] > right[j]:
            tab.append(right[j])
            j += 1
        else:
            tab.append(left[i])
            i += 1
    if i == l_left:
        tab.extend(right[j:])
    else:
        tab.extend(left[i:])
    return tab
print(merge_sort(test, l, r))
