arr = [1,0,2,3,2,0,0,4,5,1]

print("initally array is: ", arr)
n = len(arr)

temp = []

for i in range(n):
    
    if(arr[i] != 0 ):
        temp.append(arr[i])
print("Temporary array:",temp)

temp_size = len(temp)

for i in range(temp_size):
    arr[i] = temp[i]
    
print("array after putting the elements back from the temporary array:",arr)

for i in range(temp_size,n):
    arr[i] = 0
    
print("Array with all the Zeros at end:",arr)
