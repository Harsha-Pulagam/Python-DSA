def primefactorization(n):
	i=2
	lst = []
	while n>1:
		if n%i==0:
			lst.append(i)
			n=n//i
		else:
			i+=1
	print(lst)
	return lst
#if n:100 O/P : [2, 2, 5, 5]


def divisorsofN(n):
	for i in range(1,n+1):
		if n%i==0:
			print(i)

divisorsofN(7)