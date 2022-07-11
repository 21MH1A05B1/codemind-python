n=int(input())
for i in range(n):
    a=input()
    for i in a:
        if ord(i)>=49 and ord(i)<=57:
            print('Yes')
            break
    else:
        print('No')

    