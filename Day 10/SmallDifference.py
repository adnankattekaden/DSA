def smallestDifference(arrayOne,arrayTwo):
    arrayOne.sort()
    arrayTwo.sort()



    idxOne = 0
    idxTwo = 0

    smallest = float("inf")
    current = float("inf")


    smallestPair = []

    while idxOne < len(arrayOne) and idxTwo < len(arrayTwo):
        firstNum = arrayOne[idxOne]
        secondNum = arrayTwo[idxTwo]

        if firstNum < secondNum:
            current = secondNum - firstNum
            idxOne += 1
        elif secondNum < firstNum:
            current = firstNum - secondNum
            idxTwo += 1
        else:
            return [firstNum,secondNum]

        if smallest > current:
            smallest = current
            smallestPair = [firstNum,secondNum]


    return smallestPair


if __name__ == '__main__':
    arrOne =  [0, -6, 4, 6, 5, -2]
    arrTwo = [-4, 8, 2, 3, 10, 9]
    result = smallestDifference(arrOne,arrTwo)
    print(result)