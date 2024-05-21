nums = [1, 2, 1, 3, 5, 6, 4]

for i in nums:
    if nums[i] > nums[i - 1] and nums[i] > nums[i + 1]:
        print(f"The number: {nums[i]} is pico")
        break
