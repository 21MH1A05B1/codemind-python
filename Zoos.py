n=input()
x=y=0
for i in n:
    if i=='z':
        x+=1
    elif i=='o':
        y+=1
if y==2*x:
    print('Yes')
else:
    print('No')
        