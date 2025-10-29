s1 = "these+notes#reveal9Newton seeking-out an(!underlying structure to /the\\pyramid:the unit of measurement?used>by its builders"
clean = ''

for x in s1:
    if x.isalpha() or x.isspace():
        clean = clean + x
    else:
        clean = clean + ' '
print(clean)