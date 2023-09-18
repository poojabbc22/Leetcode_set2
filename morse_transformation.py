
def unique_morse_transformations(words):
    morse_code = [
        ".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---",
        "-.-", ".-..", "--", "-.", "---", ".--.", "--.-", ".-.", "...", "-",
        "..-", "...-", ".--", "-..-", "-.--", "--.."
    ]

    transformations = set()

    for word in words:
        transformation = ''.join(morse_code[ord(c) - ord('a')] for c in word)
        transformations.add(transformation)

    return len(transformations)


# Test cases
words1 = ["gin", "zen", "gig", "msg"]
print(unique_morse_transformations(words1))  # Output: 2

words2 = ["a"]
print(unique_morse_transformations(words2))  # Output: 1