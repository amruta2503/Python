def reverse_string_brute(string):
    rev_string = ""
    n = len(string)
    for i in range(n-1,-1,-1):
        rev_string += string[i]
    print("using Brute force:",rev_string)

def reverse_string_optimal(string):
    print("using optimal:",string[::-1])


string = "reverse"
reverse_string_brute(string)
reverse_string_optimal(string)
