# second largest better

arr = [1,2,4,7,7,5]

n = len(arr)

largest = arr[0]

for i in range(1,n):
    if arr[i] > largest:
        largest = arr[i]
        
print("largest: ",largest)
        
slargest = -1

for i in range(0,n):
    if arr[i] > slargest and arr[i] != largest:
        slargest = arr[i]
        
print("second largest: ",slargest)
