def insertionSort(arr):
    x = len(arr)
    for i in range(1,x-1):
        j = i-1
        a = arr[i]
        print(arr)
        while j>=0 and a<arr[j]:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1]=a
    return
arr = [9,1,8,2,6,3,4,7,5]
insertionSort(arr)
print(arr)

            
            