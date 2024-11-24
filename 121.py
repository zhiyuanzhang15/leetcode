# 121. 买卖股票的最佳时机
# 简单
# 给定一个数组 prices ，它的第 i 个元素 prices[i] 表示一支给定股票第 i 天的价格。
# 你只能选择 某一天 买入这只股票，并选择在 未来的某一个不同的日子 卖出该股票。
# 设计一个算法来计算你所能获取的最大利润。
# 返回你可以从这笔交易中获取的最大利润。如果你不能获取任何利润，返回 0 。

def maxProfit(prices):
    min_price = float('inf')
    max_profit = 0

    for price in prices:
        min_price = min(min_price, price)
        max_profit = max(max_profit, price - min_price)
    return max_profit

# 示例使用
prices = [7, 1, 5, 3, 6, 4]
print(maxProfit(prices))  # 输出: 5

prices = [7, 6, 4, 3, 1]
print(maxProfit(prices))  # 输出: 0