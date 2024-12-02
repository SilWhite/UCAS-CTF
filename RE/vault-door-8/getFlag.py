# reference: ChatGPT


# 定义反向的switchBits操作
def switch_bits(c, p1, p2):
    mask1 = 1 << p1
    mask2 = 1 << p2
    bit1 = c & mask1
    bit2 = c & mask2
    rest = c & ~(mask1 | mask2)
    shift = p2 - p1
    result = (bit1 << shift) | (bit2 >> shift) | rest
    return result


# 定义反向scramble方法
def unscramble(password):
    password = list(password)
    for i in range(len(password)):
        c = password[i]
        c = switch_bits(c, 6, 7)
        c = switch_bits(c, 2, 5)
        c = switch_bits(c, 3, 4)
        c = switch_bits(c, 0, 1)
        c = switch_bits(c, 4, 7)
        c = switch_bits(c, 5, 6)
        c = switch_bits(c, 0, 3)
        c = switch_bits(c, 1, 2)
        password[i] = c
    return password


# 预期的值（从Java代码中提取）
expected = [
    0xF4,
    0xC0,
    0x97,
    0xF0,
    0x77,
    0x97,
    0xC0,
    0xE4,
    0xF0,
    0x77,
    0xA4,
    0xD0,
    0xC5,
    0x77,
    0xF4,
    0x86,
    0xD0,
    0xA5,
    0x45,
    0x96,
    0x27,
    0xB5,
    0x77,
    0xE0,
    0x95,
    0xF1,
    0xE1,
    0xE0,
    0xA4,
    0xC0,
    0x94,
    0xA4,
]


# 执行反向操作，猜测密码
def find_password():
    # 初始化一个空的密码
    possible_password = []
    for c in expected:
        # 对每个字节进行反向scramble操作
        unscrambled = unscramble([c])
        possible_password.append(unscrambled[0])

    # 输出可能的密码
    return "".join(chr(x) for x in possible_password)


# 获取反向操作后的密码
password = find_password()
print(f"可能的密码是: {password}")
