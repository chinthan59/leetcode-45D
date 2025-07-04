def kth_small(arr,k):
    arr.sort()
    print(arr[k-1])

arr=[7, 10, 7, 3, 20, 15]

kth_small(arr,3)