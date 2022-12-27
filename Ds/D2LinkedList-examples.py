
'''
1.Print the Middle of a given linked list
you can get the SingleLinked code by importing D1Linkedlist from https://github.com/BHariKrishnaReddy/Python-DSA/blob/main/D1LinkedList.py
'''
#as per the statement we should get the length and divied it to half ,if len is odd one number else even two middle numbers
def lenList(Linkedlist):
  c,temp=0,Linkedlist.head
  while temp:
    temp = temp.next
    c+=1
  return c

def middleElement(Linkedlist):
  l = lenList(Linkedlist)
  
  if l%2==1:
    print(l,"is odd")
    temp,index = Linkedlist.head,0
    while temp:
      if index == int(l/2)+1:
        break
      temp.next
      index+=1
  else:
    print(l,"is Even")
    temp,index = Linkedlist.head,0
    while temp:
      if index == int(l/2) or index == int(l/2)+1:
        print(temp.data)
        if index == int(l/2)+1:
          break
      temp.next
      index+=1
