n=int(input())
a=list(map(int,input().split()))
hcf=a[0]
j=1
for i in range(n):
    while j<n:
        if a[j]%hcf==0:
            j+=1
        else:
            hcf=a[j]%hcf
print(hcf)