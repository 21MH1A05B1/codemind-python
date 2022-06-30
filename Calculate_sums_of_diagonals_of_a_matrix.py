n=int(input())
p=0
s=0
for i in range(0,n):
    a=list(map(int,input().split()))
    for j in range(0,n):
        if i==j:
            p+=a[j]
        if i+j==n-1:
            s+=a[j]
print('Principal Diagonal:',end='')
print(p)
print('Secondary Diagonal:',end='')
print(s)