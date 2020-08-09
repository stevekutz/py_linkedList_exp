class Node:
     def __init__(self, value=None, next=None):
        self.value = value
        self.next = next

class LinkedList:
     def __init__(self):
          self.head = None

     def print(self):
          if self.head is None:
               print("Linked list is empty")
               return
          itr = self.head
          llstr = ''
          while itr:
               llstr += str(itr.value) + ' --> '
               itr = itr.next
          print(llstr)

     def get_length(self):
          count = 0
          itr = self.head
          while itr:
               count+=1
               itr = itr.next

          return count

     def insert_at_tail(self, value):
          if self.head == None:
               self.head = Node(value, None)
               return
          else:
               itr = self.head
               while itr.next: # while it still has a value, not None
                    itr = itr.next
               # at end, next will = None
               itr.next = Node(value, None)     
                    

# def __init__(self, value=None, next=None):
# in Node, next assigned to to self.head
     def insert_at_begining(self, value):
          #    node = Node(value, self.head)
          #    self.head = node

          # this approach also works
          node = Node(value)
          node.next = self.head
          self.head = node

# if __name__ == '__main__':
#      new_list = LinkedList()
#      new_list.insert_at_begining("Orig First")
#      new_list.insert_at_begining("New First")
#      new_list.print()        

new_list = LinkedList()
new_list.insert_at_begining("Orig First")
new_list.insert_at_begining("New First")
new_list.print()  
new_list.insert_at_tail("FirstTail")
new_list.print()    