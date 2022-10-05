class Node:
    data = None
    next = None
    def __init__(self,data) -> None:
        self.data = data


class QueueWithArray:
    front = None
    rear = None

    def enqueue(self,data):
        for i in data:
            newNode = Node(i)

            if (self.rear == None):
                self.front =  self.rear = newNode
                
            
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
    queue = QueueWithArray()
    arr = [10,39,403,233]
    queue.enqueue(arr)
    queue.dequeue()
    queue.dequeue()
    queue.display()