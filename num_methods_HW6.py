import math
import matplotlib.pyplot as plt

# Problem 1 -------------------------------
def product_even_sampling(x, N): # x is our approximating input value, N + 1 is number of points evenly distributed between [-1, 1]
    x_i = [] # stores location of points sampled from function
    delta_x = 2.0/(N)
    product = 1
    for i in range(0, N + 1):
        x_i.append(delta_x*i - 1)
        current_x = x_i[i]
        product *= (x - current_x)
    return product



# Problem 2 -------------------------------
def product_cheb_sampling(x, N):
    x_i = []
    product = 1
    for i in range(0, N + 1):
        x_i.append(math.cos((2*N + 1 - 2*i)*math.pi/(2*N + 2))) # Chebyshev sampled points get stored into x_i
        current_x = x_i[i]
        product *= (x - current_x)
    return product

# this function finds the log base 10 value of product, allows for both sample types
# 3rd argument: 0 for evenly-sampled x_i, 1 for Chebyshev-sampled x_i
def plot_y(x, N, sample_type):
    if (sample_type == 0):
        return math.log10(max(10**(-150), abs(product_even_sampling(x, N))))
    elif (sample_type == 1):
        return math.log10(max(10**(-150), abs(product_cheb_sampling(x, N))))
'''
# Problem 3 -------------------------------- 
x_approx = [] # list that will hold the x values to be approximated with the two product functions

# these lists will hold the y value products with both types of sampling and different N values
even_sampled_y_vals_5 = []
cheb_sampled_y_vals_5 = []
even_sampled_y_vals_10 = []
cheb_sampled_y_vals_10 = []
even_sampled_y_vals_200 = []
cheb_sampled_y_vals_200 = []

# fill in data into lists
for j in range(0, 2001):
    x_approx.append(-1 + j/1000)
    even_sampled_y_vals_5.append(plot_y(x_approx[j], 5, 0))
    cheb_sampled_y_vals_5.append(plot_y(x_approx[j], 5, 1))

    even_sampled_y_vals_10.append(plot_y(x_approx[j], 10, 0))
    cheb_sampled_y_vals_10.append(plot_y(x_approx[j], 10, 1))

    even_sampled_y_vals_200.append(plot_y(x_approx[j], 200, 0))
    cheb_sampled_y_vals_200.append(plot_y(x_approx[j], 200, 1))

# function holding common plot styles between the three plots, arguments are y axis limits
def plot_style(ylim_min, y_lim_max):
    plt.ylabel("Logarithmic Product")
    plt.xlabel("Values to be Multiplied")
    plt.xlim(-1, 1)
    plt.ylim(ylim_min, y_lim_max)
    plt.legend(["Even Sampling", "Chebyshev-Sampling"])

# plot data, parts b, c, and d
plt.subplot(3, 1, 1)
plt.plot(x_approx, even_sampled_y_vals_5, color = "red")
plt.plot(x_approx, cheb_sampled_y_vals_5, color = "blue", linestyle = "dashed")
plt.title("Logarithmic Products Using\nEven and Chebyshev-Sampled Intervals,\n5 Intervals Each")
plot_style(-4, -1)

plt.subplot(3, 1, 2)
plt.plot(x_approx, even_sampled_y_vals_10, color = "red")
plt.plot(x_approx, cheb_sampled_y_vals_10, color = "blue", linestyle = "dashed")
plt.title("Logarithmic Products Using\nEven and Chebyshev-Sampled Intervals,\n10 Intervals Each")
plot_style(-5.5, -2)

plt.subplot(3, 1, 3)
plt.plot(x_approx, even_sampled_y_vals_200, color = "red")
plt.plot(x_approx, cheb_sampled_y_vals_200, color = "blue", linestyle = "dashed")
plt.title("Logarithmic Products Using\nEven and Chebyshev-Sampled Intervals,\n200 Intervals Each")
plot_style(-90, -20)

plt.show()
'''
# Problem 4 --------------------------------
N_vals = []
y_1_graph = []
y_2_graph = []

# Write table into a text file
with open('numMethodsHW6Table.txt', 'w') as table:
    # write table header
    table.write("N\t\ty_1(N)\t\t\t\t\t\ty_2(N)")
    
    for i in range(0, 50):
        y_1 = []
        y_2 = []

        # fill list with values for N
        N_vals.append(i*10 + 5)

        # write current N value into file
        table.write('\n\n')
        table.write(str(N_vals[i]))

        # fill out products for current N at different x
        for j in range(0, 2001):
            current_x = -1 + j/1000
            y_1.append(plot_y(current_x, N_vals[i], 0))
            y_2.append(plot_y(current_x, N_vals[i], 1))

        # find maximum value out of all the products
        y_1_max = max(y_1)
        y_2_max = max(y_2)

        # Store the max value into lists, saving for problem 5
        y_1_graph.append(y_1_max)
        y_2_graph.append(y_2_max)
        
        # write max values into file
        table.write('\t\t')
        table.write(str("{:.14e}".format(y_1_max)))
        table.write('\t\t')
        table.write(str("{:.14e}".format(y_2_max)))


# Problem 5 --------------------------------
plt.plot(N_vals, y_1_graph, color = "red")
plt.plot(N_vals, y_2_graph, color = "blue", linestyle = "dashed")
plt.title("Maximum Logarithmic Products for Different Node Amounts")
plt.xlabel("Number of Nodes for Each Product (N)")
plt.ylabel("Products, Sampled Between [-1, 1]")
plt.legend(["Even Sampling", "Chebyshev-Sampling"])
plt.show()
