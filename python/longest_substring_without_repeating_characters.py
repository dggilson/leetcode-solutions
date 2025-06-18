class Solution(object):
    def lengthOfLongestSubstring(self, s):
        #pointers for sliding window
        left = 0
        right = 0
        
        #hashmap that will contain chars in the string as keys and their related index as values
        char_hashmap = {}
        count = 0
        max_substring = 0
        
        #early exit for single char strings
        if len(s) == 1:
            return 1
        
        #Sliding window
        while right < len(s):
            #if the char at the right side of the window is in the map and in the window
            if s[right] in char_hashmap and char_hashmap[s[right]] >= left:
                max_substring = max(max_substring, count)
                #update left pointer to the next index after the first occurence of dupliecate charå
                count -= char_hashmap[s[right]] - left
                left = char_hashmap[s[right]] + 1
                char_hashmap[s[right]] = right
                right += 1
            else:
                #Normal case where each value that is added to the window is new to the hashmap
                char_hashmap[s[right]] = right
                count += 1
                max_substring = max(max_substring, count)
                right += 1
                
        return max_substring
        
    