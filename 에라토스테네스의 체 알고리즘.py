b=int(input())
# x와 arr[x]를 같은 수로 맞추기 위해 0부터 시작함
arr=[i for i in range(0,b+1)]
arr[1]=0
def f(b):
    for x in range (2,int((b+1)**0.5)+1):
        if arr[x]==0:
            continue
        j=2
        while x*j<=b:
            arr[x*j]=0
            j+=1
f(b)
for i in range(b+1):
    if arr[i]!=0:
        print(arr[i])

        
