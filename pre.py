def remove_comments(input_string: str) -> str:
    result = []
    i = 0
    length = len(input_string)
    while i < length:
        if i + 1 < length and input_string[i:i+2] == '/*':
            i += 2
            while i + 1 < length and input_string[i:i+2] != '*/':
                i += 1
            if i + 1 < length:
                i += 2
            continue
        if i + 1 < length and input_string[i:i+2] == '//':
            i += 2
            while i < length and input_string[i] != '\n':
                i += 1
            continue
        result.append(input_string[i])
        i += 1
    return ''.join(result)