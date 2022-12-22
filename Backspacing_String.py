s1=input()
s2=input()
l=[]
m=[]
for i in s1:
    if i=="#":
        l.pop()
    else:
        l.append(i)
for i in s2:
    if i=="#":
        m.pop()
    else:
        m.append(i)
if l==m:
    print('True')
else:
    print('False')