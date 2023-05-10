## **Recursion**
    A function which calls itself. generally with a conditional statement so that it doesn't fall in an infinite loop
### **Types of Recursion**
* Tail Recursion
* Head Recursion
* Tree Recursion
* Indirect Recursion
* Nested Recursion

**Tail Recursion** if recursive function call is the last line of the function it's called as Tail Recursion.
```commandline
def tail_recursion(x):
    if x>0:
        tail_recursion(x-1)
        print(x)
```

```commandline
OUTPUT:123
```
**Head Recursion** if recursive call is the first line of the function it's called as Head Recurion.
```python
def fun_calling(x):
    if x>0:
        print(x)
        fun_calling(x-1)
```
```commandline
OUTPUT:321
```
**Tree Recursion**if recursive call is morethan one time it's called as Tree Recursion
```python
class Recursion:
    def __init__(self):
        self.i = 0
    
    def tree_recursion(self, x):
        self.i +=1
        if x>0:
            print(x)
            self.tree_recursion(x-1)
            self.tree_recursion(x-1)

#object creation
tree =Recursion()
#calling tree recursion
tree.tree_recursion(3)
```
```commandline
OUTPUT:3211211
```
