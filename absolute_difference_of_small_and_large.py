n=input()
n=n.split()
for i in range(len(n)):
    a=ord(max(n[i]))
    b=ord(min(n[i]))
    print(abs(a-b),end=' ')