n=int(input())
a=list(map(int,input().split()))
b=int(input())
for i in a:
    if b in a:
        print('True')
        break
    else:
        print('False')
        break
    