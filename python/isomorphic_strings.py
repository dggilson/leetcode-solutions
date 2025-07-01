class Solution(object):
    def isIsomorphic(self, s, t):
        map = {}
        #orignal approach was brute force, creating a list for each char and doing comparison
        #runtime was 252ms :skull:
        for i in range(len(s)):
            if s[i] not in map:
                #value is already mapped
                if t[i] in map.values():
                    return False
                #maps the current char of both strings to eachother    
                map[s[i]] = t[i]
            else:
                #since s[i] is in the map, we want to make sure that they have the same value
                if map[s[i]] != t[i]:
                    return False
        return True