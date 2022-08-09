def insertion_sort(arr):
    for i in range(1,len(arr)): # first element is alrady sorted so start from 2nd one
        index_to_insert = i
        j = i-1
        while j >= 0: # go reverse in the list till 0 th element
            if arr[j] < arr[index_to_insert]:
                break # if elements at Jth position is already min then no need to proceed in ths while loop break out

            # else swap
            arr[j], arr[index_to_insert] = arr[index_to_insert], arr[j]
            # move the index_to_isert with swap to the value the new swapped lower element has moved
            index_to_insert = j

            j -= 1
    return arr


if __name__ == "__main__":
    arr = [2,3,5,6,1,8]
    print (insertion_sort(arr))