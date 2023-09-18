def lastlen(s: str) -> int:
    count = 0
    i = len(s) - 1  # Start from the last character of the string

    # Ignore any trailing spaces at the end of the string
    while i >= 0 and s[i] == " ":
        i -= 1

    # Count the characters of the last word until a space is encountered
    while i >= 0 and s[i] != " ":
        count += 1
        i -= 1

    return count
s = " my name is ahmargadyal"
result = lastlen(s)
print(result)
