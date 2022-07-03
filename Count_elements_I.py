n,m=map(int,input().split())
a=list(map(int,input().split()))
b=list(map(int,input().split()))
a,b=set(a),set(b)
a,b=list(a),list(b)
c=[]
for i in range(len(a)):
    if a[i] in b:
        c.append(a[i])
print(len(c))
