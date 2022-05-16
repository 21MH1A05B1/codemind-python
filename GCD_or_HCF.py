
def hcf(a,b):#(3,9)
    if a>b:
        a,b=b,a
    c=a#c=3
    while True:
        if a%c==0 and b%c==0:#3%3==0 and 6%3==0
            return c #return 3
        c-=1
a,b=map(int,input().split())
print(hcf(a,b))
