#code
# https://practice.geeksforgeeks.org/problems/fractional-knapsack/0
def main():
    t=int(input())
    
    while t>0:
        n,w =input().split()
        n,w = int(n) , int(w)
        values=[]
        weights=[]
        ratios=[]
        l=input().split()
        for i in range(n):
            values.append(int(l[2*i]))
            weights.append(int(l[2*i+1]))
            ratios.append([values[-1]/weights[-1],i])
        ratios.sort(reverse=True)
        i=0
        ans=0
        while i<n and w>0:
            
            ind = ratios[i][1]
            # print(weights[ind])
            if weights[ind]<=w:
                w-=weights[ind]
                ans+=values[ind]
            else:
                
                # print((w*1.0/weights[ind])*values[ind])
                ans+= (w*1.0/weights[ind])*values[ind]
                w=0
            i+=1
        print(round(ans*1.0,2))
        t-=1
main()