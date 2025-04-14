
def trans(s: str, b: int) -> list[int]:
    # 预处理字符到数字的转换
    digits_list = [int(c) for c in s]
    result = []
    
    while digits_list:
        next_digits = []  # 存储商
        rem = 0           # 存储余数
        
        # 竖式除法计算
        for d in digits_list:
            rem = rem * 10 + d
            q = rem // b  # 商
            if q or next_digits:  # 跳过前导零
                next_digits.append(q)
            rem = rem % b
        
        result.append(rem)
        digits_list = next_digits
    
    # 反转结果（因为余数是按从低位到高位的顺序收集的）
    result.reverse()
    return result

s = "123456679900324"


a = trans(s,8)
print(a)
print(oct(int(s)))