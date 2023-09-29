import sys


def binary(n: int):
    if n < 1:
        print(A)
    else:
        A[n - 1] = 0
        binary(n - 1)
        A[n - 1] = 1
        binary(n - 1)


if __name__ == "__main__":
    print('Python %s on %s' % (sys.version, sys.platform))
    A = [1, 2, 3, 4]
    binary(3)
