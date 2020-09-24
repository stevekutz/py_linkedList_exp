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

          length = 1
          # current = point_del = self.head
          current = self.head
          point_del = self.head
          


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

     def sum_total(self):
          current = self.head
          total = 0

          while  current:
               total += current.value
               current = current.next

          return total


     def sum_odd(self):
          current = self.head
          odd_total = 0

          while current:
               if current.value % 2 != 0:
                    odd_total += current.value
               current = current.next 

          return odd_total         

     def sum_even(self):
          current = self.head
          odd_total = 0

          while current:
               if current.value % 2 == 0:
                    odd_total += current.value
               current = current.next 

          return odd_total  


     def sum_palindromes(self):
          
          def is_palindrome(val):
               d = 0; s = 0;  
               temp = val; 
               while (val > 0) :  
               
                    d = val % 10;  # find remainder
                    s = s * 10 + d;   
                    val = val // 10;  
               
                    print(f' d: {d}   s: {s}  val {val} ')
               # If n is equal to its reverse,  
               # it is a palindrome  
               print(f' result: {s == temp} ')
               return s == temp;
          
          current = self.head
          sum_pal = 0

          while current:
               if is_palindrome(current.value):
                    sum_pal += current.value
               current = current.next

          return sum_pal


     def move_last_to_front(self):
          current = self.head
          seclast_pointer = self.head

          # check if empty list OR single node
          # if current or current.next:   # empty list ERROR >> AttributeError: 'NoneType' object has no attribute 'next'
          
          if current  == None:
               print(f' empty list, nothing to move')
               return self.head
          elif current.next == None:
               print(f' only 1 Node, no last Node to move')
               # return self.head     


          while current and current.next:
               seclast_pointer = current
               current = current.next

          print(f' current is {current.value}')    # points to last
          
          if current.next != None:
               print(f' seclast_pointer is {seclast_pointer.value}') # points to second last

          # have seclast_pointer.next point to None
          seclast_pointer.next = None

          # set new head to current(last)
          current.next = self.head

          # set current.next to point to orig head
          self.head = current



     def move_last_to_front2(self):
          current = self.head
          sec_last =self.head

          if current == None:
               print(f' empty linked list')
               return
          if current.next == None:
               print(f' Only 1 node, can move anyting')

          # point current to next node
          current = current.next

          while sec_last and current.next:
               current = current.next  
               sec_last = sec_last.next   

          # should be point last value
          print(f' last value is {current.value}') 
          print(f' sec_last value is {sec_last.value}')   

          # set sec_last to point to None
          sec_last.next = None

          # set last to point to rest of list from head
          current.next = self.head 

          # set head to current(last 
          self.head = current








     def move_first_to_end(self):
          current = self.head
          first_pointer = self.head

          # verify if empty list
          if current == None:
               print(f' empty list')
               return self.head
          elif current.next == None:
               print(f' list has only 1 node, nothing to move') 
               return self.head  
  
          # find end
          while current.next:
               current = current.next
          # current will now point to last     

          # point original head to the next node
          # self.head = first_pointer.next
          self.head = self.head.next

          # set last node to point to first_pointer
          current.next = first_pointer

          # set first node to point to None since it is now last
          first_pointer.next = None

          

     def move_first_to_end2(self):
          first = self.head
          current = self. head


          if current == None:
               print(f' No nodes, empty list')
               return self.head
          elif current.next == None:
               print(f' Only 1 node in list, nothing to move')
               return self.head

          while current.next:
               current = current.next     

          print(f' current should now be last node {current.value}')

          # MUST  adjust head pointer first
          # set head to point to next node
          self.head = self.head.next


          #############   order of these steps does not matter
          # set first node to point to None
          first.next = None

          # set last pointer to point to first node
          current.next = first

     def sort_asc(self):
          current = self.head
          index = None

          if current == None:
               return
          else:
               while current:
                    index = current.next 

                    while index:
                         if current.value > index.value:
                              temp = current.value
                              current.value = index.value
                              index.value = temp

                         index = index.next 

                    current = current.next          






##########################################################################
#              Outside of LinkedList class  - goes inside Solution class
##########################################################################


def merge_sorted_rec(l_1, l_2):
     # l_1 = l_1.head
     # l_2 = l_2.head
     
     # check if l1 empty
     if l_1 == None:
          return l_2
     # check if l2 empty
     if l_2 == None:
          return l_1

     current = None

     if l_1.value <= l_2.value:  
          current = l_1

          current.next = merge_sorted_rec(l_1.next, l_2)

     elif l_1.value > l_2.value:
          current = l_2

          current.next = merge_sorted_rec(l_1, l_2.next)    

     return current


def merge_sorted(l_1, l_2):
     # create head to return solution
     merged = Node()
     temp_tail = merged
     
     while True:
          # check if l1 empty
          if l_1 == None:
               temp_tail.next = l_2
               break

          # check if l2 empty
          if l_2 == None:
               temp_tail.next = l_1
               break

          # Compare values, smallest is appended to tail head is adjusted
          if l_1.value <= l_2.value:
               temp_tail.next = l_1
               l_1 = l_1.next 
          elif l_1.value > l_2.value:
               temp_tail.next = l_2
               l_2 = l_2.next

          # increment tail
          temp_tail = temp_tail.next     

     # return point to new merged list
     return merged.next


def sort_asc_2(linked_list):
     current = linked_list
     index = None
     sol = current

     if current == None:
          return
     else:
          while current:
               index = current.next 

               while index:
                    if current.value > index.value:
                         temp = current.value
                         current.value = index.value
                         index.value = temp

                    index = index.next 
               sol = current
               current = current.next 

     return linked_list


# def sort_asc_3(linked_list):
#      # if not head or not head.next: 
#      sol = Node()
#      linked_list = sol

#      if linked_list == None:
#           return
     
#      head = linked_list

#      def getSize(head):
#           # Simply count the length of linked list
#           counter = 0
#           while head:
#                counter +=1
#                head = head.next
#           return counter
     
#      def split(head, size):
#           # given the head & size, return the the start node of next chunk
#           for i in range(size-1): 
#                if not head: 
#                     break 
#                     head = head.next

#           if not head: return None
#           next_start, head.next = head.next, None  #disconnect
          
#           return next_start
     
#      def merge(l1, l2, dummy_start):
#           # Given dummy_start, merge two lists, and return the tail of merged list
#           curr = dummy_start
#           while l1 and l2:
#                if l1.val <= l2.val:
#                     curr.next, l1 = l1, l1.next
#                else:
#                     curr.next, l2 = l2, l2.next
#                     curr = curr.next
          
#           curr.next = l1 if l1 else l2
#           while curr.next: curr = curr.next  # Find tail
#           # the returned tail should be the "dummy_start" node of next chunk
#           return curr  

#           total_length = getSize(head)
#           dummy = Node()
#           dummy.next = dummy.head
#           start, dummy_start, size = None, None, 1
     
#           while size < total_length:
#                dummy_start = dummy
#                start = dummy.next 
#                while start:
#                     left = start
#                     right = split(left, size) # start from left, cut with size=size
#                     start = split(right, size) # start from right, cut with size=size
#                     dummy_start = merge(left, right, dummy_start)  # returned tail = next dummy_start 
#                size *= 2
#           return dummy.next     
#           # return sol.next


# def merge_unsorted(l_a, l_b):


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


# loop_list.remove_nth_from_end(1)  # first --> second --> third -->
# loop_list.print()


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

# t_list = LinkedList()
# t_list.insert_at_head('first')
# t_list.insert_at_head('dup')
# t_list.insert_at_head('dup')
# t_list.insert_after_value('dup', 'spacer')
# t_list.insert_after_value('spacer', 'more')
# t_list.insert_at_tail('dup')
# t_list.insert_at_tail('dup')
# t_list.insert_at_tail('last')
# t_list.insert_at_tail('dup')
# t_list.print()
# # dup --> spacer --> more --> dup --> first --> dup --> dup --> last --> dup --> 
# t_list.remove_by_value('dup')
# t_list.print()
# # spacer --> more --> first --> last --> 

# num_list = LinkedList()
# num_list.insert_at_tail(10)
# num_list.insert_at_tail(20)
# num_list.insert_at_tail(30)
# num_list.insert_at_tail(40)
# num_list.insert_at_tail(50)
# num_list.print()
# 10 --> 20 --> 30 --> 40 --> 50 --> 

# print(num_list.sum_total())

# m_list = LinkedList()
# # m_list.move_last_to_front()
# m_list.insert_at_head(1)
# m_list.insert_after_value(1, 2)
# m_list.insert_after_value(2, 3)
# m_list.print()

# m_list.move_first_to_end2()
# m_list.print()

# m_list.move_last_to_front()

# # m_list.move_first_to_end()
# m_list.print()

# l_1 = LinkedList()
# l_1.insert_at_head(4)
# l_1.insert_at_head(2)
# l_1.insert_at_head(1)
# l_1.print()    # 1 --> 2 --> 4 --> 

# l_2 = LinkedList()
# l_2.insert_at_head(4)
# l_2.insert_at_head(3)
# l_2.insert_at_head(1)
# l_2.print()   #  1 --> 3 --> 4 --> 

# sol = LinkedList()
# # sol.head = merge_sorted_rec(l_1.head, l_2.head)
# # sol.print() # 1 --> 1 --> 2 --> 3 --> 4 --> 4 -->

# sol.head = merge_sorted(l_1.head, l_2.head)
# sol.print()   # 1 --> 1 --> 2 --> 3 --> 4 --> 4 -->


# print(sol.sum_odd())   # 5
# print(sol.sum_even())  # 10

# l_3 = LinkedList()
# l_3.insert_at_head(2)
# l_3.insert_at_head(5)
# l_3.insert_at_head(7)
# l_3.insert_at_head(0)
# l_3.insert_at_head(5)
# l_3.insert_at_head(6)
# l_3.print()    # 6 --> 5 --> 0 --> 7 --> 5 --> 2 -->
# l_3.sort_asc()
# l_3.print()    # 0 --> 2 --> 5 --> 5 --> 6 --> 7 -->

# l_p = LinkedList()
# l_p.insert_at_head(88)
# l_p.insert_at_head(14)
# l_p.insert_at_head(313)
# l_p.insert_at_head(2)
# print(l_p.sum_palindromes())

# l_3.remove_duplicates()
# l_3.print()

l_a = LinkedList()
l_a.insert_at_head(3)
l_a.insert_at_head(1)
l_a.insert_at_head(5)
l_a.insert_at_head(7)
l_a.insert_at_head(7)
l_a.insert_at_head(79)
l_a.print()  # 79 --> 7 --> 7 --> 5 --> 1 --> 3 --> 

sol = LinkedList()
sol.head = sort_asc_2(l_a.head)
sol.print()  # 1 --> 3 --> 5 --> 7 --> 7 --> 79 -->