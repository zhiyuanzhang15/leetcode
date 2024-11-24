# 70. 爬楼梯
# 简单
# 提示
# 假设你正在爬楼梯。需要 n 阶你才能到达楼顶。
# 每次你可以爬 1 或 2 个台阶。
# 你有多少种不同的方法可以爬到楼顶呢？

def climbStairs(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    
    prev1, prev2 = 2, 1
    for i in range(3, n + 1):
        curr = prev1 + prev2
        prev2 = prev1
        prev1 = curr
    return prev1

# 示例使用
n = 2
print(climbStairs(n))  # 输出: 2

n = 3
print(climbStairs(n))  # 输出: 3

n = 4
print(climbStairs(n))  # 输出: 5
