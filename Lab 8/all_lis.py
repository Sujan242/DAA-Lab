def main():
	l=input().split()
	n=len(l)
	for i in range(n):
		l[i]=int(l[i])

	lis=[1 for _ in range(n)]
	ln = 0
	for i in range(n):

		for j in range(i):

			if l[i]>l[j]:
				lis[i]=max(lis[i] , 1+ lis[j])
		ln=max(ln, lis[i])

	print("length of lis = ", ln)

	dic={}

	dic = {}   # maps from a number to a list of lists
	dic[0]=[[]]

	for i in range(n):

		ll = dic[lis[i]-1]

		
		if dic.get(lis[i])==None:
			dic[lis[i]]=[]

		# print(ll)
		for x in ll:

			if len(x)==0 or l[i]>x[-1]:
				ls=x.copy()
				ls.append(l[i])
				dic[lis[i]].append(ls)
		# break

	# print(dic)
	for x in dic[ln]:
		print(x)

main()

