'''53. Maximum Subarray
Given an integer array nums, find the subarray with the largest sum, and return its sum.

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.
'''

def maxSubArray( nums):
        maxSum = nums[0]
        currentSum = nums[0]
        

        for i in range(1, len(nums)):
            currentSum = max(nums[i], currentSum + nums[i])

            if currentSum > maxSum:
                maxSum = currentSum

        return maxSum
nums=[-2,1,-3,4,-1,2,1,-5,4]
print(maxSubArray(nums))
        
