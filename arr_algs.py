def arr_min(arr):
    mn = arr[0]
    for i in range(1, len(arr)):
        cur = arr[i]
        if cur < mn:
            mn = cur
    return mn


def arr_avg(arr):
    sm = 0
    for i in range(len(arr)):
        sm += arr[i]
    return sm / len(arr)


arr1 = [-10, 3, 1, 0, 5, -100]
print(arr_min(arr1))
arr2 = [2, 2, 6, 6]
print(arr_avg(arr2))