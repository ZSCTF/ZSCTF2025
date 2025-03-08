import hashlib

m = [int(b) for b in f"{256145588589325975889797077785006635585:0128b}"]
s = [int(b) for b in f"{161012175678781152374518992864407311111:0128b}".translate({48: 49, 49: 48})]
for _ in range(128):s = [s[-1] ^ sum(s[i] & m[i + 1] for i in range(127)) & m[0]] + s[:-1]
print("ZSCTF{" + hashlib.md5(str(int("".join(map(str, s)), 2)).encode()).hexdigest() + "}")

# ZSCTF{8d1e3405044a79b23a44a43084bd994b}