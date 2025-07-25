def sorting(array):
    n = len(array)
    for i in range(n):
        for j in range(0, n - i - 1):
            if array[j] > array[j + 1]:
                array[j], array[j + 1] = array[j + 1], array[j]
    return array

def get_kth_smallest(array, k):
        sorting(array)
        return array[k - 1]              

array = [7, 10, 4, 3, 20, 15]
k = 3

print(get_kth_smallest(array, k))
