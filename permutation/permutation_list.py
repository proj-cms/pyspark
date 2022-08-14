def permute_list(nums):
    result = []

    if len(nums) == 1:
        return [nums.copy()]

    for i in range(len(nums)):
        n = nums.pop(0)
        # split the list leaving the first element and then make recursive call
        perms = permute_list(nums)

        # what ever result is obtained iterate over it
        for perm in perms:
            perm.append(n)

        result.extend(perms)
        nums.append(n)

    return result


if __name__ == "__main__":
    list1 = ['1', '2', '3']
    print(permute_list(list1))
