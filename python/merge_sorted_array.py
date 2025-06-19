class Solution(object):
    def merge(self, nums1, m, nums2, n):
        #I chose to write from the end since we were given space there. If this wasnt in place, i woudlve opted for a temporay array.
        i = m - 1
        j = n - 1

        #since this has to be in-place we hae to write to the same array
        write_ptr = m + n -1
        
        #while nums2 still has items to be checked
        while j >= 0:
            #if nums1 still has items and nums1[i] >= nums2[j] then write this item at the next spot
            if i >= 0 and nums1[i] >= nums2[j]:
                nums1[write_ptr] = nums1[i]
                i -= 1
            else:
                #if nums1 is out of items or the current item is smaller, write nums2[i]
                nums1[write_ptr] = nums2[j]
                j -= 1
            write_ptr -= 1