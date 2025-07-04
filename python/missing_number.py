class Solution(object):
    def missingNumber(self, nums):
        n = len(nums)
        #returns the sum of all values from n and below
        true_sum = (n*(n+1))/2
        partial_sum = 0
        for i in range(n):
            partial_sum += nums[i]
        return true_sum - partial_sum