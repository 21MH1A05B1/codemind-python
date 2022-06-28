n=int(input())
sum=0
import math
sqr=math.pow(n,2)
while sqr>0:
    r=sqr%10
    sum=sum+r
    sqr=sqr//10
if sum==n:
    print('Neon Number')
else:
    print('Not Neon Number')
