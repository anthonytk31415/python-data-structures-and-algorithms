import matplotlib.pyplot as plt

# Given array
array = [1, 5, 8, 12, 14, 15, 16, 17, 18]

# 17 original delta
# new delta at i = 4: 17 - 4 = 13

k = 3

# X-axis values (indices)
x = list(range(len(array)))

# Original array (y = array[i])
y = array
y_plus_k = [value + k for value in array]
y_minus_k = [value - k for value in array]

def calcDelta(i):
    left = y_plus_k[0]
    right = y_minus_k[-1]
    plus_i = y_plus_k[i]
    minus_iminus1 = y_minus_k[i + 1]
    return abs(max(right, plus_i) - min(left, minus_iminus1))

res = []
for i in range(len(array)-1):
    res.append([i, calcDelta(i)])
print("i and the ranges of i: ", res)

print ("optimal i: ")
delta = calcDelta(i)
print("delta: {}; i: {}".format(delta, i))


def calcPlot(i):
    # Plotting the original array
    plt.plot(x, y, 'bo-', label='y = array[i]', color='blue')

    # Plotting array + k
    plt.plot(x, y_plus_k, 'go-', label='y = array[i] + k', color='green')

    # Plotting array - k
    plt.plot(x, y_minus_k, 'ro-', label='y = array[i] - k', color='red')

    # Overlay horizontal lines
    plt.axhline(y=y_plus_k[0], color='black', linestyle='--', linewidth=1, label='y = array[0] + k')
    plt.axhline(y=y_minus_k[-1], color='black', linestyle='--', linewidth=1, label='y = array[n-1] - k')
    plt.axhline(y=y_plus_k[i], color='black', linestyle='--', linewidth=1, label='y = array[4] + k')
    plt.axhline(y=y_minus_k[i + 1], color='black', linestyle='--', linewidth=1, label='y = array[5] - k')

    # Adding labels and title
    plt.xlabel('Index (i)')
    plt.ylabel('Array Value')
    plt.title('Graph of array, array + k, array - k with horizontal lines')

    # Adding grid
    plt.grid(True)

    # Show the legend
    plt.legend()

    # Display the graph
    plt.show()

calcPlot(3)

