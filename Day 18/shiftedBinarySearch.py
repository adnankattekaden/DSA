def shifted_binary_search(array,target):
    return shifted_binary_search_helper(array,target,0,len(array)-1)


def shifted_binary_search_helper(array,target,left,right):
    if left > right:
        return -1


    middle = (left + right) // 2
    potentialMatch = array[middle]
    leftNum = array[left]
    rightNum = array[right]

    if target == potentialMatch:
        return middle
    elif leftNum <= potentialMatch:
        if target < potentialMatch and target >= leftNum:
            return shifted_binary_search_helper(array,target,left,middle-1)
        else:
            return shifted_binary_search_helper(array,target,middle+1,right)
    else:
        if target > potentialMatch and target <= rightNum:
            return shifted_binary_search_helper(array,target,middle+1,right)
        else:
            return shifted_binary_search_helper(array,target,left,middle-1)


if __name__ == "__main__":
    arr = [4,5,6,7,0,1,2] 
    target = 1

    res=shifted_binary_search(arr,target)
    print(res)