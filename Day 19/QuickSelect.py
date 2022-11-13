def quick_select(array,k):
    position = k - 1
    return quick_select_helper(array,0,len(array)-1,position)

def quick_select_helper(array,startIdx,endIdx,position):
    while True:
        
        if startIdx > endIdx:
            raise Exception("Your Algorithm Should Never Arrive Here")

        pivotIdx = startIdx
        leftIdx = startIdx + 1
        rightIdx = endIdx

        while leftIdx <= rightIdx :
            if array[leftIdx] > array[pivotIdx] and array[rightIdx] < array[pivotIdx]:
                swap(leftIdx,rightIdx,array)
            elif array[leftIdx] <= array[pivotIdx]:
                leftIdx += 1
            elif array[rightIdx] >= array[pivotIdx]:
                rightIdx -= 1
            
        swap(pivotIdx,rightIdx,array)

        if rightIdx == position:
            return array[rightIdx]
        elif rightIdx < position:
            startIdx = rightIdx +1
        else:
            endIdx = rightIdx - 1
                

def swap(leftIdx,rightIdx,array):
    array[leftIdx],array[rightIdx] = array[rightIdx],array[leftIdx]


if __name__ == "__main__":
    nums = [8, 5, 2, 9, 7, 6, 3]
    k = 6

    res=quick_select(nums,k)
    print(res)