s=input()
s=s.lower()
s=s.replace(" ","")
s2=[]
for i in s:
    if s.count(i)==1:
        s2.append(i)

a=sorted(s2)
for i in a:
    if i!=" ":
        print(i,end='')