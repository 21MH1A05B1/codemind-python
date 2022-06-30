n=list(map(int,input().split()))[:3]
m=list(map(int,input().split()))[:3]
d=0
c=0
for i in range(3):
        if n[i]>m[i]:
            c+=1
        elif(n[i]<m[i]):
            d+=1
print(c,d)