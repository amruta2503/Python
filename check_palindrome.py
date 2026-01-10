def is_Palindrome_brute(string):
    rev_string = ""
    string = string.lower()
    n = len(string)
    for i in range(n-1,-1,-1):
        rev_string += string[i]
        
    if rev_string == string:
        print("using brute:",True)
    else:
        print("using brute:",False)

def is_Palindrome_better(string):
    string = string.lower()
    left = 0
    right = len(string) - 1
    
    while left < right:
        if string[left] != string[right]:
            return False
        
        left+=1
        right-=1
        
    return True
    
def is_Palindrome_optimal(string):
    string = string.lower()
    return string == string[::-1]


 
string = input("Enter the string:")
is_Palindrome_brute(string)
print("using better:",is_Palindrome_better(string))
print("using optimal:",is_Palindrome_optimal(string))
