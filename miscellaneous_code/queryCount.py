from typing import List


class Solution:
    def solveQueries(self, N: int, num: int, A: List[int], Q: List[List[int]]) -> List[int]:
        # code here
        # N = number of elements in A
        # A = list of elements in which frequency has to be counted
        # Q = list of queries having queries equal to num , lis of list

        # initialize empty list to store the result
        numList = []
        freqCnt = 0

        # iterate over the Q
        # num is the size of Q
        for queryIndex in range(num):
            queryToInterate = Q[queryIndex]  # it will yeild a list

            # initialize L,R,K
            L = queryToInterate[0]
            R = queryToInterate[1]
            K = queryToInterate[2]

            # now iterate for i items such that L <= i <= R
            # initialize numCnt for loop of i
            numCnt = 0
            for i in range(L, R + 1):
                freqCnt = A[i:N].count(A[i])  # N is the count of elements in A
                if (freqCnt == K):
                    numCnt += 1

            numList.append(numCnt)

        return numList
