# 123. 买卖股票的最佳时机 III
# 困难
# 给定一个数组，它的第 i 个元素是一支给定的股票在第 i 天的价格。
# 设计一个算法来计算你所能获取的最大利润。你最多可以完成 两笔 交易。
# 注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。

def maxProfit(prices):
    if not prices:
        return 0
    
    buy1, sell1 = float('-inf'), 0
    buy2, sell2 = float('-inf'), 0

    for price in prices:
        buy1 = max(buy1, -price)
        sell1 = max(sell1, buy1 + price)
        buy2 = max(buy2, sell1 - price)
        sell2 = max(sell2, buy2 + price)

    return sell2


# 示例使用
prices = [3, 3, 5, 0, 0, 3, 1, 4]
print(maxProfit(prices))  # 输出: 6

prices = [1, 2, 3, 4, 5]
print(maxProfit(prices))  # 输出: 4

prices = [7, 6, 4, 3, 1]
print(maxProfit(prices))  # 输出: 0