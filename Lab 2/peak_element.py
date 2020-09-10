# https://practice.geeksforgeeks.org/problems/peak-element/1
def peakElement(arr, n):
    # Code here
    l=0
    r=n-1
    while(l<r):
        mid = int((l+r)/2)
        if(arr[mid]>=arr[mid+1]):
            r=mid
        else:
            l=mid+1
    # print(l)
    return l

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        index = peakElement(arr, n)
        print(index)
