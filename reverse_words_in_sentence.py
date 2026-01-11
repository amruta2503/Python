def reverse_words_brute(sentence):
    words = sentence.split()
    
    result = []
    
    for word in words:
        rev = ""
        for ch in word:
            rev = ch + rev
        result.append(rev)
        
    return " ".join(result)

def reverse_words_better(sentence):
    rev_str = []
    words = sentence.split()
    for word in words:
        rev_str.append(word[::-1])
    
    return " ".join(rev_str)

def reverse_words_optimal(sentence):
    return " ".join([word[::-1] for word in sentence.split()])

sentence = "i love python"
print(reverse_words_brute(sentence))
print(reverse_words_better(sentence))
print(reverse_words_optimal(sentence))
