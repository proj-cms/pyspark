import statistics
from typing import List


def getBalancingElement(A: List[int]) -> int:
    return statistics.median(A)


def getOptimalArray(A: List[int]) -> List[int]:
    balancingElement = getBalancingElement(A)
    return [balancingElement] * len(A)


def calcOptimalArrayStep(A: List[int], B: List[int]):
    sum_ = 0
    for l, r in zip(A, B):
        sum_ += abs(l - r)

    return sum_


if __name__ == '__main__':
    A = [1, 6, 9, 12]
    # A = [1, 1, 1, 7, 7, 10, 19]
    finalArray = [0]
    for i in range(2, len(A) + 1):
        B = getOptimalArray(A[0:i])
        val = int(calcOptimalArrayStep(A[0:i], B))
        # finalArray.append(finalArray[len(finalArray)-1] + val)
        finalArray.append(val)

    print(finalArray)
