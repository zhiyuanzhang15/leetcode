# 84. 柱状图中最大的矩形
# 困难
# 给定 n 个非负整数，用来表示柱状图中各个柱子的高度。每个柱子彼此相邻，且宽度为 1 。
# 求在该柱状图中，能够勾勒出来的矩形的最大面积。
def largest_rectangle_area(heights):
    stack = []
    max_area = 0
    heights.append(0)  # 添加一个高度为0的柱子，确保最后能计算所有柱子的面积

    for i in range(len(heights)):
        while stack and heights[i] < heights[stack[-1]]:
            h = heights[stack.pop()]
            w = i if not stack else i - stack[-1] - 1
            max_area = max(max_area, h * w)
        stack.append(i)

    return max_area

heights = [2,1,5,6,2,3]
print(largest_rectangle_area(heights))  # 输出 10