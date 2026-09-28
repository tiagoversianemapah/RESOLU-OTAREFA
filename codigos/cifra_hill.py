# Questão 14 - Cifra de Hill: C = K * P mod 26 (P = vetor coluna do bloco)
# Requer: pip install sympy
from sympy import Matrix

def _aplicar(K, texto):
    n = K.shape[0]
    nums = [ord(c) - 65 for c in texto.upper() if c.isalpha()]
    while len(nums) % n:          # completa o último bloco com 'X'
        nums.append(23)
    saida = []
    for i in range(0, len(nums), n):
        bloco = Matrix(nums[i:i + n])
        saida += [x % 26 for x in K * bloco]
    return ''.join(chr(x + 65) for x in saida)

def cifrar(msg, K):
    return _aplicar(Matrix(K), msg)

def decifrar(cifra, K):
    K_inv = Matrix(K).inv_mod(26)   # falha se mdc(det K, 26) != 1
    return _aplicar(K_inv, cifra)

if __name__ == "__main__":
    K1 = [[2, 1], [25, 4]]
    c = cifrar("DOGS", K1); print(c, decifrar(c, K1))          # UBEO DOGS
    K2 = [[0, 1, 0, 1], [1, 0, 0, 0], [0, 1, 1, 0], [1, 2, 3, 4]]
    c = cifrar("FLAMENGO", K2); print(c, decifrar(c, K2))      # XFLXBETA FLAMENGO
