class Solution:
    # cant sort->nlogn 
    # Some sort of consecutive structure? 
    # On seen:
    # Auto handles duplicates
    #     - Hash[value] = index
    # After loop:
    #     Check value, then check if its neighbor is in the map
    #     If not, remove from map
    def longestConsecutive(self, nums: List[int]) -> int:
        #edge
        if len(nums) == 0 or len(nums) == 1:
            return len(nums)
        map = {}
        #O(n)
        for i in range(len(nums)):
            map[nums[i]] = i
        m_count = 1
        for key in list(map.keys()):
            high = low = key
            count = 1
            if key in map:
                del map[key]
            while (high + 1) in map:
                del map[high+1]
                count += 1
                high += 1
            while (low - 1) in map:
                del map[low - 1]
                count += 1
                low -= 1
            m_count = max(count, m_count)
        return m_count
        
         