#to creat the LL we need two class Node and SingleLinkedList
class Node:
  def __init__(self,data):
    self.data=data
    self.next = None

class SingleLinkedList:
  def __init__(self):
    self.head = None
    self.tail = None
  
  #Insertion to LinkedList
  def insert(self,data,position):
    newNode = Node(data)
    if self.head == None:
      self.head = newNode
      self.tail = newNode
    elif position == 1:
      #if position is 1 it refers that insertion at Head
      newNode.next = self.head
      self.head = newNode
    elif position == -1:
      #if position is -1 it refers that insertion at Tail
      self.tail.next = newNode
      self.tail = newNode
    else:
      #if it in between we need travers thru the list and insert it
      temp,index = self.head,0
      while index < position -1 :
        temp = temp.next
        index+=1
      nextnode=temp.next
      temp.next=newNode
      newNode.next=nextnode

  def delete(self,position):
    if self.head==None:
      return "Empty Linked list"
    elif position == 0:
      self.head= self.head.next
    elif position == -1:
      temp=self.head
      while temp is not None:
        if temp.next==self.tail:
          break
        temp=temp.next
      temp.next=None
      self.tail=temp
    else:
      temp,i=self.head,0
      while i<position-1:
        temp=temp.next
        i+=1
      nextnode = temp.next
      temp.next=n.next

  #Travesal
  def travesel(self):
    if self.head==None:
      return "Empty list"
    else:
      temp=self.head
      while temp is not None:
        print(temp.value)
        temp=temp.next

  #itertion - can use to print the List.
  def _iter_(self):
    temp= self.head
    while temp:
      yield temp
      temp=temp.next

  
sl = SingleLinkedList()
