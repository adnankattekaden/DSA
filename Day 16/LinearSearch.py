def linear_search(array,target):
    print(array,target)
    for position in range(len(array)):
        
        if array[position] == target:
            return position

    return -1


if __name__ == "__main__":
    arr = [10, 20, 80, 30, 60, 50,110, 100, 130, 170]
    target = 10
    
    res=linear_search(arr,target)
    print(res)