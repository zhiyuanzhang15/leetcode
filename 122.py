# 122. 买卖股票的最佳时机 II
# 中等
# 给你一个整数数组 prices ，其中 prices[i] 表示某支股票第 i 天的价格。
# 在每一天，你可以决定是否购买和/或出售股票。你在任何时候 最多 只能持有 一股 股票。
# 你也可以先购买，然后在 同一天 出售。
# 返回 你能获得的 最大 利润 。

def maxProfit(prices):
    profit = 0
    profit_lis = [0] * len(prices)
    for i in range(1,len(prices)):
        profit_lis[i] = prices[i] - prices[i-1]
    for i in range(len(profit_lis)):
        profit = max(profit,profit + profit_lis[i])
    return profit

prices = [7,1,5,3,6,4]
print(maxProfit(prices))