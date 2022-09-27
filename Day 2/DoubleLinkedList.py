class Node:
    data = None
    next = None
    prev = None
    def __init__(self,data) -> None:
        self.data = data


class DLinkedList:
    head = None
    tail = None

 
    def display(self):
        temp = self.head
        while (temp != None):
            print(temp.data)
            temp = temp.next

    def displayReverse(self):
        temp = self.tail
        while (temp != None):
            print(temp.data)
            temp = temp.prev

    def insertAtEnd(self,data):
        newNode = Node(data)
        temp = self.head

        if (self.head == None):
            self.head = newNode
        else:
            self.tail.next = newNode
            newNode.prev = self.tail

        self.tail = newNode

    def deleteByValue(self,data):
        temp = self.head
        prev = None

        if (temp != None and temp.data == data ):
            self.head = temp.next
            return


        while (temp != None and temp.data != data):
            prev = temp
            temp = temp.next

        if (temp == None):
            return

        if (temp == self.tail):
            self.tail = prev
            self.tail.next = None
            return

        prev.next = temp.next

    def ifValueExist(self,data):

        temp = self.head

        while (temp != None):
            if (temp.data == data):
                print(f"Data Found {temp.data}")
                return True
            temp = temp.next
        

if __name__ == '__main__':

    DList = DLinkedList()

    DList.insertAtEnd(100)
    DList.insertAtEnd(10)
    DList.insertAtEnd(20)
    DList.insertAtEnd(30)
    DList.deleteByValue(100)

    DList.display()
