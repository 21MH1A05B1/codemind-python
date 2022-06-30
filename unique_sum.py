n=int(input())
a=list(map(int,input().split()))
s=[]
for i in a:
    if i not in s:
        s.append(i)
x=0
for i in s:
    x+=i
print(x)
        