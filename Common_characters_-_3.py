n=input().lower()
n=n.split(' ')
s=n[0]
x=''
for i in s:
    c=0
    for j in range(1,len(n)):
        if i in n[j]:
            c+=1
    if c==len(n)-1:
        x+=i
if len(x)==0:
    print("-1")
else:
    print(min(x))