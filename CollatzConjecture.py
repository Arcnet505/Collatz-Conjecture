number = int(input("Enter a number: "))
print(number)
count = 0

while number != 1:
    if number % 2 == 0:
        number /= 2
    else:
        number = 3 * number + 1
    print(int(number))
    count += 1
print("Number 1 reached in {0} operations".format(count))