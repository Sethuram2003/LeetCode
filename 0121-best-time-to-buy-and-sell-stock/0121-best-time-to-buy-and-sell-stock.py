class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        buy_num=prices[0]
        profit=0

        for i in range(1,len(prices)):
            cost=prices[i]-buy_num
            profit=max(cost,profit)
            buy_num=min(buy_num,prices[i])
        return profit


        