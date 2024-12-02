his_bytes = [
    106,
    85,
    53,
    116,
    95,
    52,
    95,
    98,
    0x55,
    0x6E,
    0x43,
    0x68,
    0x5F,
    0x30,
    0x66,
    0x5F,
    0o142,
    0o131,
    0o164,
    0o63,
    0o163,
    0o137,
    0o70,
    0o146,
    "4",
    "a",
    "6",
    "c",
    "b",
    "f",
    "3",
    "b",
]

flag = ""
for byte in his_bytes:
    if isinstance(byte, int):
        flag += chr(byte)
    else:
        flag += byte

print(flag)
