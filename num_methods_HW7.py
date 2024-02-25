import math
import matplotlib.pyplot as plt

count = 0
# l corresponds to the lth Fourier series coefficient for both sine and cosine coefficients
l = 0
# trig_funct determines which Fourier series coefficient to calculate: 0 means cosine, 1 means sine
trig_funct = 0

def f(x):
    global count
    # change output according to f(x) definition
    # problem 2a, f(t) = |sin(2*PI*t)|
    if (trig_funct == 0): 
        output = abs(math.sin(2*math.pi*x))*math.cos(l*math.pi*x/3.1)
    elif (trig_funct == 1):
        output = abs(math.sin(2*math.pi*x))*math.sin(l*math.pi*x/3.1)
    count += 1
    return output

def R00(a, b): 
    # R(0, 0) = output
    output = (1/2)*(b - a)*(f(a) + f(b))
    return output

#Rn_minus_1 = function
def RN0(Rn_minus_1, n, a, b):
    # R(n, 0) = output
    h_n = (b - a)/(2**n)
    output = 0
    for k in range(1, (2**(n-1))+1):
        output += f(a + (2*k-1)*h_n)
    output *= h_n
    output += (1/2)*Rn_minus_1
    return output

def RNM(Rn_mm1, Rnm1_mm1, m):
    # R(n, m) = output
    output = (1/((4**m)-1))*((4**m)*Rn_mm1 - Rnm1_mm1)
    return output

def R_nm(n, m, a, b):
    RR = []
    for i in range(0, 51):
        RR.append([])
        for j in range(0, 51):
            RR[i].append(0)
    #initialize R(0, 0)
    RR[0][0] = R00(a, b)

    # Loop through first column of each row, building R(n, 0)
    for i in range(1, n + 1):
        RR[i][0] =  RN0(RR[i-1][0], i, a, b)
        # loop through the column spaces in current row, building from R(n, 0) to R(n, m)
        for j in range(1, m + 1):
            RR[i][j] = RNM(RR[i][j - 1], RR[i - 1][j - 1], j)
    return RR[n][m]

y_vals_m0 = []
y_vals_m1 = []
y_vals_m2 = []

y_vals_error_m0 = []
y_vals_error_m1 = []
y_vals_error_m2 = []

# n must be greater than or equal to m
'''
def main_function():
    global count
    a = 0
    b = math.pi/2
    # exact integral = F = 1
    F = 1

    for m in range(0, 3):
        for n in range(m, 9):
            count = 0
            E_nm = abs((R_nm(n, m, a, b) - F)/F)
            F_nm = count
            if (m == 0):
                y_vals_m0.append(math.log10(F_nm))
                y_vals_error_m0.append(math.log10(E_nm))
            elif(m == 1):
                y_vals_m1.append(math.log10(F_nm))
                y_vals_error_m1.append(math.log10(E_nm))
            elif(m == 2):
                y_vals_m2.append(math.log10(F_nm))
                y_vals_error_m2.append(math.log10(E_nm))
'''
       
#main_function()

'''
print(R_nm(1, 1, 0, math.pi/2))
print(count)
count = 0
'''

# Part c graphs
'''
plt.subplot(1, 3, 1)
plt.plot(range(0, 9), y_vals_m0, color='blue')
plt.title("Number of Function Evaluations VS n\nin Romberg Integrator, m = 0")
plt.xlabel("n Parameter in R(n, m)")
plt.ylabel("Function Evaluations, in Base 10 Logarithms")

plt.subplot(1, 3, 2)
plt.plot(range(1, 9), y_vals_m1, color='red')
plt.title("Number of Function Evaluations VS n\nin Romberg Integrator, m = 1")
plt.xlabel("n Parameter in R(n, m)")
plt.ylabel("Function Evaluations, in Base 10 Logarithms")

plt.subplot(1, 3, 3)
plt.plot(range(2, 9), y_vals_m2, color='green')
plt.title("Number of Function Evaluations VS n\nin Romberg Integrator, m = 2")
plt.xlabel("n Parameter in R(n, m)")
plt.ylabel("Function Evaluations, in Base 10 Logarithms")
plt.show()
'''

# Part d graph
'''
plt.plot(range(0, 9), y_vals_error_m0, color='blue')
plt.plot(range(1, 9), y_vals_error_m1, color='red')
plt.plot(range(2, 9), y_vals_error_m2, color='green')
plt.title("Problem 1d")
plt.ylabel("Logarithmic Error")
plt.xlabel("n value in R(n, m)")
plt.legend(["m = 0", "m = 1", "m = 2"])
plt.show()
'''

# Part f graph
'''
a_1f = 0
b_1f = 11*math.pi
error_m0_p1f = []
error_m1_p1f = []
error_m2_p1f = []
E_nm_1f = 0
F_1f = 2
for m in range(0, 3):
    for n in range(m, 21):
        E_nm_1f = abs((R_nm(n, m, a_1f, b_1f) - F_1f)/F_1f)
        if (m == 0):
            error_m0_p1f.append(math.log10(E_nm_1f))
        elif (m == 1):
            error_m1_p1f.append(math.log10(E_nm_1f))
        elif (m == 2):
            error_m2_p1f.append(math.log10(E_nm_1f))

plt.plot(range(0, 21), error_m0_p1f, color='blue')
plt.plot(range(1, 21), error_m1_p1f, color='red')
plt.plot(range(2, 21), error_m2_p1f, color='green')
plt.title("Problem 1f")
plt.ylabel("Logarithmic Error")
plt.xlabel("n value in R(n, m)")
plt.xticks(range(0, 21))
plt.legend(["m = 0", "m = 1", "m = 2"])
plt.grid(True)
plt.show()
'''

# Problem 2 part a

# lists to store table values
a_l_R54 = []
a_l_R104 = []
a_l_extrap = []
b_l_R54 = []
b_l_R104 = []
b_l_extrap = []

def main_function():
    global count
    global l
    global trig_funct
    
    # Richardson extrapolation function using R(5, 4) and R(10, 4)
    def r_extrap(a, b):
        F = ((1024*R_nm(10, 4, a, b) - R_nm(5, 4, a, b))/1023)
        return F
    # L is our Fourier series period divided by 2
    L = 3.1

    # write out table data into text file
    with open('numMethodsHW7Table.txt', 'w') as table:
        table.write("\tR(5, 4)\t\tR(10, 4)\tRichardson Extrap.\tR(5, 4)\t\tR(10, 4)\tRichardson Extrap.")
        table.write("\nl\ta_l\t\t\ta_l\t\t\ta_l\t\t\t\t\tb_l\t\t\tb_l\t\t\tb_l")
        for i in range(0, 51):
            # formula: a_l or b_l = (2/L)R(n, m)
            l = i

            # evaluate a_l, cosine coefficients
            trig_funct = 0
            a_l_R54.append((1/3.1)*R_nm(5, 4, -3.1, 3.1))
            a_l_R104.append((1/3.1)*R_nm(10, 4, -3.1, 3.1))
            a_l_extrap.append((1/3.1)*r_extrap(-3.1, 3.1))

            table.write("\n" + str(l) + "\t")
            table.write(str("{:.4e}".format(a_l_R54[i])) + "  ")
            table.write(str("{:.4e}".format(a_l_R104[i])) + "  ")
            table.write(str("{:.4e}".format(a_l_extrap[i])) + "  ")

            # evaluate b_l, sine coefficients
            trig_funct = 1
            b_l_R54.append((1/3.1)*R_nm(5, 4, -3.1, 3.1))
            b_l_R104.append((1/3.1)*R_nm(10, 4, -3.1, 3.1))
            b_l_extrap.append((1/3.1)*r_extrap(-3.1, 3.1))

            table.write("\t\t" + str("{:.4e}".format(b_l_R54[i])) + "  ")
            table.write(str("{:.4e}".format(b_l_R104[i])) + "  ")
            table.write(str("{:.4e}".format(b_l_extrap[i])) + "  ")
main_function()

# Part 2c, plot the Fourier series approximation
x_2c = []
y_2c = []
for j in range(0, 201):
    t_val = 2 + j*0.01
    x_2c.append(t_val)
    # initialize the first term in the fourier series to a_0/2
    fourier_sum = a_l_R104[0]/2
    for i in range(1, 51):
        fourier_sum += ((a_l_R104[i]*math.cos(i*math.pi*t_val/3.1)) + (b_l_R104[i]*math.sin(i*math.pi*t_val/3.1)))
    y_2c.append(fourier_sum)
plt.plot(x_2c, y_2c)
plt.title("Fourier series representation of |sin(2*PI*t)|\n-3.1 <= t <= 3.1")
plt.xlabel("t values from 2 to 4")
plt.ylabel("Approximation using Romberg Integration R(10, 4)")
plt.show()


