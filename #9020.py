T=int(input())
r=[i for i in range (0,10001)]
r[1]=0
t=[]
c=-1
for i in range (101):
    if r[i]==0:
        continue
    else:
        for x in range (i+i,10001,i):
            r[x]=0
for x in r:
    c+=1
    if x!=0:
        t.append(c)
for i in range (0,T):
    a=int(input())
    b=a//2
    while True:
        if r[b]!=0:
            if r[a-b]!=0:
                print('{} {}'.format(b,a-b))
                break
            e=t.index(b)-1
            while True:
                if a-t[e] in t:
                    print('{} {}'.format(t[e],a-t[e]))
                    break
                e-=1
            break
        else:
            b-=1
        
                
        
    
