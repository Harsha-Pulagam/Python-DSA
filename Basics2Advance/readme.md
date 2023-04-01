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
* Given a positive integer value N. The task is to find how many numbers less than or equal to N have numbers of divisors exactly equal to 3.
  * Example 1:
  In:
  N = 6
  Out: 1
  Explanation: The only number less than 6 with 
  3 divisors is 4.
  
  * Example 2:
In:
N = 10
Out: 2
Explanation: 4 and 9 have 3 divisors.
```commandline
import math
def exactly3Divisors(self,N):
       root_N = math.floor(pow(N, 0.5)) + 1
       isPrime = [True] * root_N
       
       for i in range(2, root_N):
           for j in range(i*i, root_N, i):
               isPrime[j] = False
               
       ans = 0    
       for i in range(2, root_N):
           if isPrime[i] == True:
               ans += 1
               
       return ans
```
---
### Lists in Python
1. Dynamic and allows items of all types
2. Internal working
   1. Advantages
      1. Random access
      2. Cache friendly
   2. Disadvantages
      1. Slow during insertion or deletion
      2. Search is slow (sorted)
```commandline
# few built-in lib's
l = [] or l = [1,2,3,6,"t",0]
l.append()
l.insert(index,val)
l.index(val)           #will retrun the first occurence of the value in list
l.count(val)           #retunrs the no.of occurnces
l.remove(val)
l.pop(index)
del l[index]
min(l)           max(l)            sum(l)           l.reverse()           l.sort()
```
#### Know Recursion or about _Tail Recursion_ ?
* Recursion - calling directly or indirectly
  * There should be one change in parameter so that call approaches towards _BASE case_.
  * used in Dynamic programming, Back tracking , Divide and conquer .....
* Tail Recursion - If the function doest not do anything after last recursive call.
  *  _NO TAIL CALL ELIMINATION_  in python
```commandline
Few Problems to get good touch on LIST / RECURSION
1. Reverse a list 
2. Remove duplicate in list
3. Left Rotate or Couterclock wise by n
4. Write Pandlidrome or Sum of Digits in Number ?
```

#### Binary Search code

```
def CommonBS(l, x):
    low = 0
    high = len(l) - 1
    while low <= high:
        mid = (low + high) // 2
        if l[mid] > x:
            high = mid - 1
        elif l[mid] < x:
            low = mid + 1

        {code this part chnages and tells which side to move}  
        
    return -1
```
code this part chnages and tells which side to move
```
#in case of first
else:            
  if mid == 0 or l[mid - 1] != l[mid]:
    return mid
  else:
    high = mid - 1

#in case of last
else:
  if mid == len(l) - 1 or l[mid] != l[mid + 1]:
      return mid
    else:
      low = mid + 1
```