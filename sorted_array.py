# check if array is sorted

def is_sorted(arr):
    n = len(arr)
    for i in range(1,n):
        
        if(arr[i] < arr[i-1]):
            return False
      
    return True


arr = [1,3,2,3,3,4]
print(is_sorted(arr))
