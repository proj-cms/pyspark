def merge_sort(arr):

    # this check and return is important else  the method goes in endless recursion
    if len(arr) <= 1:
        return arr

    n = len(arr)

    left = merge_sort(arr[:n//2]) # the // operator will give an integer
    right = merge_sort(arr[n//2:]) # recursion call

    i, j = 0, 0
    result = []

    # merging logic
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1

    if i < len(left):
        result += left[i:]
    if j < len(right):
        result += right[j:]

    return result


if __name__ == "__main__":
    arr = [2, 3, 5, 6, 1, 8]
    print(merge_sort(arr))
