s=input().replace(" ","").lower()
s1=''
c=0
s1=set(s)
s1=sorted(s1)
for i in s1:
    if i!=" ":
        c+=1
print(c)