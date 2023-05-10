## **Recursion**
    A function which calls itself. generally with a conditional statement so that it doesn't fall in an infinite loop
### **Types of Recursion**
* Tail Recursion
* Head Recursion
* Tree Recursion
* Indirect Recursion
* Nested Recursion

**Tail Recursion** if recursive function call is the last line of the function its called as Tail Recursion.
```commandline
    def fun_returning(x):
    if x>0:
        fun_returning(x-1)
        print(x)
```

```commandline
OUTPUT:123
```