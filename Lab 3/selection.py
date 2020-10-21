#code
l=[]
t=int(input())

def partition(low , high , x):
    global l
    ind=l.index(x)
    l[ind] , l[high] = l[high], l[ind]
    # print(l)
    i = low
    for j in range(low,high):
        if l[j]<=x:
            
            l[i],l[j]=l[j],l[i]
            i=i+1
    
    l[i] , l[high] = l[high] , l[i]
    return i
            
        
    

def select(k , low , high):
    global l
    if low>high:
        return
    # x= l[high]   # rightmost element as pivot
    x= random.choice(l[low:high+1]) # random pivot
    rank = partition(low , high , x)
    # print(rank ,l , x , low , high)
    if rank-low==k-1:
        return x
    elif rank-low>k-1:
        return select(k,low , rank-1)
    else:
        return select(k-rank+low-1 , rank+1 , high)
    
    
while t>0:
    n=int(input())
    l=input().split()
    for i in range(n):
        l[i]=int(l[i])
    k=int(input())
    # k-=1
    print(select(k,0,n-1))
    t-=1

