s1=input().lower()
s2=input().lower()
a=set(s1)
b=set(s2)
c=0
for i in a:
    if i in b:
        if i!=" ":
            c+=1
print(c)

