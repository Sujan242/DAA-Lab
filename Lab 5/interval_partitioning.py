def main():
	n= int(input())

	intervals=[]

	for i in range(n):
		l=input().split()
		intervals.append([int(l[0]) , int(l[1])])

	intervals.sort()
	resources = []
	finish_time_resources = []

	for i in range(n):
		# print(resources)
		cons = intervals[i]
		if len(resources)==0:
			resources.append([cons])
			finish_time_resources.append(cons[1])
			continue

		j=0
		while j<len(resources):
			if cons[0]>finish_time_resources[j]:
				resources[j].append(cons)
				finish_time_resources[j]=max(finish_time_resources[j] , cons[1])
				break
			j+=1

		if j==len(resources):
			resources.append([cons])
			finish_time_resources.append(cons[1])
	print(len(resources))
	for x in resources:
		print(x)
main()


