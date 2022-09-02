# try this code on python tutor for visibility

def permutations(s, empty=''):
    if len(s) == 0:
        print(empty)

    for i in range(len(s)):
        newEmptyString = empty + s[i]
        newString = s[0:i] + s[i + 1:]
        permutations(newString, newEmptyString)


if __name__ == "__main__":
    permutations('ABC')
