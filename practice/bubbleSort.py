def selectionSort(arr,size):
    
    for i in range(size-1,0,-1):
        
        for j in range(0,i):
            
            if arr[j]>arr[j+1]:
                arr[j],arr[j+1]=arr[j+1],arr[j]
            
               
        
        print(arr)
    
        
    
    
    
arr = [93,75,64,12,43,27,39]
selectionSort(arr,len(arr))
 