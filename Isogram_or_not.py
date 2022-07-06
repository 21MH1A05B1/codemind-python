n=input()
s=n.lower()
x=list(s)
b=[]
for i in x:
    if i not in b:
        b.append(i)
if len(b)==len(x):
    print('True')
else:
    print('False')