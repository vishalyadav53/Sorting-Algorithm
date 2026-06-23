'''Product of Array Except Self

Given an integer array nums, return an array answer such that answer[i] is equal to
the product of all the elements of nums except nums[i].
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
You must write an algorithm that runs in O(n) time and without using the division operation.

 Input: nums = [1,2,3,4]
Output: [24,12,8,6]'''

def productExceptSelf(nums):
        product=1
        count=0
        for n in nums:
            if (n!=0):
                product*=n
            else:
                count+=1
        if (count>1):
            return [0] * len(nums)
        for i in range(0,len(nums)):
            if (count==0):
                nums[i]=product//nums[i]
            else:
                if (nums[i]!=0):
                    nums[i]=0
                else:
                    nums[i]=product
        return nums
nums=[1,2,3,4]
print(productExceptSelf(nums))
        