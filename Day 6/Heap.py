from turtle import right


class MinHeap:
    
    def __init__(self,array=None) -> None:
        if array is not None:
            self.buildHeap(array)
    
    def buildHeap(self,array):
        self.heap = array

        for i in range(self.parent(len(self.heap) - 1),-1,-1):
            self.shift_down(i)

        

    def shift_down(self,currentIdx):
        endIdx = len(self.heap) - 1
        leftIdx = self.left_child(currentIdx)

        while (leftIdx <= endIdx):
            rightIdx = self.right_child(currentIdx)
            idxToshift = None

            if rightIdx <= leftIdx and self.heap[rightIdx] < self.heap[leftIdx]:
                idxToshift = rightIdx
            else:
                idxToshift = leftIdx
            
            if self.heap[currentIdx] > self.heap[idxToshift]:

                self.heap[currentIdx],self.heap[idxToshift] = self.heap[idxToshift],self.heap[currentIdx]

                currentIdx = idxToshift
                leftIdx = self.left_child(currentIdx)
            else:
                return



    def shift_up(self,currentIdx):

        parentIdx = self.parent(currentIdx)

        while currentIdx > 0 and self.heap[parentIdx] > self.heap[currentIdx]:
            self.heap[currentIdx],self.heap[parentIdx] = self.heap[parentIdx],self.heap[currentIdx]
            
            currentIdx = parentIdx
            parentIdx = self.parent(currentIdx)


    def peak(self):
        return self.heap[0]

    def remove(self):
        self.heap[0],self.heap[len(self.heap)-1] = self.heap[len(self.heap)-1],self.heap[0]

        self.heap.pop(len(self.heap)-1)

        self.shift_down(0)

    def insert(self,value):
        self.heap.append(value)
        self.shift_up(len(self.heap)-1)

    def parent(self,i):
        return (i -1) // 2

    def left_child(self,i):
        return (i*2) + 1

    def right_child(self,i):
        return (i*2) + 2

    def display(self):
        for i in self.heap:
            print(i)

if __name__ == '__main__':
    arr = [6,2,8]
    heap = MinHeap(arr)

    heap.insert(1)
    heap.insert(5)
    heap.insert(15)
    heap.remove()
    heap.display()
