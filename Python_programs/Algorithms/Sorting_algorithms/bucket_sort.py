test = [1, 2, 17, 7, 5, 9, 15, 10]
n = len(test)

def bucket_sort(arr, n, r):
    n_of_buckets = r // n
    buckets = []
    for i in range(n_of_buckets):
        buckets.append([])
    for j in range(n):
        index = (arr[j] * n_of_buckets) // (r + 1)
        buckets[index].append(arr[j])
    arr = []
    for k in range(n_of_buckets):
        buckets[k] = sorted(buckets[k])
        arr.extend(buckets[k])
    return arr
print(bucket_sort(test, n, 17))
