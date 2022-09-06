s=input().lower().replace(" ","")
s2=set(s)
a=sorted(s2)
for i in a:
    if i!=" ":
        print(i,end='')
