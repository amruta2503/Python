# Optimal solution of move all zeros to the end of the array
arr = [1,0,2,3,2,0,0,4,5,1]
n = len(arr)
j=-1
for i in range(n):
    
    if(arr[i] == 0):
        j=i
        break
print("first zero is at index: ",j)

for i in range(j+1,n):
    
    if(arr[i] != 0):
        temp = arr[j]
        arr[j] = arr[i]
        arr[i] = temp
        j+=1
print("Array after the operation: ",arr)
