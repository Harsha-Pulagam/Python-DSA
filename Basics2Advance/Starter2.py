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

# best for prime
def isPrime(n):
	if n==1:
		return False
	if n==2 or n==3:
		return True
	if n%2==0 or n%3==0:
		return False
	i=5
	while (i*i) <=n:
		if n%i ==0  or n%(i+2)==0:
			return False
		i+=6
	return True

def SieveOfEratosthenes(num):
	prime = [True for i in range(num+1)]
	p = 2
	while (p * p <= num):
		if (prime[p] == True):
			for i in range(p * p, num+1, p):
				prime[i] = False
		p += 1

	for p in range(2, num+1):
		if prime[p]:
			print(p)

SieveOfEratosthenes(25)

def GCD(self,a,b):
	if a>b:
		return self.GCD(a-b,b)
        elif a<b:
                return self.GCD(a,b-a)
        else:
		return a