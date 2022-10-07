
s1=input().lower()
s2=input().lower()
s1,s2=s1.replace(" ",''),s2.replace(" ",'')
a=list(set(s1) &set(s2))
s=''
flag=0
for i in a:
    s+=i
    flag=1
b=sorted(s)
if flag==0:
    print("-1")
else:
    for i in b:
        print(i,end='')
