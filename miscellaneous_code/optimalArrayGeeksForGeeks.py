import math
import statistics
from typing import List


def getBalancingElement(A: List[int]) -> int:
    returnValue = 0
    if len(A) % 2 == 0:  # eve numbered
        returnValue = math.ceil((A[len(A) // 2] + A[len(A) // 2 - 1]) / 2)
    else:
        returnValue = statistics.median_low(A)

    return returnValue


def getOptimalArray(A: List[int]) -> List[int]:
    balancingElement = getBalancingElement(A)
    return [balancingElement] * len(A)


def calcOptimalArrayStep(A: List[int], B: List[int]):
    return sum(map(lambda i, j: abs(i - j), A, B))


if __name__ == '__main__':
    A = [1, 6, 9, 12]
    # A = [1, 1, 1, 7, 7, 10, 19]
    finalArray = [0]
    for i in range(2, len(A) + 1):
        B = getOptimalArray(A[0:i])
        val = calcOptimalArrayStep(A[0:i], B)
        # finalArray.append(finalArray[len(finalArray)-1] + val)
        finalArray.append(val)

    print(finalArray)
