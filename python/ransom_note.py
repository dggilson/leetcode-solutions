class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        hshmp = {}
        val = 0
        #since magazine > ransomnote, it would be optimal to add the note
        # to the map first, then do the comparison to the magazine since len(r) <len(m)
        for i, char in enumerate(magazine):
            if char in hshmp:
                #updates value in map on hit
                val = hshmp[char]
                val += 1
                hshmp[char] = val
            else:
                hshmp[char] = 1
        j = 0
        for i, char in enumerate(ransomNote):
            if char in hshmp:
                #updates value in map on hit
                val = hshmp[char]
                val -= 1
                hshmp[char] = val
                if val <= 0:
                    hshmp.pop(char, None)
                j += 1
        return j == len(ransomNote)