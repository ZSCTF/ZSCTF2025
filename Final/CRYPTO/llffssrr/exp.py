import hashlib
from Crypto.Util.number import *


class LFSR:
    def __init__(self, n, seed, mask, noise):
        self.state = seed
        self.mask_bits = [int(b) for b in bin(mask)[2:].zfill(n)]
        self.n = n
        self.noise = noise

    def update(self):
        s = sum([self.state[i] * self.mask_bits[i] for i in range(self.n)])
        self.state = self.state[1:] + [s]
        return self.state[-1]

    def __call__(self, n, out):
        eqs = []
        for _ in range(n):
            eqs.append(self.update() + self.noise[_ % 128] - out[_])
        return eqs


mask = 303923099786210747282565463186091151032
out = [0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 0, 1, 1, 0, 1, 0, 0, 1, 0, 0, 1, 1, 0, 1, 0, 0, 1, 1, 0, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 0, 0, 1, 1, 1, 1, 1, 0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 1, 1, 0, 0, 1, 0, 1, 0, 1, 0, 0, 1, 0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 1, 0, 1, 1, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0, 0, 0, 1, 1, 1, 1, 1, 0, 1, 1, 1, 0, 1, 1, 0, 0, 0, 0, 1, 0, 1, 1, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 1, 1, 0, 0, 1, 0, 0, 1, 1, 1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0]
br256 = BooleanPolynomialRing(256, [f"x{i}" for i in range(256)])
key_sym = list(br256.gens())
seed_ = key_sym[:128]
noise_ = key_sym[128:]
lfsr = LFSR(128, seed_, mask, noise_)
eqs = lfsr(270, out)
mat = matrix(GF(2), [[1 if j in i else 0 for j in key_sym] for i in eqs])
B = vector(GF(2),[1 if ' + 1' in str(i) else 0 for i in eqs])
sol = mat.solve_right(B)
seed = sol[:128]
noise = sol[128:]
seed = int("".join(map(str,seed)), 2)
print(seed)
flag = 'ZSCTF{' + hashlib.md5(str(seed).encode()).hexdigest() + '}'
print(flag)
# ZSCTF{b2c4a55a969bda52e0b553ad4f88cd29}