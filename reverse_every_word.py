n=input()
n=n.split(' ')
for i in range(len(n)):
    for j in range(len(n[i])-1,-1,-1):
        print(n[i][j],end='')
    print(end=' ')
  