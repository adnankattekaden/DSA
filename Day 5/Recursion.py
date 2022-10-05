def factorial(number):


    if number <= 1:
        return 
    
    factorial(number -1)
    print(number)
    factorial(number-1)



res = factorial(5)