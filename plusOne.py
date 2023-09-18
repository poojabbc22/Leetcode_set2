def plusOne(digits: list[int]) -> list[int]:
    n = len(digits)

    # Traverse the digits in reverse order
    for i in range(n - 1, -1, -1):
        if digits[i] == 9:
            digits[i] = 0
        else:
            digits[i] += 1
            return digits


    return [1] + digits
digits=[8,9]
res=plusOne(digits)
print(res)
