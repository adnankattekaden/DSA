def searchForRange(array,target):
    finalRange = [-1,-1]

    alteredBinarySearch(array, target, 0, len(array)-1, finalRange, True)
    alteredBinarySearch(array, target, 0, len(array)-1, finalRange, False)

    return finalRange

def alteredBinarySearch(array,target,left,right,finalRange,goleft):
    if left > right:
        return

    mid = (left + right) // 2

    if array[mid] < target:
        alteredBinarySearch(array,target,mid+1,right,finalRange,goleft)
    elif array[mid] > target:
        alteredBinarySearch(array,target,left,mid-1,finalRange,goleft)
    else:
        if goleft:
            if mid == 0 or array[mid - 1] != target:
                finalRange[0] = mid
            else:
                alteredBinarySearch(array,target,left,mid-1,finalRange,goleft)
        else:
            if mid == len(array) -1 or array[mid + 1] != target:
                finalRange[1] = mid
            else:
                alteredBinarySearch(array,target,mid+1,right,finalRange,goleft)

if __name__ == "__main__":
    nums = [0, 1, 21, 33, 45, 45, 45, 45, 45, 45, 61, 71, 73,71,71,71]
    target = 71
    res = searchForRange(nums,target)
    print(res)