class Solution(object):
     def removeDuplicates(self, nums):
        write_ptr = 2
        #early exit since no chance of >3 duplicates
        if len(nums) <= 2:
            return 2
        for i in range(2, len(nums)):
            #if the current value does not match the one 2 positions down:
            if nums[i] != nums[write_ptr - 2]:
                #we write
                nums[write_ptr] = nums[i]
                write_ptr += 1
            #else proceed through
        return write_ptr
        #note: i and write_ptr are differnt since we are scanning and placing in-place