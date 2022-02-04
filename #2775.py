num=[i for i in range (1,15)]
T=int(input())
for i in range (T):
    k=int(input())
    n=int(input())
    if n==1:
        print(1)
    else:
        for x in range (k):
            for y in range (1,n):
                if y==1:
                    num[y]+=1
                else:
                    num[y]+=num[y-1]
        print(num[n-1])
        num=[i for i in range (1,15)]
            
