class Solution(object):
    def isSubsequence(self, s, t):
        
        ptrn_ptr = 0
        #EARLY EXITS
        if len(s) == 0:
            return True
        if len(t) == 0:
            return False

        #INCREMENT PATTERN POINTER ON EVERY EQUAL OCCURENCE
        for i in range(len(t)):
            if s[ptrn_ptr] == t[i]:
                ptrn_ptr += 1
                if ptrn_ptr == len(s):
                    return True
                    
        return False
