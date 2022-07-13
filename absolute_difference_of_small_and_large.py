n=list(map(str,input().split()))
s1=0
s2=0
for i in n:
    a=ord(min(i))
    s1+=a
    b=ord(max(i))
    s2+=b
    print(abs(s2-s1),end=' ')
    s1=s2=0