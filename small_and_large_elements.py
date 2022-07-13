n=input()
n=n.split()
if len(n)==2:
    print(min(n[0]),max(n[1]))
else:
    print(min(n[0]),max(n[len(n)-2]))