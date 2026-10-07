test = [1, 2, 17, 7, 5, 9, 15, 10]
n = len(test)

def Bucket_sort(tab, n, r):
    n_of_buckets = r // n
    buckets = []
    for i in range(n_of_buckets):
        buckets.append([])
    for j in range(n):
        index = (tab[j] * n_of_buckets) // (r + 1)
        buckets[index].append(tab[j])
    tab = []
    for k in range(n_of_buckets):
        buckets[k] = sorted(buckets[k])
        tab.extend(buckets[k])
    return tab
print(Bucket_sort(test, n, 17))




