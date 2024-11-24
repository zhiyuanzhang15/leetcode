# 136. 只出现一次的数字
# 简单
# 给你一个 非空 整数数组 nums ，除了某个元素只出现一次以外，
# 其余每个元素均出现两次。找出那个只出现了一次的元素。
# 你必须设计并实现线性时间复杂度的算法来解决此问题，
# 且该算法只使用常量额外空间。

def singleNumber(nums):
    result = 0
    for num in nums:
        result ^= num
    return result

# 示例使用
nums = [2, 2, 1]
print(singleNumber(nums))  # 输出: 1

nums = [4, 1, 2, 1, 2]
print(singleNumber(nums))  # 输出: 4