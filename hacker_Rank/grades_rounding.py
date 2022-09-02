#!/bin/python3


#
# Complete the 'gradingStudents' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY grades as parameter.
#

def gradingStudents(grades):
    # Write your code here
    rounded_grade = 0
    multiple_5 = [val * 5 for val in range(1, 20)]
    return_result = []
    for grade in grades:
        # No rounding cases:
        # 1. grade < 40
        # 2. grade is exact divisible by 5 ( not specified in problem)
        # 3. if the diff between grade and next multiple is >= 3
        if grade < 40 or grade % 5 == 0 or 5 - (grade % 5) >= 3:
            return_result.append(grade)
        elif 5 - (grade % 5) < 3:  # perform rounding
            # how much it will take to reach to next 5 multiple
            rounded_grade = grade + (5 - (grade % 5))
            return_result.append(rounded_grade)
        else:
            continue

    return return_result


if __name__ == '__main__':
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    grades_count = int(input().strip())

    grades = []

    for _ in range(grades_count):
        grades_item = int(input().strip())
        grades.append(grades_item)

    result = gradingStudents(grades)
    print(result)

    # fptr.write('\n'.join(map(str, result)))
    # fptr.write('\n')
    #
    # fptr.close()
