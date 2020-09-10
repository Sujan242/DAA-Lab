# https://www.hackerrank.com/contests/launchpad-1-winter-challenge/challenges/shift-plates/submissions/code/1326386900
def solve(n , s , t, i):
    if(n<=0):
        return 
    solve(n-1 , s, i , t)
    print(f'Moving ring {n} from {s} to {t}')
    solve(n-1 , i , t , s)

n=int(input())

solve(n , "A" , "B" , "C")