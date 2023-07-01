def solve(A, B, C):
    waterLeftToPass = A - B
    sumTapSize = sum(C)
    sumWaterPassed = 0
    for i in range(len(C) - 1):  # -2 since last tap is confirmed to release
        sumWaterPassed = sumWaterPassed +  ( (C[i] * A) / sumTapSize )
        waterPAssed = (C[i] * A) / sumTapSize
        print(f'waterPassed : {waterPAssed} by tap : {i} ')
        print(f'sumWaterPassed : {sumWaterPassed} waterLeftToPass : {waterLeftToPass}')
        if sumWaterPassed >= waterLeftToPass:
            # taps after this needs to be closed
            return (len(C) - 1) - i

    return 0


if __name__ == "__main__":
    A = 373
    B = 348
    C = [50, 32, 39, 50, 67, 6, 30, 14, 66, 97, 79, 21, 6, 82, 19, 53, 34, 55, 97, 33, 57, 6, 22, 46, 88, 29, 44, 88, 44, 74, 16, 62, 15, 93, 19]
    print (f'length of C : {len(C)}')
    print(solve(A, B, C))
