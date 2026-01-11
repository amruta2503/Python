def is_anagram_brute(string1,string2):
    if len(string1) != len(string2):
        return False
        
    for ch in string1:
        if ch.count(string1) != ch.count(string2):
            return False
            
    return True

def is_anagram_better1(string1,string2):
    if len(string1) != len(string2):
        return False
    
    return sorted(string1) == sorted(string2)

def manual_sorting(string):
    chars = list(string)
    n = len(chars)
    
    for i in range(n):
        for j in range(0,n-i-1):
            if chars[j] > chars[j+1]:
                temp = chars[j]
                chars[j] = chars[j+1]
                chars[j+1] = temp
                
    return " ".join(chars)


def is_anagram_better2(string1,string2):
    if len(string1) != len(string2):
        return False
    
    return manual_sorting(string1) == manual_sorting(string2)

string1 = "race"
string2 = "care"
print(is_anagram_brute(string1,string2))
print(is_anagram_better1(string1,string2))
print(is_anagram_better2(string1,string2))
