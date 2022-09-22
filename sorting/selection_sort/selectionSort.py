def selectionSort(arr):
    for i in range(len(arr) - 1):
        current_min_index = i

        for j in range(i, len(arr) - 1): # start J from I till end
            if arr[j] < arr[current_min_index]:
                current_min_index = j  # relocate the minimum index since the current jth element is lesser than
                # current assumed min

        if i != current_min_index:
            arr[i], arr[current_min_index] = arr[current_min_index], arr[i]

    return arr


if __name__ == "__main__":
    arr = [2,3,5,6,1,8]
    print (selectionSort(arr))
