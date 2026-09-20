class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit = 0
        possible_buys = [prices[0]]

        for i in range(1, len(prices)):
            profit = prices[i] - min(possible_buys)

            if profit > 0 and profit > max_profit:
                max_profit = profit
            

            possible_buys.append(prices[i])

        return max_profit