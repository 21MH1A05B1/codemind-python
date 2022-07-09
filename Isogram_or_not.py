s=input()
s=s.lower()
b=len(s)
a=[]
for i in s:
    if i not in a:
        a.append(i)
if b==len(a):
    print('True')
else:
    print('False')
        