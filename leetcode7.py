"""
给出一个 32 位的有符号整数，你需要将这个整数中每位上的数字进行反转。

示例 1:

输入: 123
输出: 321
 示例 2:

输入: -123
输出: -321
示例 3:

输入: 120
输出: 21
"""


def reverse(x):
    import re

    source = []
    if re.search("-", str(x)):
        reverse = str(x)[1:]
        for i in reverse:
            source.insert(0, i)
        result = int("-" + "".join(source))
        if result < -2 ** 31:
            return 0
        else:
            return result
    else:
        reverse = str(x)
        for i in reverse:
            source.insert(0, i)
        result = int("".join(source))
        if result > 2 ** 31 - 1:
            return 0
        else:
            return result
