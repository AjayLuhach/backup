def selectionSort(arr):
    
    for i in range(len(arr)-1,0,-1):
        maxIdx = i
        
        print(arr)
        for j in range(0,i):
            if arr[j]>arr[maxIdx]:
                
                maxIdx = j
        arr[i],arr[maxIdx] = arr[maxIdx],arr[i]
        

arr = [9,8,7,6,5,4,3,2]
selectionSort(arr)
print(arr)


    