int_values = [
    1096770097,
    1952395366,
    1600270708,
    1601398833,
    1716808014,
    1734304867,
    942695730,
    942748212,
]


hex_string = ""
for value in int_values:
    for i in range(3, -1, -1):
        byte = (value >> (i * 8)) & 0xFF
        hex_string += format(byte, "02x")


for char_index in range(0, len(hex_string), 2):
    print(chr(int(hex_string[char_index : char_index + 2], 16)), end="")
