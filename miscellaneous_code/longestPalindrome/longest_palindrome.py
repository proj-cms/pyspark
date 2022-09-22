def expandFromCenter(s, left, right):
    if s is None or len(s) == 1:
        return s

    while left >= 0 and right < len(s) and s[left] == s[right]:
        left -= 1
        right += 1

    return right - left - 1


def callExpandFromCenter(s):
    if s is None or len(s) == 1:
        return s

    start = 0
    end = 0

    for i in range(len(s)):
        # odd length case
        len1 = expandFromCenter(s, i, i)

        # even length case
        len2 = expandFromCenter(s, i, i + 1)
        len3 = max(len1, len2)

        if len3 > (end - start):
            start = i - (len3 - 1) // 2
            end = i + len3 // 2

    return s[start:end + 1]


# Program time complexity - O(n2)
# it can be coded with complex Manacher's algo for O(n) time complexity
if __name__ == "__main__":
    s = "abbbbbba"
    print(callExpandFromCenter(s))
