# 152. 乘积最大子数组
# 中等
# 给你一个整数数组 nums ，请你找出数组中乘积最大的非空连续 
# 子数组
# （该子数组中至少包含一个数字），并返回该子数组所对应的乘积。
# 测试用例的答案是一个 32-位 整数。

def maxProduct(nums):
    if not nums:
        return 0
    
    max_product = nums[0]
    min_product = nums[0]
    result = nums[0]

    for i in range(1, len(nums)):
        if nums[i] < 0:
            max_product, min_product = min_product, max_product
        max_product = max(nums[i], nums[i] * max_product)
        min_product = min(nums[i], nums[i] * min_product)
        result = max(result, max_product)
    return result

# 示例使用
nums = [2, 3, -2, 4]
print(maxProduct(nums))  # 输出: 6

nums = [-2, 0, -1]
print(maxProduct(nums))  # 输出: 0