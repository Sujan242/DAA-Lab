import sys

l=[]
b=0
def merge(low , mid , high):
	global l
	global b
	first = l[low:mid+1]
	second = l[mid+1:high+1]
	i=low
	fp = 0 #first pointer
	sp=0 #second pointer
	while fp<len(first) or sp<len(second):
		if fp>=len(first):
			l[i]=second[sp]
			i+=1
			sp+=1
			continue
		if sp>=len(second):
			l[i]=first[fp]
			i+=1
			fp+=1
			continue

		if first[fp]<=second[sp]:
			l[i]=first[fp]
			i+=1
			fp+=1
		
		else:
			l[i]=second[sp]
			i+=1
			sp+=1

	# return ans

def sort_and_count(low , high):
	global l
	global b
	# print(l)
	if(low<high):
		mid= int((low+high)/2)

		il = sort_and_count(low,mid)  #inversions in left
		ir = sort_and_count(mid+1 , high)  #inversions in right
		isp = 0  # inversion that cross over
		j= mid+1
		for i in range(low , mid+1):    # incrementing j at each iteration. So this won't be O(n^2).Rather O(n+n)
			while j<=high and l[i]>l[j]*b:
				j+=1
			isp+= j- (mid+1)
		# print(isp)
		merge(low , mid, high)  #O(n)
		return il + ir + isp

	return 0
def countBinversions():
	''' Add your code here. Define appropriate parameters and call this function from main. '''
	global l
	global b
	l[-1]= l[-1][:-1]
	# print( l)
	for i in range(len(l)):
		l[i]=int(l[i])
	print(l,b)

	print(sort_and_count(0 , len(l)-1))

	pass

def main():
	global b
	global l
	
	if len(sys.argv) != 2:
		return

	fname = sys.argv[1] 
	file=open(fname,'r')
	
	numTestcases = int(file.readline())

	for i in range(numTestcases):
		line= file.readline() # Read in the numbers in the sequence
		l=[]
		# Print the numbers in the sequence one by one.
		for w in line.split(' '):
			l.append(w)
		    # print(w, end=' ')

		b = file.readline() # The number b
		# print(b) 
		b=int(b)
		if(len(l)==0):
			print(0)
			continue

		countBinversions()
		# print(l)


	file.close()

if __name__ == '__main__':
	main()