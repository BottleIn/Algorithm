str = input()
ans = ""
for word in str:
    if(word.isupper()):
        ans += word.lower()
    else:
        ans += word.upper()
        
print(ans, end='')