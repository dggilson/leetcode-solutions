class Solution(object):
    def rotate(self, nums, k):
        k = k % len(nums)
        #modulo arithmetic: if k is greater than n, k will be the apparent number of indexes to jump. This takes advatange of the fact that when k = len(nums), the array does not appeart to change.
        #creates array with 0's
        rotated = [0] * len(nums)
        
        for i in range(len(nums)):
            # when i + K is greater than length, modulo returns a value that falls into range
            #modulo is the way for cyclic movements
            # 6 % 7 = 6 because 6 < 7. 7 % 6 returns 1 because when 6 goes into 7, 1 remains
            # 7 % 7 = 0, no remainder
            #9 % 7 = 2, because 2 remains
            rotated[(i + k) % len(nums)] = nums[i]
        
        for i in range(len(nums)):
            nums[i] = rotated[i]