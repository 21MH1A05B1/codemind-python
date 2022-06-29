n=int(input())
a,b=0,1
for i in range(2,n):
    c=a+b#1
    a=b#
    b=c
    if c==n:
        print('True')
        break
else:
    print('False')