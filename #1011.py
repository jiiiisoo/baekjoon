T=int(input())
for i in range (T):
    x,y=map(int,input().split())
    num=2
    distance=y-x-2
    if distance>0:
        a=int(distance**0.5)
    if distance==-1:
        num=1
    elif distance==0:
        num=2
    elif distance<=2:
        num=3
    elif distance>=a*(a+1)-1 and distance<=(a+1)**2-2:
        num+=a*2-1
    elif distance==(a+1)**2-1:
        num+=(a+1)*2-2
    else:
        num+=a*2-2
    print(int(num))
        
        
        
            
        
    
