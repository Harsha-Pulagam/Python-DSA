def reverseList(A, start, end):
	while start < end:
		A[start], A[end] = A[end], A[start] # it is like a swapping to variables without using extra variable
		start += 1
		end -= 1

A = [1, 2, 3, 4, 5, 6]
reverseList(A, 0, 5)
print("Reversed list is",A)

