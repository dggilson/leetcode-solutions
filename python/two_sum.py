class Solution(object):
    def twoSum(self, nums, target):
        map = {}
        if len(nums) == 2:
            return [0,1]
        #pretty fun one, first problem that i thought of the clever solution
        for i in range(len(nums)):
            if target-nums[i] in map:
                return [i, map[target-nums[i]]]
            map[nums[i]] = i