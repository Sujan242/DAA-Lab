# https://practice.geeksforgeeks.org/problems/inversion-of-array/0

# time complexity = O(n^2)
t=int(input())
while t>0:
    n=int(input())
    l=input().split()
    for i in range(len(l)):
        l[i]=int(l[i])
    num_of_inversions=0
    
    for i in range(n):
        for j in range(i+1,n):
            if l[i]>l[j]:
                num_of_inversions+=1
    
    print(num_of_inversions)
    
    t-=1