r=[i for i in range (0,2*123456+1)]
r[1]=0
for x in range (0,int((2*123456)**0.5)+1):
    if r[x]==0:
        continue
    else:
        j=2
        while x*j<=2*123456:
            r[x*j]=0
            j+=1
while True:
    n=int(input())
    if n==0:
        break
    a=0
    for x in range (n+1,2*n+1):
        if r[x]!=0:
            a+=1
    print(a)
    a=0
