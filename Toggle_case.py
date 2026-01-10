def toggle_case_brute(string):
    rev_string = ""
    for ch in string:
        if 'a'<= ch <= 'z':
            rev_string += chr(ord(ch) - 32)
        elif 'A'<= ch <= 'Z': 
            rev_string += chr(ord(ch) + 32)
        else:
            rev_string += ch
    print("Toggle case brute force solution:",rev_string)

def toggle_case_better(string):
    rev_string = ""
    for ch in string:
        if ch.islower():
            rev_string += ch.upper()
        elif ch.isupper():
            rev_string += ch.lower()
        else:
            revs_string += ch
    print("Toggle case better solution:",rev_string)
    
def toggle_case_optimal(string):
    print("Toggle case optimal solution",string.swapcase())
    
string = "MomMa"
print(f"original string: {string}")
toggle_case_brute(string)
toggle_case_better(string)
toggle_case_optimal(string)
