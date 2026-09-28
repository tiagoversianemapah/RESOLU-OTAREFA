# Questão 15 - Cifra de fluxo auto chave (não-síncrona)
# k0 = semente ; k_i = m_(i-1) ;  E: y_i = m_i + k_i mod 26 ; D: m_i = y_i - k_i mod 26

def cifrar(msg, semente):
    m = [ord(c) - 65 for c in msg.upper() if c.isalpha()]
    k = [semente] + m[:-1]
    return ''.join(chr((mi + ki) % 26 + 65) for mi, ki in zip(m, k))

def decifrar(cifra, semente):
    k, m = semente, []
    for c in cifra.upper():
        mi = (ord(c) - 65 - k) % 26
        m.append(mi)
        k = mi                       # a próxima chave é o texto claro recém-obtido
    return ''.join(chr(x + 65) for x in m)

if __name__ == "__main__":
    c = cifrar("ENCRYPTION", 20)
    print("Cifrado:", c)                      # YRPTPNIBWB
    print("Decifrado:", decifrar(c, 20))      # ENCRYPTION
