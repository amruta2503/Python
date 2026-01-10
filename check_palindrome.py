def is_Palindrome_brute(string):
    rev_string = ""
    n = len(string)
    
    for i in range(n-1,-1,-1):
        rev_string += string[i]
        
    if rev_string == string:
        print("using brute:",True)
    else:
        print("using brute:",False)
    
    
def is_Palindrome_optimal(string):
    return string == string[::-1]

string = input("Enter the string:")
is_Palindrome_brute(string)
print("using optimal:",is_Palindrome_optimal(string))
