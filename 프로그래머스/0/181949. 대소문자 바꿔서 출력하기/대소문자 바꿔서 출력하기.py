str = input()
str2 = ''
for n in range(len(str)):
    
    if str[n].isupper():
        str2 += str[n].lower()
    else:
        str2 += str[n].upper()
print(str2)