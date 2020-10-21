import heapq
class Node:
	def __init__(self, symbol , freq , left , right):
		self.symbol = symbol
		self.freq = freq
		self.left= left
		self.right = right
	# def __str__(self):
	# 	return str(self.freq)

	def __eq__(self, other):
		return self.freq == other.freq

	def __ge__(self, other):
		return self.freq > other.freq
encoding ={}

def preorder(root , s):
	global encoding
	if root.symbol=="":
		s1=s+"0"
		s2=s+"1"
		preorder(root.left , s1)
		preorder(root.right , s2)
	else:
		encoding[root.symbol]=s

def decode(s):
	global encoding
	o=""
	st=""
	dic={}
	for x in encoding.keys():
		dic[encoding[x]]=x
	for x in s:
		st=st+x
		if dic.get(st)!=None:
			o+=dic[st]
			st=""
	print(o)
	return o

def encode(s):
	global encoding
	count={}
	for x in s:
		if count.get(x)==None:
			count[x]=1
		else:
			count[x]+=1

	hp=[]

	for x in count.keys():
		nd= Node(x , count[x] , None , None)
		heapq.heappush(hp , [count[x] , nd])

	while len(hp)>1:
		l1 = heapq.heappop(hp)
		l2 = heapq.heappop(hp)
		nd= Node("", l1[0]+l2[0] , l1[1] , l2[1])
		heapq.heappush(hp , [l1[0]+l2[0] , nd])

	# print(heapq.heappop(hp))
	root = heapq.heappop(hp)[1]
	print(root)
	preorder(root , "")
	for x in encoding.keys():
		print(x , encoding[x])
	encoded_string=""
	for x in s:
		encoded_string+= encoding[x]
	print("encoded string:")
	return encoded_string


def main():
	# s=input()
	file = open("input.txt")

	s = file.read().replace("\n", " ")
	file.close()
	encoded_string= encode(s)
	print(encoded_string)
	print("Number of bits needed to encode the string = " , len(encoded_string))
	print(decode(encoded_string) == s)

main()