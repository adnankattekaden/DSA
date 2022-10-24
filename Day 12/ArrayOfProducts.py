

def arrayOfProducts(array):
    products = [1 for _ in range(len(array))]

    for i in range(len(array)):
        runningProduct = 1
        for j in range(len(array)):
            if i != j:
                
                runningProduct *= array[j]
            
        products[i] = runningProduct

    return products

if __name__ == "__main__":
    arr = [10, 3, 5, 6, 2]
    res = arrayOfProducts(arr)
    print(res)