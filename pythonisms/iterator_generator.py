# Use of iterator and generator in LinkedList implementation 
class Node:
  def __init__(self,value):
    self.value = value
    self.next = None

  def __eq__(self,other):
    """return True or False if the node value is equal other value
    """
    return self.value == other.value


class LinkedList:
  def __init__(self):
    self.head = None
   
    def __next__(self):
      """
      a function to get the next element in iterable object
      """
      if not self.head:
        node = self.head.value
        self.head = self.head.next(node)
        return node

  def append(self, value):

        new_node = Node(value)
        current = self.head
        if not self.head:
            self.head = new_node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = new_node


  def __str__(self):
    """returns a sting represring the linked list"""
    result = ""
    current = self.head
    while current:
      result+= f" >>{current.value}"
      current=current.next
 
    return result

  def __iter__(self):
    current = self.head
    while current:
      yield current.value
      current = current.next

  def __eq__(self,other):
    """
    return True or False if the node from list2 is equal node from list1 
    because i don't know which node from list 1 i will try to do it for all list 
    """
    current1=self.head 
    current2=other.head 
    flag = True

    while  current1 and current2 :
      if not(current1.value  == current2.value):
        flag = False
        break  
      current1 = current1.next
      current2 = current2.next
    return flag
    

  def __getitem__(self,index):
    """get item should return a value depending on the index we give"""

    for i,val in enumerate(self):
      if i == index:
        return val
    raise IndexError('index is out of range')

  def __len__(self):
    for index,value in enumerate(self, start=1):
      current = index
    return current


    
    


# Add ability for list comprehension using iterators
# if __name__ == '__main__':
#   ll = LinkedList()
#   ll.append(7)
#   ll.append(5)
#   ll.append(9)
#   ll.append(10)
  
# lst = [i for i in ll ]
# print(lst)


    


     





    
        


       

  


