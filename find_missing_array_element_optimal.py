# optimal solution
arr = [1,2,4,5]
N=5

n = len(arr)
sum = N*(N+1)//2
print("Sum of N natural numbers is: ", sum)

sum2 = 0
for i in range(0,n):
    sum2 = sum2 + arr[i]
print("Sum of elements in the array:",sum2)

missing_element = sum - sum2

print("Missing Array Element:",missing_element)
