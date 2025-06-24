class Solution(object):
    def majorityElement(self, nums):
        count = 0
        res = 0

        #Works similar to crossing out numbers
        for i, num in enumerate(nums):
            #we either have just started, or we found enough of other numbers to cancel out the first we chose
            if count == 0:
                res = num
            if res == num:
                count += 1
            #New numbers cancels out progress
            else:
                count -= 1
        return res