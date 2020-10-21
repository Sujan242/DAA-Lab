#code
# https://practice.geeksforgeeks.org/problems/overlapping-intervals/0
def main():
    t=int(input())
    while(t>0):
        
        n=int(input())
        interval=[]
        l= input().split()
        # print(l)
        for i in range(n):
            interval.append([int(l[2*i]) , int(l[2*i+1])])
        interval.sort()
        
        i=0
        merged=[]
        # print(interval)
        while(i<n):
            # print(i)
            start_time = interval[i][0]
            finish_time = interval[i][1]
            # print(start_time , finish_time)
            i+=1
            while i<n and finish_time>=interval[i][0]:
                finish_time = max(finish_time , interval[i][1])
                i+=1
            
            merged.append([start_time , finish_time])
        
        for x in merged:
            print(x[0],x[1] , end=' ')
        print()
            
        t-=1
main()