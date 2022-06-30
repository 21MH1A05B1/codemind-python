n=int(input())
a=list(map(int,input().split()))
s1=0
s2=0
for i in range(0,(n//2)+1):
    s1=s1+i
print(s1)
for i in range((n//2)+1,n+1):
    s2=s2+i
print(s2)