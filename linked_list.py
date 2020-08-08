class Node:
     def __init__(self, value = None):
          self.value = value
          self.next = None
          self.last = None

     def __str__(self):
          return str(self.value)

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
               current = current.next # goto next node
          return total     

     def print_list(self):
          elements = []
          current_node = self.head
          # iterate until last node found
          while current_node.next != None:
               current_node = current_node.next
               item = str(current_node.value) + "-->"
               #elements.append(current_node.value)
               elements.append(item)
          print(f' elements: {elements}')


     def get(self, index):
          if index >= self.length() or index < 0:
               print(f' index out of range !!') 
               return None
          cur_index = 0
          current_node = self.head  # start at  Head placeholder
          while True:
               current_node = current_node.next  # increment
               if cur_index == index:
                    return current_node.value
               cur_index += 1  # increment if not found


     def delete(self, index):
          if index >= self.length() or index < 0:
               print(f' index out of range !!') 
               return None
          cur_index = 0
          current_node = self.head
          while True:
               last_active_node = current_node   
               current_node = current_node.next
               if cur_index == index:
                    # previosu active points AROUND "deleted" node to next node that exists
                    last_active_node.next = current_node.next 
                    return
               cur_index += 1     




# create instance
new_list = Linked_List()

new_list.append("First")
new_list.append(2)
new_list.append(3)
new_list.print_list()   # ['First-->', '2-->', '3-->']
print(new_list.get(2))   # 3

new_list.delete(1)  # deletes value '2' at index 1
new_list.print_list() # ['First-->', '3-->']

print(new_list.length())