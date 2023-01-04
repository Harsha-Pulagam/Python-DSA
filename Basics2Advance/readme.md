**Asymptotic analysis** is a method of analyzing the behavior of a function as the input size becomes infinite. It allows us to understand how the function scales with respect to the input size, without having to analyze the function for every possible input.

**Order of growth** is a measure of how quickly a function grows as the input size increases. It is often expressed using Big O notation, which provides an upper bound on the growth rate of a function.

**Big O notation** is a mathematical notation that represents the upper bound on the growth rate of a function. It is often used to express the asymptotic behavior of a function, and is denoted as O(f(n)), where n is the input size and f(n) is a function that represents the growth rate. For example, O(n) represents a function that grows linearly with respect to the input size, while O(n^2) represents a function that grows at a rate of n^2.

**Omega notation** is similar to Big O notation, but it represents the lower bound on the growth rate of a function. It is denoted as Ω(f(n)), and is used to express the asymptotic behavior of a function from below.

**Theta notation** is a combination of Big O and Omega notation, and represents the tight bound on the growth rate of a function. It is denoted as Θ(f(n)), and is used to express the asymptotic behavior of a function when both the upper and lower bounds are known.

**Auxiliary space** is the extra space used by an algorithm beyond the input size. It is often used to store temporary variables or data structures

*In summary, asymptotic analysis is a method of **analyzing the behavior of a function as the input size becomes infinite**, and is often expressed using Big O, Omega, or Theta notation, which represent upper, lower, and tight bounds on the growth rate of the function, respectively.*

---
Handy NoteBook
* While dealing with divisors
  * Divisors always appear in pairs like.. 
    * 10 -> (1,10),(2,5)
    * 30 -> (1,30), (2,15), (3,10), (5,6)
  * One of the divisor in every pair is smaller or equal to n^1/2.
    * let say `x*y = n and x<= y, i.e x*x <= n , x = n^1/2`
* Dealing with primes ?
```commandline
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
		i+=6                          # value of i->5,11,17,23.....
	return True
```
* No.of primes till n ?
```commandline
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
```
* Efficient way to do factorial of number and get the digit count
```
def digitsInFactorial(self,N):
        log_factorial = 0
        for i in range(1, N+1):
            log_factorial += math.log10(i)
        return math.floor(log_factorial) + 1
```
* For Better understanding of above logic
<img width="992" alt="Screenshot 2022-12-28 at 21 06 15" src="https://user-images.githubusercontent.com/45511185/209836123-c809f7e0-4e97-473a-a146-d4292e2d1e20.png">
* Modulus `(a*b)%m == 1`
* 

