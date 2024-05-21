pairs = [2, 3, 4, 7, 3, 5]
answer = []

for i in range(len(pairs) // 2):
    j = len(pairs) - 1 - i
    sum_values = pairs[i] + pairs[j]
    answer.append(sum_values)

print(answer)
