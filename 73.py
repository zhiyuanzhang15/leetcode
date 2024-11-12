# 73. 矩阵置零
# 中等
# 给定一个 m x n 的矩阵，如果一个元素为 0 ，
# 则将其所在行和列的所有元素都设为 0 。请使用 原地 算法

def setZeroes(matrix):
    if not matrix:
        return

    m, n = len(matrix), len(matrix[0])
    first_row_has_zero = any(matrix[0][j] == 0 for j in range(n))
    first_col_has_zero = any(matrix[i][0] == 0 for i in range(m))

    # 标记第一行和第一列
    for i in range(1, m):
        for j in range(1, n):
            if matrix[i][j] == 0:
                matrix[i][0] = 0
                matrix[0][j] = 0

    # 根据标记设置元素为 0
    for i in range(1, m):
        for j in range(1, n):
            if matrix[i][0] == 0 or matrix[0][j] == 0:
                matrix[i][j] = 0

    # 处理第一行
    if first_row_has_zero:
        for j in range(n):
            matrix[0][j] = 0

    # 处理第一列
    if first_col_has_zero:
        for i in range(m):
            matrix[i][0] = 0

# 示例使用
matrix = [
    [1, 1, 1],
    [1, 0, 1],
    [1, 1, 1]
]
setZeroes(matrix)
print(matrix)  # 输出: [[1, 0, 1], [0, 0, 0], [1, 0, 1]]