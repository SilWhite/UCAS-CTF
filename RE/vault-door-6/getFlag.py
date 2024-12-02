# reference: ChatGPT

# The predefined byte array (myBytes) from the Java code
my_bytes = [
    0x3B,
    0x65,
    0x21,
    0x0A,
    0x38,
    0x00,
    0x36,
    0x1D,
    0x0A,
    0x3D,
    0x61,
    0x27,
    0x11,
    0x66,
    0x27,
    0x0A,
    0x21,
    0x1D,
    0x61,
    0x3B,
    0x0A,
    0x2D,
    0x65,
    0x27,
    0x0A,
    0x6C,
    0x61,
    0x6D,
    0x37,
    0x6D,
    0x6D,
    0x6D,
]

# The XOR key (0x55)
xor_key = 0x55

# Calculate the original password
password_bytes = [my_byte ^ xor_key for my_byte in my_bytes]

# Convert the bytes to a string (password)
password = "".join(chr(byte) for byte in password_bytes)

# Output the result
print("The password is:", password)
