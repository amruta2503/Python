def two_sum_brute(arr,target):
    n = len(arr)
    for i in range(0,n):
        for j in range(i+1,n):
            if arr[i] + arr[j] == target:
                print(i,j)
                return True
    return False            
            
def two_sum_better_hashmap(arr,target):
    seen = {}
    n = len(arr)
    
    for i in range(0,n):
        
        remaining = target - arr[i]
        
        if remaining in seen:
            print(f"Indexes are: {seen[remaining]},{i}")
            print(f"Elements are: {remaining},{arr[i]}")
            return True
        seen[arr[i]] = i
    return False
                
def bubble_sort(arr):
    n = len(arr)
    for i in range(0,n):
        
        for j in range(0,n-i-1):
            
            if arr[j] > arr[j+1]:
                temp = arr[j]
                arr[j] = arr[j+1]
                arr[j+1] = temp
    print("Sorted Array: ",arr)
    return arr
    
    
def two_sum_better_two(arr,target):
    sorted_arr = bubble_sort(arr.copy())
    
    n = len(sorted_arr)
    
    left = 0
    right = n-1
    
    while left<right:
        curr_sum = sorted_arr[left] + sorted_arr[right]
        if curr_sum == target:
            print("Elements are:",sorted_arr[left], sorted_arr[right])
            print("Indexes are:",left,right)
            return True
        elif curr_sum > target:
            right -= 1
        else:
            left += 1
    return False

arr = [2,6,5,8,11]
target = 14
two_sum_brute(arr,target)
two_sum_better_hashmap(arr,target)
two_sum_better_two(arr,target)
