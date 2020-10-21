# top down
def edit_distance(s1,s2,i , j):
	n1=len(s1)
	n2=len(s2)
	if i>=n1 and j>=n2:
		return 0

	if i>=n1:
		return n2-j
	if j>=n2:
		return n1-i

	if s1[i]==s2[j]:

		return edit_distance(s1,s2,i+1,j+1)

	l1 = 1 + edit_distance(s1,s2,i+1,j+1)  #substitute
	l2 = 1 + edit_distance(s1,s2,i+1,j)    #delete from s1
	l3 = 1 + edit_distance(s1,s2 , i,j+1)  #insert to s1 


	ans= min(l1,l2,l3)
	return ans

#bottom up
def edit_distance2(s1,s2):
	n1 = len(s1)
	n2 = len(s2)
	dp=[[0 for _ in range(n2+1)] for _ in range(n1+1)]

	for i in range(n2+1):
		dp[0][i]=i 

	for i in range(n1+1):
		dp[i][0]=i 

	for i in range(1,n1+1):
		for j in range(1,n2+1):

			if s1[i-1]==s2[j-1]:
				dp[i][j]=dp[i-1][j-1]
				continue
			dp[i][j]= 1+ min(dp[i-1][j-1] , dp[i-1][j] , dp[i][j-1])

	print("edit distance = " , dp[n1][n2])

	# dis = dp[n1][n2]
	i= n1 
	j= n2
	s=[]
	while i>=1 or j>=1:

		if i<=0:
			s.append(f"_ {s2[j-1]} 1")
			j-=1
		elif j<=0:
			s.append(f"{s1[i-1]} _ 1")
			i-=1
		else:
			l = min(dp[i-1][j-1] , dp[i-1][j] , dp[i][j-1])
			if l ==dp[i][j]:
				s.append(f"{s1[i-1]} {s2[j-1]} 0")
				i-=1
				j-=1
				continue
			if l==dp[i-1][j-1]:
				s.append(f"{s1[i-1]} {s2[j-1]} 1")
				i-=1
				j-=1
			elif l==dp[i-1][j]:
				s.append(f"{s1[i-1]} _ 1")
				i-=1
			else:
				s.append(f"_ {s2[j-1]} 1")	
				j-=1
	s.reverse()
	print("table:")
	for x in s:
		print(x)

def main():
	s1=input()
	s2 = input()
	edit_distance2(s1,s2)
	print()
main()
