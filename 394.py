# 394. 字符串解码
# 中等
# 给定一个经过编码的字符串，返回它解码后的字符串。
# 编码规则为: k[encoded_string]，表示其中方括号内部的 encoded_string 正好重复 k 次。
# 注意 k 保证为正整数。
# 你可以认为输入字符串总是有效的；输入字符串中没有额外的空格，且输入的方括号总是符合格式要求的。
# 此外，你可以认为原始数据不包含数字，所有的数字只表示重复的次数 k ，例如不会出现像 3a 或 2[4] 的输入。

def decodeString(s: str) -> str:
    stack_num = []
    stack_str = []
    current_num = 0
    current_str = ""

    for char in s:
        if char.isdigit():
            current_num = current_num * 10 + int(char)
        elif char == '[':
            stack_num.append(current_num)
            stack_str.append(current_str)
            current_num = 0
            current_str = ""
        elif char == ']':
            num = stack_num.pop()
            prev_str = stack_str.pop()
            current_str = prev_str + num * current_str
        else:
            current_str += char

    return current_str

# 示例使用
s = "3[a]2[bc]"
print(decodeString(s))  # 输出: "aaabcbc"