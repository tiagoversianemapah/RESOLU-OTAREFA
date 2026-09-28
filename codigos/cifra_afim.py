# Questão 13 - Cifra afim: E(x) = a*x + b mod 26  |  D(y) = a^-1 * (y - b) mod 26
from math import gcd

def cifrar(msg, a, b):
    if gcd(a, 26) != 1:
        raise ValueError("a deve ser inversível mod 26 (mdc(a,26)=1)")
    return ''.join(chr((a * (ord(c) - 65) + b) % 26 + 65) for c in msg.upper() if c.isalpha())

def decifrar(cifra, a, b):
    a_inv = pow(a, -1, 26)
    return ''.join(chr((a_inv * (ord(c) - 65 - b)) % 26 + 65) for c in cifra.upper() if c.isalpha())

if __name__ == "__main__":
    c = cifrar("OBTER", 3, 7)
    print("Cifrado:", c)                  # XKMTG
    print("Decifrado:", decifrar(c, 3, 7))  # OBTER
