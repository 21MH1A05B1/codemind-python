N=int(input())
T=N
REV=0
while N:
    R=N%10
    REV=REV*10+R
    N=N//10
    if T==REV:
        print('True')
        break
else:
    print('False')