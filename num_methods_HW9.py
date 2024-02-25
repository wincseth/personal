import numpy as np
import openpyxl

workbook = openpyxl.Workbook()
worksheet = workbook.active
worksheet.append(["i", "x_i", "d_i", "relative error", "f(x_i)"])

############ Problem 1: Bisection Method for Minimization Algorithm With Printout Data Table ############

# Global Variables
counter = 0
a = 0.15
b = 0.5
tolerance = 10e-6

# store initial x values in a list
# In order: lower bracket, middle bracket, upper bracket, midpoint of lower and midde, midpoint of middle and upper
x = [a, (a + b)/2, b, (3*a + b)/4, (a + 3*b)/4]

# Evaluation Function and Table Printout
def f(x, x_min, x_max):
    global counter
    counter += 1
    interval = x_max - x_min
    output = np.sin(1/x) - 1
    rel_err = interval/((abs(x_max) + abs(x_min))/2)
    worksheet = workbook.active
    worksheet.append([counter, str("{:.7e}".format(x)), str("{:.7e}".format(interval)), str("{:.7e}".format(rel_err)), str("{:.15e}".format(output))])
    workbook.save("numMethodsHW9P1Table.xlsx")
    print(counter)
    return output

# store initial f(x) evaluations in a list
f_x = [f(x[0], x[0], x[2]), f(x[1], x[0], x[2]), f(x[2], x[0], x[2]), f(x[3], x[0], x[2]), f(x[4], x[0], x[2])]

# Bisection Method Minimization Function
def f_min_bisection():
    while ((x[2] - x[0])/((abs(x[2]) + abs(x[0]))/2) >= tolerance):
        # change bracketing and function evaluations depending on middle values
        if f_x[3] < f_x[1]:
            x[2] = x[1]
            x[1] = x[3]
            f_x[2] = f_x[1]
            f_x[1] = f_x[3]
            print("left bracket")
        elif f_x[4] < f_x[1]:
            x[0] = x[1]
            x[1] = x[4]
            f_x[0] = f_x[1]
            f_x[1] = f_x[4]
            print("right bracket")
        else:
            x[0] = x[3]
            x[2] = x[4]
            f_x[0] = f_x[3]
            f_x[2] = f_x[4]
            print("middle bracket")
        
        # reevaluate the midpoints and their function evaluations of upper and lower halves of the bracket
        x[3] = (3*x[0] + x[2])/4
        x[4] = (x[0] + 3*x[2])/4
        f_x[3] = f(x[3], x[0], x[2])
        f_x[4] = f(x[4], x[0], x[2])

    return "The minimum value found by the bisection method (x, f(x)) is " + str(x[1]) + " " + str(f_x[1])

workbook.save("numMethodsHW9P1Table.xlsx")
print(f_min_bisection())