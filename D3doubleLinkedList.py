#doulble LinkedList
class Node:
  def __init__(self,value):
    self.value=value
    self.next=None
    self.prev=None
class Dll:
  def __init__(self):
    self.head=None
    self.tail=None

  #insertion
  def dinsertion(self,value,l):
    if self.head==None:
      return "Empty !"
    elif l==0:
      #at startPosition
      newNode =Node(value)
      newNode.next=self.head
      self.head.prev=newNode
      self.head=newNode
    elif l == -1:
      #at endPosition
      newNode = Node(value)
      self.tail.next=newNode
      newNode.prev=self.tail
      self.tail=newNode
    else:
      #in middlePosition
      newNode = Node(value)
      temp,i=self.head,0
      while i<l-1:
        temp=temp.next
        i=+1
      newNode.next = temp.next
      newNode.prev = temp
      newNode.next.prev = newNode
      tempNode.next = newNode

  #deletion
  def ddeletion(self,l):
    if self.head==None:
      return "Empty !"
    elif l==0:
      #at startPosition
      self.head = self.head.next
      self.head.prev = None
    elif l == -1:
      self.tail=self.tail.prev
      self.tail.next= None
    else:
      i,temp=0,self.head
      while i <l-1:
        temp=temp.next
        i+=1
      temp.next=temp.next.next
      temp.next.prev=temp
