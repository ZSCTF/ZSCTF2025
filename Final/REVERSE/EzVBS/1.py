import random

def obfuscate_char(char):
    ascii_val = ord(char)
    method = random.choice(["add", "sub", "div"])  # 只保留加法、减法和除法

    if method == "add":
        a = random.randint(1, 2000)
        b = ascii_val - a
        return f"chr({a} + {b})"

    elif method == "sub":
        a = random.randint(ascii_val + 1, ascii_val + 3000)
        b = a - ascii_val
        return f"chr({a} - {b})"

    else:  # div
        a = random.randint(2, 50)
        b = ascii_val * a
        return f"chr({b} / {a})"

def obfuscate_string(s):
    return " & ".join(obfuscate_char(c) for c in s)

# 读取 txt 文件
with open("chall.txt", "r", encoding="utf-8") as file:
    lines = file.readlines()

# 拼接所有行，行间用 \r\n 分隔
full_content = "\r\n".join(line.strip() for line in lines if line.strip())

# 混淆整个内容
obfuscated_content = obfuscate_string(full_content)

# 生成 VBScript 代码，使用 Execute，最后加 vbcrlf
vbscript_code = f"Execute({obfuscated_content} & vbcrlf)"

# 保存到文件
with open("chall.vbs", "w", encoding="utf-8") as file:
    file.write(vbscript_code)

print("混淆完成，结果已保存到 chall.vbs")

