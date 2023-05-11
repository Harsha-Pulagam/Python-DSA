#Below function is example of head recursion
#the numbers are printed in ascending order because the print executes during returning time
#Time Complexity O(n)
#Space Complexity O(n)
def recursion_1toN(n):
    if n>0:
        recursion_1toN(n-1)
        print(n)#executes druing retruning

recursion_1toN(10)

#Below funtion is example of Tail Recursion
#The Numbers are printed in descending order because the print executes during calling
def recursion_Nto1(n):
    if n>0:
        print(n)#executes druing calling
        recursion_Nto1(n-1)

recursion_Nto1(10)              