def swap(arr,element1,element2):
    temp = arr[element1]
    arr[element1] = arr[element2]
    arr[element2] = temp
    
    return element1,element2
    
def sort_zeroes_twos(arr):
    n = len(arr)
    low = mid = 0
    high = n-1
    
    while mid <= high:
        if arr[mid] == 0:
            swap(arr,mid,low)
            mid += 1
            low += 1
        elif arr[mid] == 1:
            mid += 1
        else:
            swap(arr,mid,high)
            high -= 1
    print(arr)

arr = [0,1,2,0,1,2,1,2,0,0,0,1]
sort_zeroes_twos(arr)
