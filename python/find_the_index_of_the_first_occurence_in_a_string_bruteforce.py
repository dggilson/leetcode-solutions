class Solution(object):
    def strStr(self, haystack, needle):
        j = 0
        i = 0
        if len(needle) == 0:
            return 0
    
        #brute force
        while i < len(haystack):
            ndle_indx = 0
            j = i
            #once we get a hit note last condition, we compare at this index
            while j < len(haystack) and ndle_indx < len(needle) and haystack[j] == needle[ndle_indx]:
                j += 1
                ndle_indx += 1
            #if we found the pattern here we return
            if ndle_indx == len(needle):
                return i
            i += 1
        return -1 
                        
