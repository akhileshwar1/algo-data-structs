import math
import os
import random
import re
import sys

#
# Complete the 'superDigit' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. STRING n
#  2. INTEGER k
#


def superDigit(n, k):
    # Write your code here
    p = get_p(n, k)
    print(p)
    def super(p):
        if(p < 10):
            return p
        else:
            return p % 10 + super(p // 10)

    p = super(p)
    def digit(p):
        if(p < 10):
            return p
        else:
            sum = super(p)
            return digit(sum)
    return digit(p)

def get_p(n, k):
    add = n
    for i in range(1, k):
        n = n + add
    return int(n)


if(__name__ == '__main__'):
    # fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = first_multiple_input[0]

    k = int(first_multiple_input[1])

    result = superDigit(n, k)
    print(result)

    # fptr.write(str(result) + '\n')

    # fptr.close()
