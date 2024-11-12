# 6. Z 字形变换
# 中等
# 将一个给定字符串 s 根据给定的行数 numRows ，
# 以从上往下、从左到右进行 Z 字形排列。
# 比如输入字符串为 "PAYPALISHIRING" 行数为 3 时，排列如下：
# P   A   H   N
# A P L S I I G
# Y   I   R
# 之后，你的输出需要从左往右逐行读取，产生出一个新的字符串，
# 比如："PAHNAPLSIIGYIR"。

def convert(s, numRows):
    if numRows == 1 or numRows >= len(s):
        return s
    
    rows = [''] * numRows
    current_row = 0
    going_down = False

    for char in s:
        rows[current_row] += char
        if current_row == 0 or current_row == numRows - 1:
            going_down = not going_down
        current_row += 1 if going_down else -1
    return ''.join(rows)

# 示例使用
s = "PAYPALISHIRING"
numRows = 3
print(convert(s, numRows)) 