class Solution(object):
    def minSubArrayLen(self, target, nums):
        left = 0 
        right = 0
        min_len = 0
        total = 0
        #SLIDING WINDOW!!!!!!!!!!! best example thus far
        for right in range(len(nums)):
            total += nums[right]
            #move window to left and update min_len until we are below target value again
            while total >= target:
                if(min_len == 0):
                    min_len = (right-left) + 1
                else:
                    min_len = min(min_len, (right-left) + 1)
                total -= nums[left]
                left += 1           
        return min_len