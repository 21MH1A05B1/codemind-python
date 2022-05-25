
n=int(input())                      #5    5
for i in range(1,n+1):              # 4  4  
    for j in range(1,n+1):           # 3     
        if i==j or i==n+1-j:         #2  2
           print(n+1+-i,end=' ')     #1    1    
        else:                              
            print('',end=' ')
    print()

