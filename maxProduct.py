'''152. Maximum Product Subarray

Given an integer array nums, find a subarray that has the largest product, and return the product.
The test cases are generated so that the answer will fit in a 32-bit integer.
Note that the product of an array with a single element is the value of that element.

Input: nums = [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.

Input: nums = [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.'''

def maxProduct(nums):
        product=nums[0]
        curr_max=nums[0]
        curr_min=nums[0]

        for i in range(1,len(nums)):
            temp=curr_max
            curr_max =max(nums[i],nums[i]*temp,nums[i]*curr_min)
            curr_min =min(nums[i],nums[i]*temp,nums[i]*curr_min)
            # //product=max(product,max) 
            if(curr_max>product):
                product=curr_max
        return product
nums=[2,3,-2,4]
print(maxProduct(nums))


        