
def largestRange(array):
    bestRange = []
    longestLength = 0
    nums = {}
    for num in array:
        nums[num] = True


    for num in array:
        if not nums[num]:
            continue

        nums[num] = False
        currentLength = 1
        left = num - 1
        right = num + 1
        
        while left in nums:
            nums[left] = False
            currentLength += 1
            left -= 1

        while right in nums:
            num[right] = False
            currentLength += 1
            right += 1

        if currentLength > longestLength:
            longestLength = currentLength
            bestRange = [left+1,right-1]

    return bestRange

if __name__ == "__main__":
    arr = [100, 4, 200, 1, 3, 2]
    res = largestRange(arr)
    print(res)