s=input().replace(" ","").lower()
s1=''
s1=set(s)
s1=sorted(s1)
for i in s1:
    if i!=" ":
        print(i,end='')