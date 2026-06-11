class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class EvenNode:
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
        s=0
        temp = self.head
        
        while temp:
            if temp.data%2==0:
                s+=temp.data
            print(temp.data,end='->')
            temp = temp.next
        print("None")
        print(s)

l1=EvenNode()
l1.append(1)
l1.append(2)
l1.append(3)
l1.append(4)
l1.display()

