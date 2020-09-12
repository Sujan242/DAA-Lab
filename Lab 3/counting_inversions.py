l=[2,4,1,3,5]

def sort_and_split(low , mid , high):
	global l
	first = l[low:mid+1]
	second = l[mid+1:high+1]
	# print(first,second)
	n=min(len(first) , len(second))
	i=low
	fp = 0
	sp=0
	ans=0
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
			ans+=  len(first)-fp
			l[i]=second[sp]
			i+=1
			sp+=1
	return ans



def sort_and_count(low , high):
	global l
	if(low<high):
		mid= int((low+high)/2)

		il = sort_and_count(low,mid)
		ir = sort_and_count(mid+1 , high)
		isp = sort_and_split(low , mid, high)
		return il + ir + isp
	return 0

low= 0
high = len(l)-1
# l= [0,4,1,2]
print(sort_and_count(low,high))
# sort_and_split(0 , 1, 3)
print(l)

#perfect amundo