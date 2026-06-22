'''Sqrt(x)

Given a non-negative integer x, return the square root of x rounded down to the nearest 
integer. The returned integer should be non-negative as well.You must not use any built-in exponent function or operator.
For example, do not use pow(x, 0.5) in c++ or x ** 0.5 in python.'''

def mySqrt(x):

    if x == 1:
        return 1

    start = 1
    end = x // 2

    while start <= end:

        mid = start + (end - start) // 2

        if mid * mid == x:
            return mid

        elif mid * mid > x:
            end = mid - 1

        else:
            start = mid + 1

    return end


x = 16
print(mySqrt(x))