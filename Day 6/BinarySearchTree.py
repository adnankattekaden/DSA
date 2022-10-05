class Node:
    data = None
    left,right = None,None

    def __init__(self,data) -> None:
        self.data = data


class BinarySearchTree:
    root = None

    def insert(self,data):
        currentNode = self.root

        if (currentNode == None):
            self.root = Node(data)
            return
        
        while True:
            if (data < currentNode.data):
                if (currentNode.left == None):
                    currentNode.left = Node(data)
                    break
                else:
                    currentNode = currentNode.left
            else:
                if (data > currentNode.data):
                    if (currentNode.right == None):
                        currentNode.right = Node(data)
                        break
                    else:
                        currentNode = currentNode.right

    
    def contains(self,data):
        currentNode = self.root
        while (currentNode != None):
            if (data < currentNode.data):
                currentNode = currentNode.left
            elif (data > currentNode.data):
                currentNode = currentNode.right
            else:
                print(f'Contains {currentNode.data}')
                return True

        print('Not Available')
        return False


    def remove(self,data):
        self.removeHelper(data,self.root,None)
    


    def removeHelper(self,data,currentNode,parentNode):
        while (currentNode != None):
            if (data < currentNode.data):
                parentNode = currentNode
                currentNode = currentNode.left
            elif (data > currentNode.data):
                parentNode = currentNode
                currentNode = currentNode.right
            else:
                if (currentNode.left != None and currentNode.right != None):
                    currentNode.data = self.getMinValue(currentNode.right)
                    self.removeHelper(currentNode.data,currentNode.right,currentNode)
                else:
                    if (parentNode == None):
                        if (currentNode.right == None):
                            self.root = currentNode.left
                        else:
                            self.root = currentNode.right
                    else:

                        if (parentNode.left == currentNode):
                            if (currentNode.right == None):
                                parentNode.left = currentNode.left
                            else:
                                parentNode.left = currentNode.right
                        else:
                            if (parentNode.right == currentNode):
                                if (currentNode.left == None):
                                    parentNode.right = currentNode.right
                                else:
                                    parentNode.right = currentNode.right
                
                break;

 
    def getMinValue(self,currentNode):
        if (currentNode.left == None):
            return currentNode.data
        else:
            return self.getMinValue(currentNode.left)

    def getMaxValue(self):
        current = self.root
        while (current.right):
            current = current.right

        print(f"Max Value Is {current.data}")        
        return current.data


    def inOrder(self):
        self.inOrderHelper(self.root)

    
    def inOrderHelper(self,node):
        if (node != None):
            self.inOrderHelper(node.left)
            print(node.data)
            self.inOrderHelper(node.right)

    def preOrder(self):
        self.preOrderHelper(self.root)

    def preOrderHelper(self,node):
        if (node != None):
            print(node.data)
            self.inOrderHelper(node.left)
            self.inOrderHelper(node.right)

    def postOrder(self):
        self.postOrderHelper(self.root)

    
    def postOrderHelper(self,node):
        if (node != None):
            self.postOrderHelper(node.left)
            self.postOrderHelper(node.right)
            print(node.data)




if __name__ == '__main__':
    bst = BinarySearchTree()
    
    bst.insert(10)
    bst.insert(8)
    bst.insert(11)
    bst.insert(4)
    bst.insert(9)
    bst.insert(100)
    bst.insert(5)
    bst.insert(200)
    bst.insert(110)

    bst.getMaxValue()

    