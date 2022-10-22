
def sortedSquaredArray(array):
    sortedSquares = [0 for _ in arr]

    for idx in range(len(array)):
        value = array[idx]
        sortedSquares[idx] = value * value

    sortedSquares.sort()

    return sortedSquares


if __name__ == '__main__':
    arr = [-5,-2,-1,0,4,6]
    
    res = sortedSquaredArray(arr)
    print(res)