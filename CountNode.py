class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class CountNode:
    def __init__(self):
        self.head = None

    def append(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        temp = self.head
        while temp.next!=None:
            temp = temp.next
        temp.next = new_node

    def display(self):
        count=0
        temp = self.head
        while temp:
            count+=1
            print(temp.data,end='->')
            temp = temp.next
        print("None")
        print(count)

l1=CountNode()
l1.append(1)
l1.append(2)
l1.append(3)
l1.display()

