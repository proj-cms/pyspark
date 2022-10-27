from typing import List


def firstMissingPositiveII(arr: List[int]) -> int:
    n = len(arr)
    for i in range(0, len(arr)):
        val = arr[i]
        if 1 <= val < n:
            chair = val - 1
            if arr[i] != arr[chair]:
                arr[chair], arr[i] = arr[i], arr[chair]
                i = i - 1

    for i in range(0, len(arr)):
        if i + 1 != arr[i]:
            return i + 1

    return len(arr) + 1


if __name__ == "__main__":
    # A = [3,-3,6,3]
    # A = [1, 2, 3]
    # A = [-3, -5, 0]
    A = [100, 200, 300]
    print(firstMissingPositiveII(A))
