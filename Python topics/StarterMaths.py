#sum of natural numbers
def sumofN(n):
	return n*(n+1)/2

def CountDigits(n):
	index = 0
	while n>0:
		n=n//10
		index+=1
	return index

def Palindrome(n):
	revNum = 0
	temp = n
	while temp != 0:
		revNum = temp%10
		revNum = revNum *10 + revNum
		temp = temp//10
	return temp == revNum

def factorial(n):
	if n==0:
		return 1
	else:
		return n*factorial(n-1)

def factorialLoop(n):
	if n==0:
		return 1
	multiplicative = 1
	for i in range(2,n+1):
		multiplicative = multiplicative *i
	return multiplicative

def CountTrailingZerosInFactorical(n):
	fact = 1
	for i in range(2,n+1):
		fact =fact * i
	CountZeros = 0
	while (fact%10 == 0):
		CountZeros +=1
		fact=fact//10
	return CountZeros


'''
alternative or best solution 

Trailing zeros = n/5 + n/25 + n/125 +.........
i.e  if we can find the combinatoin of 2*5 which results trailing ZERO but in genreal the occurance of 5 is less compared to 2 so we will find for 5

keep an eye on 25,50,75.... where we get more 5's
'''

def TrailingZerosInFactorical(n):
	i=5
	count = 0
	while i<=n:
		count = count + n//i
		i = i * 5
	return count


# GCD
def gdcmethod1(a,b):
	'''
	This is euclidean distance approach
	:param a:
	:param b:
	:return:
	'''
	while a!=b:
		if a>b:
			a= a-b
		else:
			b=b-a
	return a


def gdcmethod2(a,b):
	'''
	This is OPTIMIZED euclidean distance approach
	:param a:
	:param b:
	:return:
	'''
	if b==0:
		return a
	return gdcmethod2(b,a%b)




