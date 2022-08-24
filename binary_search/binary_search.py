def binary_search(A, B):
    A_sorted = sorted(A)

    start = 0
    end = len(A_sorted)

    while start <= end:
        mid = (start + end) // 2
        if B == A_sorted[mid]:
            return A.index(B)
        elif B < A_sorted[mid]:
            end = mid - 1
        elif B > A_sorted[mid]:
            start = mid + 1
        else:
            return -1


if __name__ == "__main__":
    A = [101, 103, 106, 109, 158, 164, 182, 187, 202, 205, 2, 3, 32, 57, 69, 74, 81, 99, 100]
    B = 202
    print(binary_search(A, B))
