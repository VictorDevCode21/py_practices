nums = [1, 2, 3, 4]
answer = []

for index, value in enumerate(nums, start=0):
    total = 1
    print(f"Estos son los valores de I {index + 1}")
    for j in range(len(nums)):
        if j != index:
            print(f"nums j : {nums[j]}")
            total *= nums[j]
    answer.append(total)

print(answer)
