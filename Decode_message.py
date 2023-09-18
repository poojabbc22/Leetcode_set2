def decodeMessage( key: str, message: str) -> str:
    substitution_table = {}
    next_substitute = 'a'

    for char in key:
        if char != ' ' and char not in substitution_table:
            substitution_table[char] = next_substitute
            next_substitute = chr(ord(next_substitute) + 1)

    decoded_message = ""
    for char in message:
        if char == ' ':
            decoded_message += char
        else:
            decoded_message += substitution_table[char]

    return decoded_message
key = "the quick brown fox jumps over the lazy dog"
message = "vkbs bs t suepuv"
res=decodeMessage(key,message)
print(res)