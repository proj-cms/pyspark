# try this code on python tutor for visibility
# this code works on string as well as on lists.

def permutations(s, empty=''):
    if len(s) == 0:
        print(empty)  # not S but the string 'empty' is bein printed

    for i in range(len(s)):
        newEmptyString = empty + s[i]
        newString = s[0:i] + s[i + 1:]
        permutations(newString, newEmptyString)


if __name__ == "__main__":
    permutations(['1', '2', '3'])
    permutations('ABC')
