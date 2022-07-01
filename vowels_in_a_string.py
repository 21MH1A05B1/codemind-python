s=input()
a=input()
b=0
for i in range(len(s)):
    if s[i]==a:
        print('True')
        print(i)
        b=1
        break
if b!=1:
    print('False')
        
    