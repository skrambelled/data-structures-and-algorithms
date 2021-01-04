def anagram(primary, secondary):
    counter = {}

    for char in primary:
        if not char.isalpha():
            continue

        char = char.lower()
        if not char in counter:
            counter[char] = 1
        else:
            counter[char] += 1


    for char in secondary:
        if not char.isalpha():
            continue

        char = char.lower()
        if not char in counter:
            return False

        counter[char] -= 1
        if not counter[char]:
            del counter[char]

    if len(counter.keys()):
        return False

    return True
