

def fun(x,i, dic, s):
	# if i>=len(x)
	if i>=len(x):
		return
	if dic.get(x[i:])!=None:
		print (s+x[i:]+" ")
		# return

	st=""

	for j in range(i,len(x)):
		st=st+ x[j]
		if dic.get(st)!=None:
			fun(x,j+1 , dic , s+st+" ")

def main():
	l=['a', 'an', 'at', 'the', 'are', 'man', 'hunt', 'go', 'ant', 'he', 'mango']

	s= "anthehuntmango"

	dic={}
	for x in l:
		dic[x]=True

	fun(s,0, dic, "")

main()