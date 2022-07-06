a=input()
b=input()
a=a.lower()
b=b.lower()
s1=list(a)
s2=list(b)
c=0
for i in s1:
    if i in s2:
        c=1
    else:
        c=0
        break
if c==1:
    print('True')
else:
    print('False')
    