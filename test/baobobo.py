def Maopao(arr):
    n = len(arr)

    for i in range(n):
        for j in range(0,n-i-1):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]

arr = [32,242,53,53,23,2,1,133,4]
print("原数组:",arr)

Maopao(arr)
print('Before:')
for s in range(len(arr)):
    print("%d"%arr[s])