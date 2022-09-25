

class Node:
    data = None
    next = None

    def __init__(self,data) -> None:
        self.data = data

class SLinkedList:
    head = None
    tail = None

    def display(self):
        
        if (self.head == None):
            print("Empty")
            return

        temp = self.head
        while (temp != None):
            print(temp.data)
            
            temp = temp.next

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

    def insertAtBeginning(self,data):
        
        newNode = Node(data)

        if (self.head == None):
            self.head = newNode
        else:
            newNode.next = self.head

        self.head = newNode

    def insertAtEnd(self,data):

        newNode = Node(data)
        temp = self.head

        if (self.head == None):
            self.head = newNode
            return
        
        while(temp.next != None):
            temp = temp.next
        


        temp.next = newNode

    def insertAfterValue(self,element,data):
        newNode = Node(data)
        temp = self.head

        while (temp != None and temp.data != element):
            temp = temp.next

        if (temp == None):
            return

        
        if (temp == self.tail):
            self.tail.next = newNode
            self.tail = newNode
            return
            

        newNode.next = temp.next
        temp.next = newNode

    def ifValueExist(self,data):
        temp = self.head
        while (temp != None):
            if (temp.data == data):
                print(f"{data} Exists")
                return True
            temp = temp.next
            
    def totalElementCount(self):
        temp = self.head
        count = 0
        while (temp != None):
            count = count + 1
            temp = temp.next

        print(f"{count} Elements Available")
        return count
    
    def insertFromArray(self,data):
        for i in data:
            self.insertAtEnd(i)


if __name__ == '__main__':

    List = SLinkedList()

    List.insertAtBeginning(5)
    List.insertAtBeginning(10)
    List.insertAtBeginning(15)
    List.insertAtEnd(100)
    List.insertAtEnd(20)
    List.insertAfterValue(100,3)
    List.ifValueExist(3)
    List.totalElementCount()
    arr = [1,3,4,90]
    List.insertFromArray(arr)

    List.display()