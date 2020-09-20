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



     def insert_value_at_index(self, index, value):
         # verify if index exists
          if index < 0 or index >= self.get_length():
               print(f' Error: index out of range')
               return

          # basic insert at head
          if index == 0:
               new_node = Node(value) # create new node
               new_node.next = self.head # point to orig head
               self.head = new_node # reset head to new_node
               return 

          count = 0
          itr = self.head

          while itr:
               prev_node = itr
               itr = itr.next
               count += 1
               if count == index:
                    new_node = Node(value)
                    prev_node.next = new_node
                    new_node.next = itr

     def insert_overwrite_value(self, value, new_value):
         # you could use previous methods
         
          # if list is empty
          if self.head == None:
               new_node = Node(value)
               self.head = new_node
               return

          # if list not empty, find value
          current = self.head
          
          while current:
               if current.value == value:
                    current.value = new_value
                    return
               current = current.next          

          print(f'value {value} not found')

     def insert_after_value(self, value, new_value):
          current = self.head  # start 

          while current:
               if current.value == value:
                    # verify if there is next
                    if current.next == None:
                         new_node = Node(new_value)
                         current.next = new_node
                         return 
                    else:
                         node_after_insert = current.next  
                         new_node = Node(new_value) 
                         current.next = new_node
                         current.next.next = node_after_insert
                         return 
               # increment to next node
               current = current.next

          print(f' value {value} not found in linked list')                    

     def insert_before_value(self, value, new_value):
          current = self.head
          count = 0
          value_exists = False
               
          if count == 0 and current.value == value:
               new_node = Node(new_value)
               new_node.next = self.head
               self.head = new_node
               return

          while current.next:
               if current.next.value == value:
                    value_exists = True
                    new_node = Node(new_value)
                    orig_current_next = current.next  # placeholder for pointer to rest of list
                    current.next = new_node
                    new_node.next = orig_current_next
                    break
               current = current.next  

          if not value_exists:
               print(f' value {value} is not in linked list')          


                         
     def remove_by_value(self, value):
          # Removes ALL occurrence of value found
          
          current = self.head
          not_found = True     

          # Case 1: location is head
          if current.value == value:
               self.head = current.next # reset head to next node
               # return 

          # Case 2: location is somewhere in list
          while current.next:
               if current.next.value == value:
                    not_found = False
                    current.next = current.next.next
                    # break
               else:
                    current = current.next


          if not_found:               
               print(f' value {value} is not in linked list ')


     def remove_by_value2(self, value):
          current = self.head
          value_found = False

          # Case 1 node is head
          if current.value == value:
               self.head = current.next # reset head to next node >> None
               # return 

          # Case 2 node is inside list
          prev_node = current
          delete_target = current.next

          while prev_node:
               if delete_target.value == value:
                    value_found = True
                    prev_node.next = delete_target.next
                    break

               prev_node = prev_node.next
               if current.next:
                    current = current.next
                    delete_target = current.next          
               
          if not value_found:
               print(f' value {value} does not exist in linked list')


     def remove_by_index(self, index):
          current = self.head

          if index < 0 or index >= self.get_length():
               print(f' ERROR: index out of range')

          count = 0    
          while current != None:
               # if index is head
               if index == 0:
                    self.head = current.next 
                    return

               # if index is within list
               count += 1
               if index == count:
                    current.next = current.next.next   

               current = current.next     


     def loop_to_value(self, value):
          current = self.head

          # iterate to find value address & last node          
          if value == 'head':
               val_add = current
          else:     
               val_add = None

          # iterate to find adddress of value & point tail to address
          while current.next:
               if current.next.value == value:
                    val_add = current.next

               # iterate to next node
               current = current.next     
               # find location of tail
           
          # current now at tail , set to next pointer to loop value
          current.next = val_add

     def detect_loop(self):
          addr_set = set()  # create empty set to store address

          ll_str = ''

          current = self.head

          while current:
               
               if current in addr_set:
                    ll_str += str(current.value)
                    print(ll_str)
                    print(f' TRUE - loop detected at Node >> {current.value}')
                    return True

               # otherwise add the address to set
               addr_set.add(current)
               ll_str += str(current.value) + ' ==> '
               current = current.next     

          print(ll_str)
          print(f' FALSE - no loops found')
          return False

     def remove_loop(self):
          addr_set = set()

          current = self.head
          addr_set.add(current.value)

          orig_head = self.head
          after_head = orig_head.next

          while current:

               if current.next.value in addr_set:    
                    current.next = None
                    return
               addr_set.add(current.next.value)

               # increment to next node
               current = current.next               

     def reverse(self):
          current = self.head
          prev_add = None

          while current:
               next_add = current.next
               current.next = prev_add
               prev_add = current
               current = next_add

          self.head = prev_add

     def remove_nth_from_end(self, n):

          # NOT DONE

          length = 1
          current = point_del = self.head
          


          while current.next:
               length += 1
               current = current.next   

               if length > n + 1:
                    point_del = point_del.next  
          # when we exit loop, point_del should be at node we want to remove

          # nth is beyond length, return orig linked list
          if n > length:
               return self.head

          # nth from end is first node in link list
          if length == n:
               self.head = self.head.next # simply reset head to next element
               return 

          # nth from end is at point_del.next, set pointer around it
          else:
               point_del.next = point_del.next.next  
               return self.head

     def remove_duplicates(self):
          current = self.head
          dup_pointer = self.head    # pointer to loop through rest of list

          # start pointers at same node, increment dup_pointer until end
          #  --   if dup found, set pointer around it   
          # THEN, set both pointers to next element and repeat  

          while current:
               while dup_pointer.next:
                    if current.value == dup_pointer.next.value:
                         dup_pointer.next = dup_pointer.next.next  
                    else:
                         dup_pointer = dup_pointer.next
               # increment BOTH pointers and continue
               current = dup_pointer = current.next
               
               # NO !!!   this makes dup_pointer => current.next.next
               # current = current.next  
               # dup_pointer = current.next     ##            


# if __name__ == '__main__':
#      new_list = LinkedList()
#      new_list.insert_at_head("Orig First")
#      new_list.insert_at_head("New First")
#      new_list.print()        

# new_list = LinkedList()
# new_list.insert_at_head(1)
# new_list.insert_at_head("New First")
# new_list.print()  # New First --> 1 --> 
# new_list.insert_at_tail("FirstTail")
# new_list.insert_at_tail("Newer Tail")
# new_list.print()  # New First --> 1 --> FirstTail --> Newer Tail --> 

# my_list = list(range(3))
# print(f' {my_list}')  # [0, 1, 2]
# new_list.insert_list_at_tail(my_list)
# new_list.print()   # New First --> 1 --> FirstTail --> Newer Tail --> 0 --> 1 --> 2 -->

# new_list.remove_at_index(1)
# new_list.print()   # New First --> FirstTail --> Newer Tail --> 0 --> 1 --> 2 --> 

# new_list.remove_at_index_2(1)
# new_list.print()  # New First --> Newer Tail --> 0 --> 1 --> 2 --> 

# new_list.remove_at_index_2(0)
# new_list.print() # Newer Tail --> 0 --> 1 --> 2 -->

# new_list.remove_at_index(0)
# new_list.print() # 0 --> 1 --> 2 -->

# new_list.remove_at_index(100) # Error: index out of range
# new_list.remove_at_index(-10) # Error: index out of range

# new_list.insert_value_at_index(1, "One")
# new_list.print()  # 0 --> One --> 1 --> 2 -->
# new_list.insert_value_at_index(0, "New Firsty")
# new_list.print()  # New Firsty --> 0 --> One --> 1 --> 2 -->

# new_list.insert_overwrite_value("New Firsty", "NEWER Firsty")
# new_list.print()  # NEWER Firsty --> 0 --> One --> 1 --> 2 -->
# new_list.insert_overwrite_value("One", "New ONE")
# new_list.print() # NEWER Firsty --> 0 --> New ONE --> 1 --> 2 -->

# new_list.insert_after_value("New ONE", "added AFTER")
# new_list.print() # NEWER Firsty --> 0 --> New ONE --> added AFTER --> 1 --> 2 -->

# new_list.insert_after_value("Newer", "added AFTER") 
# # value Newer not found in linked list
# new_list.insert_after_value("NEWER Firsty", "After NEWER Firsty")
# new_list.print()  # NEWER Firsty --> After NEWER Firsty --> 0 --> New ONE --> added AFTER --> 1 --> 2 --> 
# # # new empty list
# new_list2 = LinkedList()
# new_list2.insert_after_value("first", "new_first")
# # value first not found in linked list

# new_list.remove_by_value("After NEWER Firsty")
# new_list.print() # NEWER Firsty --> 0 --> New ONE --> added AFTER --> 1 --> 2 --> 
# new_list.remove_by_value("NEWER Firsty")
# new_list.print() # 0 --> New ONE --> added AFTER --> 1 --> 2 -->

# # only 1 node
# new_list2.insert_at_head("Loner")
# new_list2.print() # Loner -->  
# new_list2.remove_by_value("Loner")
# new_list2.print() # Linked list is empty

# new_list.remove_by_value("added AFTER")
# new_list.print() # 0 --> New ONE --> 1 --> 2 -->

# new_list.remove_by_index(1)
# new_list.print() # 0 --> 1 --> 2 -->

# # new_list.remove_by_index(0)
# # new_list.print() # 1 --> 2 --> 

# new_list.insert_before_value( 1, "Before")
# new_list.print() # 0 --> Before --> 1 --> 2 -->

# new_list.insert_before_value("Before", "pre-Before")
# new_list.print() # 0 --> pre-Before --> Before --> 1 --> 2 --> 

# new_list.insert_before_value("Not here", "not inserted") # value Not here is not in linked list


# loop_list = LinkedList()
# loop_list.insert_at_head('first')
# loop_list.insert_after_value('first', 'dup')

# loop_list.insert_after_value('first', 'second')
# loop_list.insert_after_value('second', 'third')
# loop_list.insert_after_value('third', 'fourth')
# loop_list.print()
# # loop_list.detect_loop()
# # # first ==> second ==> third ==> fourth ==> 
# # #  FALSE - no loops found

# # loop_list.loop_to_value('second')
# # loop_list.detect_loop() 
# # # first ==> second ==> third ==> fourth ==> second
# # #  TRUE - loop detected at Node >> second

# # loop_list.remove_loop()
# # loop_list.detect_loop() 
# # # first ==> second ==> third ==> fourth ==> 
# # #  FALSE - no loops found

# # loop_list.print()  # head --> first --> second --> third --> 

# # loop_list.reverse()
# # loop_list.print()   # fourth --> third --> second --> first -->


# # print(f'\n')
# # loop_list.reverse()
# # loop_list.print()  # first --> second --> third --> fourth --> ->


# # loop_list.remove_nth_from_end(1)  # first --> second --> third -->
# # loop_list.print()


# # loop_list.remove_nth_from_end(2)  # first --> second --> fourth --> 
# # loop_list.print()

# # loop_list.remove_nth_from_end(3)  # 
# # loop_list.print()    # first --> third --> fourth --> 

# # loop_list.print()
# # loop_list.remove_nth_from_end(4)  
# # loop_list.print()    # second --> third --> fourth -->

# # loop_list.remove_by_value2('first')
# # loop_list.print()  # second --> third --> fourth --> 

# # loop_list.remove_by_value('fourth')
# # loop_list.print()

# loop_list.insert_before_value('first', 'dup')
# loop_list.insert_before_value('third', 'dup')
# loop_list.insert_before_value('third', 'dup')
# loop_list.insert_before_value('fourth', 'dup')
# loop_list.insert_after_value('fourth', 'dup')
# loop_list.print()
# # # # first --> second --> dup --> dup --> third --> dup --> fourth --> dup --> 
# # # loop_list.remove_duplicates()
# # # loop_list.print()
# loop_list.remove_by_value('dup')
# loop_list.print()
# # loop_list.remove_by_value('dup')
# # loop_list.print()

t_list = LinkedList()
t_list.insert_at_head('first')
t_list.insert_at_head('dup')
t_list.insert_at_head('dup')
t_list.insert_after_value('dup', 'spacer')
t_list.insert_after_value('spacer', 'more')
t_list.insert_at_tail('dup')
t_list.insert_at_tail('dup')
t_list.insert_at_tail('last')
t_list.print()
t_list.remove_by_value('dup')
t_list.print()
