

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
	seq=[]

	i=n
	
	while ln>0:

		j=i-1
		while j>=0:
			if lis[j]==ln:
				break
			j-=1
		seq.append(l[j])
		i=j
		ln-=1

	seq.reverse()
	print("The lis is :")
	print(seq)


main()

