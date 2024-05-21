# n = int(input("Enter a number: "))
# total = 0

# For bucle

# if n > 0:
#    for i in range(1, n + 1):
#        total += 1 / n
#       total *= total
#    print(f"the total is {total}")
# else:
#    print("The number must be greater than 0, please try again...")


# While Bucle:

true = True

while true:
    n = int(input("Enter a number: \n"))
    total = 0
    if n > 0:
        for i in range(1, n + 1):
            total += 1 / n
            # total *= total
        print(f"\nThe total is {total}\n")
    else:
        print("\nPlease enter a number greater than 0: \n")
