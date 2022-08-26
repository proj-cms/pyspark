def is_palindrome(a):
    return a == a[::-1]


def compare(left, right):
    for l, r in zip(left, right):  # tuple unpacking
        if l > r:
            return 1
        elif l < r:
            return -1
        else:
            continue

    return 0


class Solution:
    # @param A : string
    # @return a strings

    def add_1(self, x):
        return str(int(x) + 1)

    def handle_odd(self, a):
        n = len(a)
        mid = n // 2
        left = a[:mid]
        right = a[mid + 1:]

        if compare(left[::-1], right) == 1:
            # if left half is greater than right then simply append : left + mid + rev(left)
            return left + a[mid] + left[::-1]
        else:
            # if left is not greater than right then
            # concat - left + mid
            # add one to left
            # reverse left
            # then concat
            left = left + a[mid]
            left = self.add_1(left)

            return left + left[::-1][1:]

    def handle_even(self, a):
        # even will have equal split so no concept of special mid
        n = len(a)
        mid = n // 2
        left = a[:mid]
        right = a[mid:]
        print(f'left :{left} right:{right}')

        if compare(left[::-1], right) == 1:
            return left + left[::-1]
        else:
            left = self.add_1(left)
            return left + left[::-1]

    def solve(self, A):
        if is_palindrome(A):
            print('entering palindrome check at beginning')
            A = self.add_1(A)

        if is_palindrome(A):
            return A

        n = len(A)

        if n & 1:
            return self.handle_odd(A)
        else:
            return self.handle_even(A)


if __name__ == "__main__":
    sol = Solution()
    print(sol.solve('1001'))
