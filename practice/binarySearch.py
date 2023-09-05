def binarysearch(arr,low,high,num) :
    if low>= high :
        return -1
    mid = low + (high-low)//2
    if num>arr[mid]:
        return binarysearch(arr,mid+1,high,num)
    elif num<arr[mid]:
        return binarysearch(arr,low,mid-1,num)
    else:
        return mid
    
def Main() :
    arr = [1,2,3,4,5,6,8,9]
    index = binarysearch(arr,0,len(arr)-1,8)
    print(index)
    
if __name__== "__main__":
    Main()
    
    
    
        
    