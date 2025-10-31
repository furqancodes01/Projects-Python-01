import re
def panagram (phrase):
    letters = re.sub(r'[^a-zA-Z]','',phrase) 
    letters_set = set(letters.lower())
    
    if len(letters_set) == 26:
        return True
    else:
        return False
    
str = "The quick brown fox jumps over the lazy dog"
print(panagram(str))