from typing import List


def singleNonDuplicate(nums: List[int]) -> int:
    # initialize the left and right pointer
    l, r = 0, len(nums) - 1

    # the binary search condition
    # print (f'l : {l} r:{r}')
    while l <= r:  # continue the loop till left pointer does not cross the right
        # compute the mid
        print(f'l : {l} r:{r}')
        m = l + ((r - l) // 2)
        print(f'm : {m}')
        print(f'nums[{m} - 1] : {nums[m - 1]}  nums[{m}] : {nums[m]}')
        print(f'nums[{m} + 1] : {nums[m + 1]}  nums[{m}] : {nums[m]}')
        if (m - 1 < 0 or nums[m - 1] != nums[m]) and \
                (m + 1 == len(nums) or nums[m] != nums[m + 1]):
            return nums[m]

        # calculate the leftSize if the leftSie is odd then  leftSide has odd and we should search leftSide

        leftSize = m - 1 if nums[m - 1] == nums[m] else m
        print(f'leftSize : {leftSize}')
        print(leftSize % 2)
        if leftSize % 2:
            r = m - 1
        else:
            l = m + 1


if __name__ == "__main__":
    A = [1, 1, 2, 3, 3, 4, 4]
    print(singleNonDuplicate(A))
