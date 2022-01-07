T=int(input())
r=[i for i in range (0,10001)]
r[1]=0
for i in range (0, int(10000**0.5)+1):
    if r[i]==0:
        continue
    else:
        for x in range (i+i,10001,i):
            r[x]=0
for i in range (0,T):
    n=int(input())
    ave=n//2
    f_count=ave
    s_count=ave
    while f_count>0:
        if r[f_count]!=0 and r[s_count]!=0:
            print(f_count, s_count)
            break
        f_count-=1
        s_count+=1
