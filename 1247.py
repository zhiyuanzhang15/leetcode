# 1247. 交换字符使得字符串相同
# 中等
# 有两个长度相同的字符串 s1 和 s2，且它们其中 只含有 字符 "x" 和 "y"，
# 你需要通过「交换字符」的方式使这两个字符串相同。
# 每次「交换字符」的时候，你都可以在两个字符串中各选一个字符进行交换。
# 交换只能发生在两个不同的字符串之间，绝对不能发生在同一个字符串内部。
# 也就是说，我们可以交换 s1[i] 和 s2[j]，但不能交换 s1[i] 和 s1[j]。
# 最后，请你返回使 s1 和 s2 相同的最小交换次数，如果没有方法能够使得这两个字符串相同，则返回 -1 。

def minimumSwap(s1, s2):
    if len(s1) != len(s2):
        return -1
    
    xy = yx = 0

    for a, b in zip(s1, s2):
        if a == 'x' and b == 'y':
            xy += 1
        elif a == 'y' and b == 'x':
            yx += 1
    
    if (xy + yx) % 2 != 0:
        return -1
    return xy // 2 + yx // 2 + 2 * (xy % 2)

# 示例使用
s1 = "xx"
s2 = "yy"
print(minimumSwap(s1, s2))  # 输出: 1

s1 = "xy"
s2 = "yx"
print(minimumSwap(s1, s2))  # 输出: 2

s1 = "xx"
s2 = "xy"
print(minimumSwap(s1, s2))  # 输出: -1