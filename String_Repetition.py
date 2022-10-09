s=input()
n=int(input())
c,c1=0,0
l=len(s)
for i in s:
    if i=='a':
        c+=1
x=n//l
y=n%l
si=x*c
for i in range(y):
    if s[i]=='a':
     si+=1
print(si)