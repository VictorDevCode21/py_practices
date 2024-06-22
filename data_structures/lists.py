#

# num = [24, 12, 5, 6, 7, 8, 9, 10, 20]

# How to acces to each string of my list


# Join lists
# list1 = num[0:3]
# list2 = num[3:5]

# final_list = list1 + list2


# Modify lists content

# num.append(5)
# num[1] = 0

# Remove content from lists

# num[:2] = []

# Example of how to reverse list and run on the other half of the list

# num.reverse()

num = [24, 12, 5, 6, 7, 8, 9, 10, 20]
answer = []

total = 0


## Recorrer lista normal
# for i in range(0, len(num)):
#   total = sum(num[i + 1 :])
#    print(f"El total es {total} en la iteracion: {i}")
#    answer.append(total)
# print(answer)

## Recorrer lista al reves
for i in range(-1, len(num)):
    total = sum(num[: i + 1])
    answer.append(total)
print(answer)


# print(f"la suma de los numeros de la lista al reves son: {total}")

# linked lists

num2 = [5, 6, 9]
num3 = [7, 4, 5]

linked_list = [num, num2, num3]


# To access to the content of the linked lists

linked_list[1]

# print(linked_list[1][1])
