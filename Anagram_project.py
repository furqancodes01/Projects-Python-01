s1 = "snooze alarams"
s2= "alas, no more Z's"
s1 = s1.lower()
s2 = s2.lower()

for x in s1:
    if x.isalpha():
        if s1.count(x) != s1.count(x):
            print('not a Anagram')
            break
else:
    print("it is a Anagram")