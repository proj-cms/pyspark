from typing import List


def singleNonDuplicate(nums: List[int], dbg: int) -> int:
    # initialize the left and right pointer
    l, r = 0, len(nums) - 1

    # the binary search condition
    # print (f'l : {l} r:{r}')
    while l <= r:  # continue the loop till left pointer does not cross the right
        # compute the mid
        print(f'l : {l} r:{r}') if dbg == 1 else None
        m = l + ((r - l) // 2)
        print(f'm : {m}') if dbg == 1 else 0
        print(f'nums[{m} - 1] : {nums[m - 1]}  nums[{m}] : {nums[m]}') if dbg == 1 else 0
        print(f'nums[{m} + 1] : {nums[m + 1]}  nums[{m}] : {nums[m]}') if dbg == 1 else 0
        if (m - 1 < 0 or nums[m - 1] != nums[m]) and \
                (m + 1 == len(nums) or nums[m] != nums[m + 1]):
            return nums[m]

        # calculate the leftSize if the leftSie is odd then  leftSide has odd and we should search leftSide

        leftSize = m - 1 if nums[m - 1] == nums[m] else m
        print(f'leftSize : {leftSize}') if dbg == 1 else 0
        print(leftSize % 2) if dbg == 1 else 0
        if leftSize % 2:
            r = m - 1
        else:
            l = m + 1


if __name__ == "__main__":
    A = [1, 1, 2, 3, 3, 4, 4]
    print(singleNonDuplicate(A, 0))
