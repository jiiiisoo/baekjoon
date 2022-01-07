def f(n,k):
    if k==1:
        p=1
    elif n==0:
        p=k
    else:
        p=f(n,k-1)+f(n-1,k)
    return p
case=int(input())
for x in range (0,case):
    n=int(input())
    k=int(input())
    print(f(n,k))
