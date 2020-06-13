import matplotlib.pyplot as plt
from matplotlib import style

style.use('fivethirtyeight')
plt.xlabel('Iteration')
plt.ylabel('Value')

num_array = []

def calc(x):
    while x != 1:
        if x % 2 == 0:
            x /= 2
            x = int(x)
        else:
            x = 3 * x + 1
        num_array.append(x)
        print("Iteration: {0} Value: {1}".format(len(num_array)-1, x))
    print("Number 1 reached in {0} operations".format(len(num_array)-1))

number = int(input("Enter a number: "))
print("Initial Value: {0}".format(number))
num_array.append(number)
calc(number)

for i in range(len(num_array)):
    plt.annotate(str(num_array[i]),
                 (i, num_array[i]),
                 textcoords="offset points",
                 xytext=(0,10),
                 ha='center',
                 rotation=90)

plt.xticks(range(0, len(num_array)))
plt.plot(num_array, '-o', color='r', linewidth=1.5)

plt.tight_layout()
plt.show()
