import re
class Solution(object):
    def isPalindrome(self, s):
        s = s.lower()
        #regex that removes all non-alphanumeric characters with OR'd together the underscore
        s = re.sub(r'\W+|_', '', s)
        if len(s) < 1:
            return True
        front = 0
        back = len(s) - 1

        #compares front and back pointer
        while front < back:
            if s[front] != s[back]:
                return False
            front += 1
            back -= 1
            
        return True