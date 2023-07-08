class Node:
    def __init__(self, info):
        self.info = info
        self.next = None

def insert_item():
    global front, rear
    temp = Node(None)
    item = int(input("\nEnter item to be inserted: "))
    temp.info = item
    temp.next = None
    if front is None:
        front = temp
    else:
        rear.next = temp
    rear = temp

def del_item():
    global front
    if front is None:
        print("\nQueue underflow")
    else:
        temp = front
        print("\nElement after deletion is =", temp.info)
        front = front.next
        temp = None

def display():
    global front
    if front is None:
        print("\nQueue is empty")
    else:
        print("\nContents of the queue are:")
        trav = front
        while trav is not None:
            print(trav.info)
            trav = trav.next

front = None
rear = None

while True:
    print("\n1. Insert item")
    print("2. Delete item")
    print("3. Display")
    print("4. Quit")
    ch = int(input("\nEnter your choice: "))
    if ch == 1:
        insert_item()
    elif ch == 2:
        del_item()
    elif ch == 3:
        display()
    elif ch == 4:
        break
    else:
        print("\nWrong choice. Try again!")

