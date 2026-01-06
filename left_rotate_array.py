#left rotate array by D places Brute

arr = [1,2,3,4,5,6,7]
d = 3
n= len(arr)

d = d % n

temp = []

for i in range(0,d):
    temp.append(arr[i])
    
print(temp)

for i in range(d,n):
    arr[i-d] = arr[i]
    
print("array",arr)

for i in range(0,d):
    
    arr[n-d+i] = temp[i]
    
print("Left rotated array", arr)
    
    
    
