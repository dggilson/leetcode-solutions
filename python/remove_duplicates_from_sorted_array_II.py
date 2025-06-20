class Solution(object):
    def removeDuplicates(self, nums):
        free_space = []
        frequency_hshmp = {}
        k = 0
        for i, num in enumerate(nums):
            #if number has been added and it's only been seen once: update it to 2
            if num in frequency_hshmp:
                num_count = frequency_hshmp.get(num)
                if num_count != 2:
                    num_count = 2
                    frequency_hshmp[num] = num_count
                    #if free space exists: we place there
                    if len(free_space) != 0:
                        nums[free_space.pop(0)] = num
                        free_space.append(i)
                    k += 1
                else:
                    #if value is at 2: mark this as free space
                    free_space.append(i)
            else:
                #number is added to map, if free space exists, we place it there
                frequency_hshmp[num] = 1
                if len(free_space) != 0:
                    nums[free_space.pop(0)] = num
                    free_space.append(i)
                k += 1
        return k