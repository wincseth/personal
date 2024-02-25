import math
import matplotlib.pyplot as plt
import numpy as np
pi = math.pi


# factorial function
def factorial(n):
    product = 1
    for i in range(1, n + 1):
        product *= i # multiply product by each value up to n
    return product

# defines sine and cosine functions based on the given x_0 values
def sin(x):
    if (x == 0 or x == pi):
        value = 0
    elif (x == pi/4):
        value = 1.414213562373095048/2 # sine of pi/4 = sqrt(2) divided by 2
    elif (x == 3*pi/2):
        value = -1
    return value

def cos(x):
    if (x == 0):
        value = 1
    elif (x == pi/4):
        value = 1.414213562373095048/2
    elif (x == pi):
        value = -1
    elif (x == 3*pi/2):
        value = 0
    return value

# general pattern: [sin(x), cos(x), -sin(x), -cos(x)] repeating for n = 1, 2, 3, 4, ...
# puts this pattern into a list with the 4 repeating terms
def sinTS_derivative_pattern(x0):
    pattern = [sin(x0), cos(x0), -1*sin(x0), -1*cos(x0)] # corresponds to n = [1, 2, 3, 4] and repeats as n increases
    return pattern


# Prints the coefficients of the Taylor Series approximation of sine about either x = 0, pi/4, pi, 3*pi/2
# Incorporates the factorial, sin, cos, and pattern list functions defined previously
def sinTS_coefficients(x0):
    
    pattern = sinTS_derivative_pattern(x0) # store the repeating derivative pattern in a variable
    n = 0 # equivalent to the n used in summation of a Taylor Series
    coefficient = 1

    print("Taylor Series coefficients about the point x =", x0)

    while abs(coefficient) > 10**(-31) or coefficient == 0.0: # checks if the coefficient's absolute value is nonzero and greater than specified value
        if coefficient != 0: # only print nonzero coefficients and it's corresponding n
            print("n =", n, "| coefficent =", coefficient)
        
        n += 1
        pattern_index = (n - 1 + len(pattern)) % len(pattern) # finds the derivative term to use based on current n
        coefficient = pattern[pattern_index]/factorial(n) # updates the coefficent output (nth derivative of sine divided by n factorial)
    print("\n")

"""
sinTS_coefficients(0)
sinTS_coefficients(pi/4)
sinTS_coefficients(pi)
sinTS_coefficients(3*pi/2)
"""

# PROBLEM 3
'''
def sqrtx(x):
    value = 0
    for i in range(0, 100):
        value += ((0.5 - i + 1)*(math.pow(x-1, i)))/math.factorial(i)
    return value
'''

#print(sqrtx(4))
def double_factorial(n):
    value = 1
    while n > 0:
        value *= n
        n -= 2
    return value

n = 50

#print(double_factorial((2*n)-3)/((2**n)*factorial(n)))

def sqrt_TS_epsilon(x):
    # about x0 = 1
    # does not add the first term
    # accepts epsilon, returns next epsilon
    result = 0
    for i in range(1, 31):
        result += (((-1)**(i-1))*((x)**i)*double_factorial((2*i) - 3)/((2**i)*factorial(i)))
    return result
e = math.sqrt(2.0) - 1
#print(math.sqrt(math.sqrt(2)))
#print(sqrt_TS_epsilon(e))
'''
Problems/Confusions:
- Writing the taylor series of the square root function about x0 = 1 converges WAY too slowly
- Still confused on a or epsilon, performing square root on the epsilon is of course bigger than what it was previously - not what we want...

Thoughts:
- every iteration of the square root MUST reference a in relation to x (add 1?) - otherwise taking the square root of just the epsilon is wrong
- 1 + epsilon evaluated (16 sig. fig. acc.) - 1.0 (infinite sig. fig. acc.) gives us epsilon at 16 sig. figs. of acc. - do this operation after every square root?
- second loop should be relatively simple, add 1 to the epsilon found, hopefully more accurate than parts (a) and (b), and square it back N times
'''

def x(N):
    x = 2.0
    epsilon = 0.0
    for i in range(0, N + 1):
        if (i == 1 or i == 0):
            if (i == 1):
                x = math.sqrt(x)
            epsilon = x - 1.0
        else:
            epsilon = sqrt_TS_epsilon(epsilon)
    for i in range(1, N + 1):
        epsilon = (epsilon * epsilon) + 2*epsilon
    x = epsilon + 1
    return x

def print_val():
    x = 2.0
    epsilon = 0.0
    for i in range(0, 51):
        if (i == 1 or i == 0):
            if (i == 1):
                x = math.sqrt(x)
            epsilon = x - 1.0
            print(i, "{:.14e}".format(epsilon))
        else:
            epsilon = sqrt_TS_epsilon(epsilon)
            print(i, "{:.14e}".format(epsilon))
print_val()


NVal = []
rel_err = []
for i in range(0, 51):
    NVal.append(i)
    rel_err.append(np.abs((2.0 - x(i))/2.0))

fig, ax = plt.subplots()
plt.plot(NVal, rel_err)
plt.title("Relative Error For Fixed Point Algorithm")
plt.xlabel("N Values")
plt.ylabel("Logarithmic Error")
ax.set_yscale('log')
plt.show()



# Parts a and b
'''
def x(N):
    x = 2.0
    for i in range(0, N + 1):
        #print("i", "x")
        if (i != 0):
            x = math.sqrt(x)
            #print(i, "{:.14e}".format(x))
            # this x should approach 1 as x approaches infinity
    for i in range(0, N + 1):
        if (i != 0):
            x = x * x
    return x
for i in range(0, 51):
    print(x(i))

NVal = []
rel_err = []
for i in range(0, 51):
    NVal.append(i)
    rel_err.append(np.log10(np.abs((2.0 - x(i))/2.0)))

print(NVal)
print(rel_err)
plt.plot(NVal, rel_err)
plt.show()
'''
