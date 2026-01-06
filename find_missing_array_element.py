# Better solution

arr = [1,2,4,5]
N=5
n = len(arr)
missing_element = 0
hash_array = [0] * (N+1)

for i in arr:
    hash_array[i] = 1
    
print("hash array:", hash_array)

for i in range(1,N+1):
    
    if hash_array[i] == 0:
        missing_element = i
        break

print("Missing Array Element: ",missing_element)
