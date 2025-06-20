class Solution(object):
    def removeElement(self, nums, val):
        free_indexes = []
        i = 0
        k = 0
        #iterates through every item
        for i in range(len(nums)):
            # case 1: if item matches, add it to free spaces
            if nums[i] == val:
                free_indexes.append(i)
            else:
                #if the item does not match and there is a free space,
                if len(free_indexes) != 0:
                    #get index of the free spot, place current item there.
                    free_spot = free_indexes.pop(0)
                    nums[free_spot] = nums[i]
                    #case 2: free space added when an item is swapped from original index
                    free_indexes.append(i)
                k += 1
            i += 1
        return k