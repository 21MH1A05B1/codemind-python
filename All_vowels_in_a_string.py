s=input()
s1='aeiou'
s2=''
for i in s:
    if i in s1 and i not in s2:
        s2+=i
if len(s2)==5:
    print('True')
else:
    print('False')
    