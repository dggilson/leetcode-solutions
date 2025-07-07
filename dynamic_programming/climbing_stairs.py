class Solution(object):
    def climbStairs(self, n):
        #THIS ANSWER IS NOT MY OWN, first time learning DP
        if n<=2:
            return n
        #ways to reach step 1 and 2
        first = 1
        second = 2
        for i in range(3, n+1):
            #bottom up running sup
            third = first + second
            first = second
            second = third
        return second
        