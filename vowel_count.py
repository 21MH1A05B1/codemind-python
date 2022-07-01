s=input()
s1='aeiouAEIOU'
c=0
for i in s:
    if i in s1:
        c+=1
if c==0:
    print('0')
else:
    print(c)
    