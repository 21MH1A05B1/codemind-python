n=input().lower()
n=n.split(' ')
s=n[0]
c,count=0,0
for i in s:
    c=0
    for j in range(1,len(n)):
        if i in n[j]:
            c+=1
    if c==len(n)-1:
        count+=1
print(count)