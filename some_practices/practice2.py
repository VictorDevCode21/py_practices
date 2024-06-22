list1 = [1, 2, 4]
list2 = [1, 3, 4]


def lista_combinada(list1, list2):
    combined_list = []
    sorted_list = []

    combined_list = list1 + list2
    n = len(combined_list)

    for i in range(n):
        for j in range(n - 1 - i):
            if combined_list[j] > combined_list[j + 1]:
                combined_list[j + 1], combined_list[j] = combined_list[j], combined_list[j + 1],
                sorted_list.append(combined_list)
    print(f"{j} se ejecuta esta vez la lista: {combined_list}")


lista_combinada(list1, list2)
