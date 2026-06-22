'''Valid Perfect Square
Given a positive integer num, return true if num is a perfect square or false otherwise.
A perfect square is an integer that is the square of an integer. In other words, 
it is the product of some integer with itself.
You must not use any built-in library function, such as sqrt.
Example 1:
Input: num = 16
Output: true'''
def isPerfectSquare( x):
        if(x==1):
            return True
        start=1
        end=x//2
        while(start<=end):
            mid=start+(end-start)//2
            if (mid*mid==x):
                return True
            elif (mid*mid>x):
                end=mid-1
            else:
                start=mid+1
        return False
    
a=16
print(isPerfectSquare(a))
        