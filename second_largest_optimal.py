# second largest optimal

arr = [1,2,4,7,7,5]

n = len(arr)

largest = arr[0]

slargest = -1

for i in range(1,n):
    
    if arr[i] > largest and arr[i] != largest:
        slargest = largest
        largest = arr[i]
    else:
        if arr[i] > slargest and arr[i] != largest:
            slargest = arr[i]
        
print(f"Largest:{largest} and Second largest:{slargest}")
