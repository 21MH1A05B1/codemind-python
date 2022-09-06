s1=input().lower()
s2=input().lower()
s3=[]
for i in s1:
    if i not in s2:
        s3.append(i)
for i in s2:
    if i not in s1:
        s3.append(i)
b=set(s3)
c=sorted(b)
for i in c:
    if i!=" ":
        print(i,end='')
