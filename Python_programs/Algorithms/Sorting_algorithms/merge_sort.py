test = [9,2,15,8,34,3, 1, 7]
l = 0
r = len(test) - 1
def merge_sort(arr, l, r):
    if l == r:
        return [arr[l]]
    mid = (l + r) // 2
    arr = merge(merge_sort(arr, l, mid), merge_sort(arr, mid + 1, r))
    return arr
def merge(left, right):
    i = j = 0
    arr = []
    l_left = len(left)
    l_right = len(right)
    while i < l_left and j < l_right:
        if left[i] > right[j]:
            arr.append(right[j])
            j += 1
        else:
            arr.append(left[i])
            i += 1
    if i == l_left:
        arr.extend(right[j:])
    else:
        arr.extend(left[i:])
    return arr
print(merge_sort(test, l, r))
