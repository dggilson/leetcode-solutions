class Solution(object):
    def maxProfit(self, prices):
        max_prft = 0
        left = 0
        right = 1
        #SLIDING WINDOW WOOHOOO!!!! I love sliding window
        while right < len(prices):
            prft = prices[right] - prices[left]
            if prft > max_prft:
                max_prft = prices[right] - prices[left]
            #this means we have to update our left value
            elif prft < 0:
                #since we have tested every other value < right, we are okay to jump here
                left = right
            right += 1
        return max_prft