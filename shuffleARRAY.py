def shuffle(nums: list[int], n: int) -> list[int]:
    shuffledarray = []
    for i in range(0, n):
        shuffledarray.append(nums[i])
        shuffledarray.append(nums[i + n])
    return shuffledarray
nums = [2, 4, 6, 7, 1, 9, 0]
n = 3  # You want to split the array into n parts
res = shuffle(nums, n)
print(res)