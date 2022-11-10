def searchSortedMatrix(matrix,target):
    row = 0
    col = len(matrix[0]) - 1
    while row < len(matrix) and col >=0:
        if matrix[row][col] > target:
            col -= 1
        elif matrix[row][col] < target:
            row += 1
        else:
            return [row,col]

    return [-1,-1 ]

if __name__ == "__main__":
    matrix = [
                [1,3,5,7],
                [10,11,16,20],
                [23,30,34,60]
            ]
    target = 20
    res=searchSortedMatrix(matrix,target)

    print(res)