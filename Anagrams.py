s1=input()
s2=input()
s1=s1.lower()
s2=s2.lower()
a=list(s1)
b=list(s2)
c=0
for i in a:
    if i in b:
        c=1
    else:
        c=0
        break
if c==1:
    print('True')
else:
    print('False')