def longestPeak(array):

    longestPeakLength = 0
    i = 1

    while i < len(array) -1:
        isPeak = array[i - 1] < array[i] and array[i] > array[i+1]


        if not isPeak:
            i += 1
            continue

        leftIdx = i -2
        while leftIdx >= 0 and array[leftIdx] < array[leftIdx + 1]:
            leftIdx -= 1

        rightIdx = i+2
        while rightIdx < len(array) and array[rightIdx] < array[rightIdx - 1]:
            rightIdx += 1

        
        currentPeakLength = rightIdx - leftIdx - 1
        longestPeakLength = max(longestPeakLength,currentPeakLength)

        i = rightIdx

    return longestPeakLength

if __name__ == "__main__":
    arr =  [1, 3, 1, 4, 5, 6, 7, 8, 9, 8, 7, 6, 5]

    res = longestPeak(arr)
    print(res)