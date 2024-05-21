# Write a program that allows u to generate the multiply table of an integer positive number n, starting from 1.

total = 0
test = True

while test == True:
    num = int(input("Enter a number: "))
    if num > 0:
        for i in range(1, 10):
            total = num**i
            print(f"The multiply table of the number {num}^{i} is {total}")
        test = False
    else:
        print("The number must be greater than 0, please try again... ")
