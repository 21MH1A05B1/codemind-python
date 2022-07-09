def poli(n):
    b=n[::-1]
    if n==b:
        return True
    else:
        return False
n=input()
n=n.lower()
n=n.split()
c=0
for i in n:
    if poli(i):
        c+=1
print(c)
