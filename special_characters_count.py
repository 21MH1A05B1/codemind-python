s=input()
c1=c2=c3=c4=0
for i in s:
    if ord(i)>=33 and ord(i)<=47:
        c1+=1
    if ord(i)>=58 and ord(i)<=64:
        c2+=1
    if ord(i)>=123 and ord(i)<=126:
        c3+=1
    if ord(i)>=91 and ord(i)<=96:
        c4+=1
print(c1+c2+c3+c4)