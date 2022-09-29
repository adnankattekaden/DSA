class Node:
    data = None
    next = None

    def __init__(self,data) -> None:
        self.data = data


class Queue:

    front = None
    rear = None

    def enqueue(self,data):
        newNode = Node(data)

        if (self.rear == None):
            self.front =  self.rear = newNode
            return
        
        self.rear.next = newNode
        self.rear = newNode

    
    def dequeue(self):
        if (self.front == None):
            print("Empty")

        self.front = self.front.next

        if (self.front == None):
            self.rear = None

    def display(self):
        current = self.front

        if (self.front == None):
            print("Empty")

        
        while(current != None):
            print(current.data)
            current = current.next

if __name__ == '__main__':
    queue = Queue()

    queue.enqueue(10)
    queue.enqueue(20)
    queue.enqueue(40)

    queue.dequeue()

    queue.display()

