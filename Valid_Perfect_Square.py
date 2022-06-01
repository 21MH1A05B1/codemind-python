n=int(input())
for i in range(0,n):
    a=int(input())
    for i in range(1,a+1):
        if i*i==a:
            print('True')
            break
    else:
        print('False')