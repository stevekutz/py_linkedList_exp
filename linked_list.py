class Node:
     def __init__(self, value = None):
          self.value = value
          self.next = None
          self.last = None

class Linked_List:
     def __init__(self):    # head nevers holds data, not indexable, user cannot acccess
          self.head = Node() # used as placeholder to point to 1st element in LL, NOT a DATA NODE!!!

     def __str__(self):
          return str(self.value)

     def __len__(self):
          return len

     def append(self, value):
          new_node = Node(value)
          current = self.head
          # we can now iterate until we find last node where current.next = None
          while current.next != None:
               current = current.next
          # Add new node to end
          current.next = new_node

     def length(self):
          current = self.head
          total = 0
          # iterate through list until last Node located
          while current.next != None:
               total += 1
               current = current.next
          return total     
