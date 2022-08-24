def power(A):
    true = 0
    if A % 8 == 0:
        true = 1
    elif A == 2 or A == 4:
        true = 1

    return true


if __name__ == "__main__":
    print(power(128))
