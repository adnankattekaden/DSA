
def nonConstructableChange(coins):
    coins.sort()
    currentChangeCreated = 0
    for coin in coins:

        if coin > currentChangeCreated + 1:
            return currentChangeCreated + 1
        
        currentChangeCreated += coin

    return currentChangeCreated + 1

if __name__ == '__main__':

    arr = [3, 5, 6, 7, 8, 10]
    res=nonConstructableChange(arr)
    print(res)