class Solution(object):
    def plusOne(self, digits):

        i = len(digits) - 1
        digits[i] += 1
        while i >= 0:
            if digits[i] >= 10:
                digits[i] -= 10
                if i-1 > -1:
                    digits[i-1] +=1
                else:
                    digits.insert(0,1)
                i -= 1
            else:
                break

        return digits
            