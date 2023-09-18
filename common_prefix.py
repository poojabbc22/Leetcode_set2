def prefix(nums: list[str]) -> str:
    if not nums:
        return ""

    n = len(nums)
    common_prefix = ""

    for i in range(len(nums[0])):
        char = nums[0][i]
        for word in nums[1:]:
            if i >= len(word) or word[i] != char:
                return common_prefix
        common_prefix += char

    return common_prefix


nums = ["raki","rat","rash"]
print(prefix(nums))