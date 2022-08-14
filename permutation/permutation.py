def permutations(word):
    # word = list(word)
    if len(word) == 1:
        return [word]
    # recursive call
    perms = permutations(word[1:])
    char = word[0]
    result = []
    for perm in perms:
        for i in range(len(perm) + 1):
            # list_temp = [perm[:i], char, perm[i:]]
            result.append(perm[:i] + char + perm[i:])

    return result


if __name__ == "__main__":
    # list1 = ['1', '2', '3']
    print(permutations("abc"))
