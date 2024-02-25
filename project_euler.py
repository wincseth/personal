import numpy as np
import math

# problem 3, lists prime factors of a number, find greatest prime factor

# isPrime function: input an integer, returns true/false based on whether it's prime or not
def isPrime(x):
    sqrtX = math.floor(np.sqrt(x))
    result = True
    for i in range(sqrtX):
        if (x % (i + 1) == 0 and (i + 1) != 1):
            result = False
    return result

# findPrimeFactors: input an integer, returns a list containing prime factors (returns itself if prime)
def findPrimeFactors(x):
    sqrtX = math.floor(np.sqrt(x))
    primeFactors = []
    num = x
    while (isPrime(num) == False):
        for i in range(2, int(num)):
            if (num % i == 0):
                primeFactors.append(i)
                num /= i
                break
    else:
        primeFactors.append(int(num))
    return primeFactors

# print(findPrimeFactors(600851475143))

# problem 4, find the largest palindrome product of two 3-digit numbers
def isPalindrome(x, y):
    product = str(x * y)
    result = True
    for i in range(math.floor(len(product)/2)):
        if (product[i] != product[len(product) - 1 - i]):
            result = False
    return result            

palindromeProducts = []
for i in range(1, 1000, 1):
    for j in range(1, 1000, 1):
        if (isPalindrome(i, j) == True):
            palindromeProducts.append(i * j)

greatestProduct = palindromeProducts[0]
for i in palindromeProducts:
    if (i > greatestProduct):
        greatestProduct = i
# print(greatestProduct)

# problem 5, smallest multiple 

# smallestMultiple function: input an integer, returns the smallest possible number evenly divisible by all the numbers from 1 to the input number
def smallestMultiple(max):
    numbers = []
    # fill the numbers list with the prime factors from 1 to max
    for i in range(1, max + 1):
        numbers.append(findPrimeFactors(i))
    print(numbers)

    # find minimum and maximum numbers in the list, we will loop between them
    maxNum = 0
    minNum = max
    for i in range(len(numbers)):
        for j in range(len(numbers[i])):
            if (numbers[i][j] > maxNum):
                maxNum = numbers[i][j]
            if (numbers[i][j] < minNum):
                minNum = numbers[i][j]
    print(minNum, maxNum)

    # loop from min to max numbers, check for duplicates, change one value to 1 if not factors of the same number

    for i in range(len(numbers)):
        for j in range(len(numbers[i])):
            if (numbers.count(numbers[i][j]) >= 2):
                print(numbers[i][j], "appears", numbers.count(numbers[i][j]), "times")

smallestMultiple(10)









        



