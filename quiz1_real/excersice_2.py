# Narcicist numbers

num = input("Enter a number: ")
num_len = len(num)
total = 0

for i in num:
    x = int(i) ** int(num_len)
    total += x

if total == int(num):
    print("It is narcissistic")
else:
    print("It is not narcissistic")
