# finding missing element brute

arr = [1,2,4,5]
N=5
n = len(arr)
missing_element = 0
for i in range(1,N+1):
    flag = 0
    for j in range(0,n):
        if arr[j] == i:
            flag = 1
            break
    if flag == 0:
        missing_element = i

print("Missing Array Element: ",missing_element)
