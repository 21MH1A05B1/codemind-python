n=int(input())
for i in range(n):
    a=input()
    b='0123456789'
    c=0
    for i in a:
        if i in b:
            c+=1
    if c==len(a):
        print('True')
    else:
        print('False')
        
    