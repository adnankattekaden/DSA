class Node:
    data = None
    next = None
    def __init__(self,data) -> None:
        self.data = data

class Stack:
    top = None

    def push(self,data):
        newNode = Node(data)
        
        if (self.top == None):
            self.top = newNode
        else:
            newNode.next = self.top
            self.top = newNode
        

    def pop(self):
        if (self.top == None):
            print("Stack UnderFlow")
            return

        self.top = self.top.next
            

    def display(self):
        
        current = self.top
        while (current != None):
            print(current.data)
            current = current.next


if __name__ == '__main__':
    stack = Stack()
    stack.push(10)
    stack.push(12)
    stack.push(11)

    stack.pop()
    stack.pop()
    stack.display()

