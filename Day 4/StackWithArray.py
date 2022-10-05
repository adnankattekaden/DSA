class Node:
    data = None
    next = None

    def __init__(self,data) -> None:
        self.data = data


class StackWithArray:

    top = None

    def push(self,data):

        index = 0
        for i in data:
            newNode = Node(i)
            if (self.top == None):
                self.top = newNode
            else:
                newNode.next = self.top
                self.top = newNode

            index += 1


    def pop(self):
        if (self.top == None):
            print(f"Empty")
            return

        self.top = self.top.next


    def display(self):
        current = self.top
        
        while (current != None):
            print(current.data)
            current = current.next




if __name__ == '__main__':
    stack = StackWithArray()
    arr = [19,20,40,32]
    stack.push(arr)
    stack.push([23,54])
    stack.pop()
    stack.pop()
    stack.pop()
    stack.display()