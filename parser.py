def parse(s: str, start: int = 0):
    tor = []
    i = start

    while i < len(s):
        char = s[i]

        if char == '{':
            _ret, end_index = parse(s, i + 1)
            tor.append(_ret)
            i = end_index
        elif char == '}':
            return tor, i
        else:
            tor.append(char)
        i += 1
    return tor, i