# Write a program that receive as data a positive integer number N, calculate the result of the serie 1 + (1/2) + 1(1/3)

# For bucle

# n = int(input("Enter a positive number: "))

# if n > 0:
#    total = 0
#    for i in range(1, n + 1):
#        total += 1 / i
#    print(f"The serie is: {total}")
# else:
#    print(f"The number {n} is not positive")

# While bucle

true = True

while true == True:
    n = int(input("Enter a positive number: "))

    if n > 0:
        true = False
        total = 0
        for i in range(1, n + 1):
            total += 1 / i
        print(f"\nThe serie is: {total} \n")
    else:
        print("\nThe number must be positive \n")
