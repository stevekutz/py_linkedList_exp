class Node:
     def __init__(self, value=None, next=None):
        self.value = value
        self.next = next

class LinkedList:
     def __init__(self):
          self.head = None  # just a pointer to first element in list

     def print(self):
          if self.head is None:
               print("Linked list is empty")
               return
          itr = self.head  # init to head
          llstr = ''
          while itr:
               llstr += str(itr.value) + ' --> '
               itr = itr.next
          print(llstr)

     def get_length(self):
          count = 0
          itr = self.head # init to first mem address of ll
          while itr: # while a pointer exists
               count +=1
               itr = itr.next # point to next node

          return count

     def insert_at_tail(self, value):
          #  check if list is empty
          if self.head == None:
               # another way
               new_node = Node(value)
               new_node.next = None
               self.head = new_node # reset head to new_node
               
               # self.head = Node(value, None)
               return

          # if list NOT empty, iterate through until end     
          else:
               itr = self.head
               while itr.next: # while it still has a value, not None
                    itr = itr.next
               # at end, next will = None
               itr.next = Node(value, None)     
                    
                                                     ### vvvvv ###  
     # from constructor >>  def __init__(self, value=None, next=None):
     # def insert_at_head(self, value):
          #    new_node = Node(value, self.head)  # in Node, next assigned to to self.head 
          #    self.head = new_node   # reset head to new node

     def insert_at_head(self, value):
          # this approach also works
          new_node = Node(value) # create new node
          new_node.next = self.head # .next points to orig head & list of value, pointers
          self.head = new_node  # reset head to new node

          # call using .insert_Node_at_head(Node("VALUE))               
     def insert_Node_at_head(self, new_node):
         new_node.next = self.head  # .next points to orig head
         new_node = self.head  # reset head to new_node
      

     def insert_list_at_tail(self, list_vals):
          for item in list_vals:
               self.insert_at_tail(item)

     def remove_at_index(self, index):
          # verify if index exists
          if index < 0 or index >= self.get_length():
               print(f' Error: index out of range')
               return
          
          # if index is head
          if index == 0:
               self.head = self.head.next # simply reset head to next element
               return

          # locate node BEFORE the index to be deleted
          itr = self.head
          count = 0

          while itr:
               prev_node = itr
               if count == index - 1:
                    # point .next to node after one to be deleted
                    itr.next = itr.next.next
                    break
               # otherwise, look to next node & INCREMENT count
               itr = itr.next
               count += 1

     def remove_at_index_2(self, index):
          # verify if index exists
          if index < 0 or index >= self.get_length():
               print(f' Error: index out of range')
               return
          
          # if index is head
          if index == 0:
               self.head = self.head.next # simply reset head to next element
               return          

          count = 0
          itr = self.head

          while itr:
               prev_node = itr
               itr = itr.next
               count += 1
               if count == index:
                    prev_node.next = prev_node.next.next
                    return

# if __name__ == '__main__':
#      new_list = LinkedList()
#      new_list.insert_at_head("Orig First")
#      new_list.insert_at_head("New First")
#      new_list.print()        

new_list = LinkedList()
new_list.insert_at_head(1)
new_list.insert_at_head("New First")
new_list.print()  # New First --> 1 --> 
new_list.insert_at_tail("FirstTail")
new_list.insert_at_tail("Newer Tail")
new_list.print()  # New First --> 1 --> FirstTail --> Newer Tail --> 

my_list = list(range(3))
print(f' {my_list}')  # [0, 1, 2]
new_list.insert_list_at_tail(my_list)
new_list.print()   # New First --> 1 --> FirstTail --> Newer Tail --> 0 --> 1 --> 2 -->

new_list.remove_at_index(1)
new_list.print()   # New First --> FirstTail --> Newer Tail --> 0 --> 1 --> 2 --> 

new_list.remove_at_index_2(1)
new_list.print()  # New First --> Newer Tail --> 0 --> 1 --> 2 --> 