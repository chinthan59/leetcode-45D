def range_q(l,u,arr):
    return sum(arr[0:u]) - sum(arr[:l-1])

arr=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
res=range_q(2, 5, arr)
print(res) 