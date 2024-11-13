# 48. 旋转图像
# 中等
# 给定一个 n × n 的二维矩阵 matrix 表示一个图像。
# 请你将图像顺时针旋转 90 度
# 你必须在 原地 旋转图像，这意味着你需要直接修改输入的二维矩阵。
# 请不要 使用另一个矩阵来旋转图像。

def rotate(matrix):
    n = len(matrix)

    for i in range(n):
        for j in range(i + 1, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for i in range(n):
        matrix[i].reverse()

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
rotate(matrix)
print(matrix)