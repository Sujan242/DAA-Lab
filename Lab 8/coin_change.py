
# https://practice.geeksforgeeks.org/problems/coin-change2448/1#
def helper(s, n , m,dp):
    if m<0:
        return 0
    if n==0:
        return 1
    if n<0:
        return 0
    if dp[n][m]!=-1:
        return dp[n][m]
    
    dp[n][m]=helper(s,n-s[m] , m,dp) + helper(s,n,m-1,dp)
    
    return dp[n][m]
    

class Solution:
    def count(self, S, m, n): 
        # code here 
        dp=[[-1 for _ in range(m+1)] for _ in range(n+1)]
        S.sort()
        return helper(S, n , m-1,dp)

