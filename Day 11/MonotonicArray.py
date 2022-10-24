
def isMonotonic(array):
    if len(array) <= 2:
        return True

    direction = array[1] - array[0]
    print(direction,array[1],array[0])

    for i in range(2,len(array)):

        if direction == 0:
            direction = array[i] - array[i - 1]

            continue
        
        if breakDirection(direction,array[i - 1],array[i]):
            return False

    return True

def breakDirection(direction,prev,current):

    difference = current - prev


    if difference > 0:
        return difference < 0


    return difference > 0


if __name__ == '__main__':
    arr =  [6, 5, 4, 4]

    res = isMonotonic(arr)
    print(res)