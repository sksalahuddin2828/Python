class Node:
   def __init__(self, dataval=None):
      self.dataval = dataval
      self.nextval = None

class SLinkedList:
   def __init__(self):
      self.headval = None

   def listprint(self):
      printval = self.headval
      while printval is not None:
         print("Value:", printval.dataval)
         printval = printval.nextval

# Create an instance of the SLinkedList class
list = SLinkedList()

# Create nodes with different values
list.headval = Node("Monday")
e2 = Node("Tuesday")
e3 = Node("Wednesday")

# Link the nodes together
list.headval.nextval = e2
e2.nextval = e3

# Print the values in the linked list
list.listprint()


# Answer: Value: Monday
#         Value: Tuesday
#         Value: Wednesday
