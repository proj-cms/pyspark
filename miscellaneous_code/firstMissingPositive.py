from typing import List


def first_missing_positive(A: List[int]) -> int:
    for i in range(len(A)):
        if A[i] < 0:
            A[i] = 0

    for i in range(len(A)):
        if 1 <= A[i] <= len(A):
            print("in second for")
            val = abs(A[i])
            print(f"i : {i} val : {val}")
            if A[val - 1] > 0:
                A[val - 1] *= -1
            elif A[val - 1] == 0:
                A[val - 1] = -1 * (len(A) + 1)

            print(A)

    for i in range(1, len(A) + 1):
        print("in 3rd for")
        if A[i - 1] >= 0:
            return i

    return len(A) + 1


if __name__ == "__main__":
    A = [3, -3, 6, 3]
    # A = [1, 2, 3]
    # A = [-3, -5, 0]
    print(first_missing_positive(A))
