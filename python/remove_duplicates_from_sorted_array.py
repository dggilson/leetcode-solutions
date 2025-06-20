class Solution(object):
    def removeDuplicates(self, nums):
        seen_set = set()
        free_space = []
        #number of unique elements
        k = 0
        for i, num in enumerate(nums):
            old_set_length = len(seen_set)
            seen_set.add(num)
            #if the number already exists, mark this index as free space
            if old_set_length == len(seen_set):
                free_space.append(i)
            else:
                #if unique is found and free space is available: place this number there
                if len(free_space) != 0:
                    nums[free_space.pop(0)] = num
                    #and mark space as free for next unique
                    free_space.append(i)
                k += 1
        return k