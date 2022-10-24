
def firstDuplicateValue(array):
    seen = set()
    for value in array:
        if value in seen:
            return value

        seen.add(value)

    return -1   

if __name__ == "__main__":
    arr =  [5, 3, 4, 3, 5, 6]
    res = firstDuplicateValue(arr)
    print(res)