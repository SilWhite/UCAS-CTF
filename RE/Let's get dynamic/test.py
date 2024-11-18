a = [
    3913356094601673258,
    6478272586731273419,
    -1748037878477762649,
    4279356992215022931,
    -7229749860270763735,
    -6940086526098425816,
    97,
]
b = [
    6214777055764401527,
    8184225536171504527,
    -8364134581669616439,
    5916610601309242417,
    -2598080388612165765,
    -4252370736625094538,
    63,
]
'''
a:
0x364f08a25a57ba2a
0x59e772982244bccb
-0x1842473060983059
0x3b635482ec0f7d53
-0x64553b316c5e6ed7
-0x605023ece29247d8
0x61

b:
0x563f52ce0f15cd77
0x719435c3652ef38f
-0x7413601641fa5b37
0x521c05fe8d590431
-0x240e3c5925231085
-0x3b0374a7a9ce0f8a
0x3f
'''
# for i in range(49):
print(chr(0x2a ^ 0x77 ^ 0 ^ 19))
print(chr(0xba ^ 0xcd ^ 1 ^ 19))
print(chr(0x57 ^ 0x15 ^ 2 ^ 19))
print(chr(0x5a ^ 0x0f ^ 3 ^ 19))
print(chr(0xa2 ^ 0xce ^ 4 ^ 19))


def process_little_endian(num, byte_size):
    bytes_list = []
    # 按照小端序取出每个字节
    for i in range(byte_size):
        # 取出当前字节
        current_byte = (num >> (i * 8)) & 0xFF
        bytes_list.append(current_byte)
    return bytes_list


a_bytes = []
b_bytes = []
for i in range(6):
    a_bytes += process_little_endian(a[i], 8)
    b_bytes += process_little_endian(b[i], 8)
a_bytes += process_little_endian(a[6], 1)
b_bytes += process_little_endian(b[6], 1)

print(a_bytes)
print(b_bytes)

for i in range(49):
    print(chr(a_bytes[i] ^ b_bytes[i] ^ i ^ 19), end='')
