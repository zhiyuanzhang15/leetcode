# 739. 每日温度
# 中等
# 给定一个整数数组 temperatures ，表示每天的温度，返回一个数组 answer ，
# 其中 answer[i] 是指对于第 i 天，下一个更高温度出现在几天后。
# 如果气温在这之后都不会升高，请在该位置用 0 来代替。

def daily_temperatures(temperatures):
    answer = [0] * len(temperatures)
    stack =[]
    for i in range(len(temperatures)):
        while stack and temperatures[i] > temperatures[stack[-1]]:
            answer[stack[-1]] = i - stack[-1]
            stack.pop()
        stack.append(i)
    
    return answer

temperatures = [73,74,75,71,69,72,76,73]
print(daily_temperatures([73,74,75,71,69,72,76,73]))