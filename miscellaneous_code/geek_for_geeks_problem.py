# User function Template for python3
query = [0] * (10001)
flag = False


def pre():
    query[1] = 1
    for i in range(2, 10001):
        if query[i] == 0:
            for j in range(2 * i, 10001, i):
                query[j] += i  # as i is the prime factor of j so it is added in it
    query[2] = 2
    for i in range(3, 10001, 2):
        if query[i] == 0:
            query[i] = i  # those numbers who are itself prime are marked by themselves
    for i in range(2, 10001):
        query[i] += query[i - 1]


class Solution:
    def sumOfAll(self, l, r):
        global flag
        if not flag:  # if pre is not yet being called we will call it once
            pre()
            flag = True  # marked flag true as pre is now called
        # query[i] represent sum of all factors of all numbers from 1 to ith number
        return query[r] - query[l - 1]


if __name__ == "__main__":
    s = Solution()
    print(s.sumOfAll(5, 6))
