s=list(map(str,input().split()))
c=0
for i in s:
    for j in i:
        if ord(j)>=65 and ord(j)<=91:
            c+=1
print(c)