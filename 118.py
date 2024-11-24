# 118. 杨辉三角
# 简单
# 给定一个非负整数 numRows，生成「杨辉三角」的前 numRows 行。
# 在「杨辉三角」中，每个数是它左上方和右上方的数的和。

def generate(numRows):
    triangle = []

    for i in range(numRows):
        row = [1] * (i + 1)
        for j in range(1, i):
            row[j] = triangle[i - 1][j - 1] + triangle[i - 1][j]
        triangle.append(row)

    return triangle

# 示例使用
numRows = 5
print(generate(numRows))
# 输出:
# [
#  [1],
#  [1, 1],
#  [1, 2, 1],
#  [1, 3, 1],
#  [1, 4, 6, 4, 1]
# ]