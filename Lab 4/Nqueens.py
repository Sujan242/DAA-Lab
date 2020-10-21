#code
num = 0
def Nqueens(l , i):
    global num
    if i==len(l):
        q=[0 for _ in range(len(l))]
        for j in range(len(l)):
            q[j]=l[j]+1
        print(q)
        num+=1
        return
    n=len(l)
    for j in range(n):
        valid=True
        for k in range(i):
            if l[k]==j or abs(l[k]-j)==(i-k):
                valid=False
                break
        if valid:
            l[i]=j
            Nqueens(l,i+1)
            l[i]=0
    
            
def main():
    global num
    t= int(input())
    while t>0:
        n=int(input())
        l=[0 for _ in range(n)]
        Nqueens(l , 0)
        if num==0:
            print(-1)
        t-=1
main()