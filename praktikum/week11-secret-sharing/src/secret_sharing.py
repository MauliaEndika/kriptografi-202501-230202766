import random

# Bilangan prima besar
PRIME = 208351617316091241234326746312124448251235562226470491514186331217050270460481

def split_secret(secret, k, n):
    # ubah string ke integer
    secret_int = int.from_bytes(secret.encode(), "big")

    coeffs = [secret_int] + [random.randrange(1, PRIME) for _ in range(k - 1)]

    def f(x):
        return sum(coeffs[i] * pow(x, i, PRIME) for i in range(k)) % PRIME

    return [(i, f(i)) for i in range(1, n + 1)]

def recover_secret(shares):
    secret = 0
    for j, (xj, yj) in enumerate(shares):
        lj = 1
        for m, (xm, _) in enumerate(shares):
            if m != j:
                lj *= xm * pow(xm - xj, -1, PRIME)
                lj %= PRIME
        secret = (secret + yj * lj) % PRIME

    return secret.to_bytes((secret.bit_length() + 7) // 8, "big").decode()

# =========================
# PEMAKAIAN (SAMA SEPERTI KODE KAMU)
# =========================

secret = "KriptografiUPB2025"

shares = split_secret(secret, 3, 5)
print("Shares:", shares)

recovered = recover_secret(shares[:3])
print("Recovered secret:", recovered)
