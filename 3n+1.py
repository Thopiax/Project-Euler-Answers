#!/usr/bin/env

while True:
	i,j = input("i,j: ")
	print(i,j)
	n_range = range(i,j+1,1)

	n_list=[]

	for x in n_range:
		n=1
		while x>1:
			n=n+1
			if x%2==0:
				x = (x/2)
			elif x%2 ==1:
				x = (3*x)+1

		n_list.append(n)

	n_list.sort(None,None,True)
	maximum=n_list[0]

	print(i,j,maximum)
