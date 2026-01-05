#find largest element optimal solution
arr = [3,7,2,9,5]

n = len(arr)

largest = arr[0]

for i in range(1,n):
    if arr[i] > largest:
        largest = arr[i]
        
print(largest)
