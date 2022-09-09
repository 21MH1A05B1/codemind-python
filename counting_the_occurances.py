n=input()
a=input()
f=0
for i in n:
    if a in n:
        c=n.count(a)
        f=1
if f==0:
    print("-1")
else:
    print(c)