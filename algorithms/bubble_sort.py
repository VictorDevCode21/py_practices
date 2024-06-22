nums = [1, 3, 7, 3, 1, 20, 3, 8, 12, 25, 24, 15, 68, 95, 42, 35, 64]

n= len(nums)


# Bubble sort

for i in range(n - 1):
    for j in range(n-1-i):
        if nums[j] > nums[j+1]:
            nums[j], nums[j+1] = nums[j+1], nums[j]
print(nums)

# Reverse Bubble Sort

# for i in range(n):
#     for j in range(n - 1 - i):
#         if nums[j] < nums[j + 1]:
#             nums[j], nums[j + 1] = nums[j + 1], nums[j]
# print(nums)

