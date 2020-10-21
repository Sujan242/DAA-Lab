# https://practice.geeksforgeeks.org/problems/majority-element/0
def majority(l , low , high):
    if low==high:
        return l[low]
    mid = int((low+high)/2)
    left = majority(l,low,mid)
    right = majority(l , mid+1 , high)
    
    if left==right:
        return left
    
    left_freq = 0
    right_freq = 0
    
    for i in range(low,mid+1):
        if l[i]==left:
            left_freq+=1
    for i in range(mid+1 , high+1):
        if l[i]==right:
            right_freq+=1
    
    if left_freq>right_freq:
        return left
    return right
    
    
def main():
    t=int(input())
    
    while t>0:
        n=int(input())
        l=input().split()
        for i in range(n):
            l[i]=int(l[i])
        
        a = majority(l,0,n-1)
        freq=0
        for i in range(n):
            if a==l[i]:
                freq+=1
        if freq>(n/2):
            print(a)
        else:
            print(-1)
        
        t-=1
main()