

def subset( l , i ,s , v , sm):

	if i==len(l):
		if sm==v and len(s)>0:
			print(s)
			return 1
		return 0
	a = subset(l, i+1 , s , v ,sm)
	s1= s+"+" +str(l[i])
	s2 = s+"-"+str(l[i])
	b= subset(l,i+1 , s1 , v , sm+l[i])
	c= subset(l,i+1 , s2 , v , sm-l[i])
	return a+b+c

def main():
	l=input("enter space seperated array:").split()
	n=len(l)
	for i in range(n):
		l[i]=int(l[i])

	v=int(input("target sum"))


	print(subset(l , 0 , "" , v,0))
main()