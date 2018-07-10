'''
Given an array of size n, find the majority element. The majority element is the element that appears more than ⌊ n/2 ⌋ times.

You may assume that the array is non-empty and the majority element always exist in the array.

Example 1:

Input: [3,2,3]
Output: 3

'''


class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dp = {}
        l = len(nums)/2
        for num in nums:
            dp[num] = dp[num] + 1 if num in dp else 1
            if(dp[num] > l):
                return num;
                
        
