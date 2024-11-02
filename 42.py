# 42. 接雨水
# 困难
# 给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，
# 计算按此排列的柱子，下雨之后能接多少雨水。
def trap(height):
    left = 0
    right = len(height) - 1
    left_max, right_max = 0, 0
    water = 0
    while left < right:
        if height[left] < height[right]:
            if height[left] >= left_max:
                left_max = height[left]
            else:
                water += left_max - height[left]
            left += 1
        else:
            if height[right] >= right_max:
                right_max = height[right]
            else:
                water += right_max - height[right]
            right -= 1
    return water

height = [0,1,0,2,1,0,1,3,2,1,2,1]
print(trap(height))
