# Exercícios de Aprendizagem: Criptografia Clássica

Tabela: A=0 B=1 C=2 D=3 E=4 F=5 G=6 H=7 I=8 J=9 K=10 L=11 M=12
N=13 O=14 P=15 Q=16 R=17 S=18 T=19 U=20 V=21 W=22 X=23 Y=24 Z=25

---

### 1) Hill: DOGS, K = [[2, 1], [25, 4]] (mod 26)

DO = (3, 14) GS = (6, 18)

**Cifrar (C = K·P):**

```
| 2   1 | | 3  |   | 2·3 + 1·14  |   | 20  |   | 20 |
|       | |    | = |             | = |     | ≡ |    | → U B
| 25  4 | | 14 |   | 25·3 + 4·14 |   | 131 |   | 1  |

| 2   1 | | 6  |   | 2·6 + 1·18  |   | 30  |   | 4  |
|       | |    | = |             | = |     | ≡ |    | → E O
| 25  4 | | 18 |   | 25·6 + 4·18 |   | 222 |   | 14 |
```

**Cifra: UBEO**

**K⁻¹:**

det K = 2·4 − 1·25 = −17 ≡ 9 (mod 26)
9⁻¹ mod 26 = 3, porque 9·3 = 27 ≡ 1

K⁻¹ = det⁻¹ · adj K = 3 · [[4, −1], [−25, 2]] = [[12, −3], [−75, 6]]

**K⁻¹ ≡ [[12, 23], [3, 6]] (mod 26)**

**Decifrar (P = K⁻¹·C):**

```
| 12  23 | | 20 |   | 263 |   | 3  |
|        | |    | = |     | ≡ |    | → D O
| 3    6 | | 1  |   | 66  |   | 14 |

| 12  23 | | 4  |   | 370 |   | 6  |
|        | |    | = |     | ≡ |    | → G S
| 3    6 | | 14 |   | 96  |   | 18 |
```

**Mensagem: DOGS**

---

### 2) Hill: FLAMENGO (mod 26)

```
      | 0 1 0 1 |
K =   | 1 0 0 0 |
      | 0 1 1 0 |
      | 1 2 3 4 |
```

FLAM = (5, 11, 0, 12) ENGO = (4, 13, 6, 14)

**Cifrar:**

K·(5, 11, 0, 12):
- 0·5 + 1·11 + 0·0 + 1·12 = 23
- 1·5 = 5
- 1·11 + 1·0 = 11
- 1·5 + 2·11 + 3·0 + 4·12 = 75 ≡ 23

→ (23, 5, 11, 23) = X F L X

K·(4, 13, 6, 14):
- 13 + 14 = 27 ≡ 1
- 4
- 13 + 6 = 19
- 4 + 26 + 18 + 56 = 104 ≡ 0

→ (1, 4, 19, 0) = B E T A

**Cifra: XFLXBETA**

**K⁻¹ por Gauss-Jordan (mod 26):**

```
[ 0 1 0 1 | 1 0 0 0 ]
[ 1 0 0 0 | 0 1 0 0 ]
[ 0 1 1 0 | 0 0 1 0 ]
[ 1 2 3 4 | 0 0 0 1 ]
```

L1 ↔ L2:

```
[ 1 0 0 0 | 0 1 0 0 ]
[ 0 1 0 1 | 1 0 0 0 ]
[ 0 1 1 0 | 0 0 1 0 ]
[ 1 2 3 4 | 0 0 0 1 ]
```

L3 = L3 − L2 e L4 = L4 − L1 − 2·L2:

```
[ 1 0 0  0 |  0  1 0 0 ]
[ 0 1 0  1 |  1  0 0 0 ]
[ 0 0 1 −1 | −1  0 1 0 ]
[ 0 0 3  2 | −2 −1 0 1 ]
```

L4 = L4 − 3·L3:

```
[ 0 0 0 5 | 1 −1 −3 1 ]
```

5⁻¹ mod 26 = 21, porque 5·21 = 105 ≡ 1. Então L4 = 21·L4:

```
[ 0 0 0 1 | 21 −21 −63 21 ] ≡ [ 0 0 0 1 | 21 5 15 21 ]
```

L3 = L3 + L4 → [ 0 0 1 0 | 20 5 16 21 ]

L2 = L2 − L4 → [ 0 1 0 0 | −20 −5 −15 −21 ] ≡ [ 0 1 0 0 | 6 21 11 5 ]

```
        |  0   1   0   0 |
K⁻¹ =   |  6  21  11   5 |
        | 20   5  16  21 |
        | 21   5  15  21 |
```

**Decifrar:**

K⁻¹·(23, 5, 11, 23) = (5, 479, 1144, 1156) ≡ (5, 11, 0, 12) = F L A M

K⁻¹·(1, 4, 19, 0) = (4, 299, 344, 326) ≡ (4, 13, 6, 14) = E N G O

**Mensagem: FLAMENGO**

---

### 3) Inversa de A em Z₅

```
      | 3 1 2 |
A =   | 1 1 2 |
      | 0 1 3 |
```

det A = 3(3 − 2) − 1(3 − 0) + 2(1 − 0) = 3 − 3 + 2 = 2

2⁻¹ mod 5 = 3, porque 2·3 = 6 ≡ 1

**Cofatores:**

- C11 = 1  C12 = −3  C13 = 1
- C21 = −1  C22 = 9  C23 = −3
- C31 = 0  C32 = −4  C33 = 2

adj A = (cofatores)ᵀ = [[1, −1, 0], [−3, 9, −4], [1, −3, 2]] ≡ [[1, 4, 0], [2, 4, 1], [1, 2, 2]] (mod 5)

A⁻¹ = 3 · adj A = [[3, 12, 0], [6, 12, 3], [3, 6, 6]]

```
        | 3 2 0 |
A⁻¹ ≡   | 1 2 3 |   (mod 5)
        | 3 1 1 |
```

---

### 4) Afim: OBTER, e(x) = 3x + 7 mod 26

```
O = 14 → 3·14 + 7 = 49 ≡ 23 → X
B = 1  → 3·1  + 7 = 10      → K
T = 19 → 3·19 + 7 = 64 ≡ 12 → M
E = 4  → 3·4  + 7 = 19      → T
R = 17 → 3·17 + 7 = 58 ≡ 6  → G
```

**Cifra: XKMTG**

**Inversa:** 3⁻¹ mod 26 = 9, porque 3·9 = 27 ≡ 1

**d(y) = 9(y − 7) mod 26**

```
X = 23 → 9·16  = 144 ≡ 14 → O
K = 10 → 9·3   = 27  ≡ 1  → B
M = 12 → 9·5   = 45  ≡ 19 → T
T = 19 → 9·12  = 108 ≡ 4  → E
G = 6  → 9·(−1) = −9 ≡ 17 → R
```

**Mensagem: OBTER**

---

### 5) Quebrar a cifra afim

Em inglês, as letras mais frequentes são E (4) e T (19). Então:

- E → B: 4a + b ≡ 1 (mod 26)
- T → U: 19a + b ≡ 20 (mod 26)

Subtraindo: 15a ≡ 19 (mod 26)

15⁻¹ mod 26 = 7, porque 15·7 = 105 ≡ 1

a ≡ 19·7 = 133 ≡ 3

b ≡ 1 − 4·3 = −11 ≡ 15

mdc(3, 26) = 1, então a chave é válida.

**e(x) = 3x + 15 → d(y) = 9(y − 15) mod 26**

---

### 6) Cifra de bloco × cifra de fluxo

A cifra de bloco divide a mensagem em blocos de tamanho fixo e cifra cada bloco inteiro de uma vez com a mesma chave (ex.: Hill, DES, AES).

A cifra de fluxo cifra bit a bit (ou caractere a caractere), somando cada símbolo com uma sequência de chave que muda a cada posição (ex.: LFSR, RC4, auto chave). Em geral é mais rápida e simples de implementar em hardware.

---

### 7) LFSR: estado inicial (k1, k2, k3, k4) = (0, 1, 1, 1)

Saída = k1. Realimentação = k1 ⊕ k2, que entra em k4. Deslocamento: k1 ← k2 ← k3 ← k4.

```
clk | k1 k2 k3 k4 | saída | k1⊕k2
 0  |  0  1  1  1 |   0   |   1
 1  |  1  1  1  1 |   1   |   0
 2  |  1  1  1  0 |   1   |   0
 3  |  1  1  0  0 |   1   |   0
 4  |  1  0  0  0 |   1   |   1
 5  |  0  0  0  1 |   0   |   0
 6  |  0  0  1  0 |   0   |   0
 7  |  0  1  0  0 |   0   |   1
 8  |  1  0  0  1 |   1   |   1
 9  |  0  0  1  1 |   0   |   0
10  |  0  1  1  0 |   0   |   1
11  |  1  1  0  1 |   1   |   0
12  |  1  0  1  0 |   1   |   1
13  |  0  1  0  1 |   0   |   1
14  |  1  0  1  1 |   1   |   1
15  |  0  1  1  1 |  (volta ao início: período 15)
```

**Chave:** 011110001001101 | 011110001 ...

**Cifrar** m = DF0E01h (24 bits):

```
m = 1101 1111 0000 1110 0000 0001
k = 0111 1000 1001 1010 1111 0001
    ------------------------------ ⊕
c = 1010 0111 1001 0100 1111 0000
```

**c = A794F0h**

---

### 8) Auto chave: M = ENCRYPTION, K = 20

k₀ = 20 e kᵢ = mᵢ₋₁

**Cifrar:** yᵢ = mᵢ + kᵢ mod 26

```
M  :  E   N   C   R   Y   P   T   I   O   N
m  :  4  13   2  17  24  15  19   8  14  13
k  : 20   4  13   2  17  24  15  19   8  14
m+k: 24  17  15  19  41  39  34  27  22  27
y  : 24  17  15  19  15  13   8   1  22   1
C  :  Y   R   P   T   P   N   I   B   W   B
```

**Chave:** 20, 4, 13, 2, 17, 24, 15, 19, 8, 14

**Cifra: YRPTPNIBWB**

**Decifrar:** mᵢ = yᵢ − kᵢ mod 26. Cada letra decifrada vira a próxima chave.

```
y  : 24  17  15  19  15  13   8   1  22   1
k  : 20   4  13   2  17  24  15  19   8  14
y−k:  4  13   2  17  −2 −11  −7 −18  14 −13
m  :  4  13   2  17  24  15  19   8  14  13
M  :  E   N   C   R   Y   P   T   I   O   N
```

**Mensagem: ENCRYPTION**

---

### 9) Cifra polialfabética × monoalfabética

A monoalfabética usa um único alfabeto de substituição, então cada letra vira sempre a mesma letra (ex.: César, afim). Ela mantém a frequência das letras e pode ser quebrada por análise de frequência.

A polialfabética usa vários alfabetos, então a mesma letra pode virar letras diferentes dependendo da posição ou da chave (ex.: Vigenère, auto chave). Ela disfarça as frequências e é mais difícil de quebrar.

---

### 10) E(x) = ax + b mod 47

Para ter inversa, é preciso mdc(a, 47) = 1.

Como 47 é primo, isso vale para qualquer a que não seja múltiplo de 47.

**Não é permitido: a ≡ 0 (mod 47).** Os valores a = 1, 2, …, 46 são todos permitidos.

---

### 11) Criptografia ou esteganografia?

As duas. Codificar as mensagens com uma chave é criptografia, porque esconde o conteúdo. Esconder a mensagem verdadeira numa cápsula sob a pele é esteganografia, porque esconde a existência da mensagem. A mensagem falsa serve para enganar quem interceptar o portador.

---

### 12) César com chave 11: x = y − 11 mod 26

```
H  P  H  T  W  W  X  P  P  E  L  E  X  T  O  Y  T  R  S  E
7 15  7 19 22 22 23 15 15  4 11  4 23 19 14 24 19 17 18  4
22 4 22  8 11 11 12  4  4 19  0 19 12  8  3 13  8  6  7 19
W  E  W  I  L  L  M  E  E  T  A  T  M  I  D  N  I  G  H  T
```

**WE WILL MEET AT MIDNIGHT**

---

### 13) Cifra afim (Python)

```python
def cifrar(msg, a, b):
    return ''.join(chr((a*(ord(c)-65) + b) % 26 + 65) for c in msg)

def decifrar(cif, a, b):
    ai = pow(a, -1, 26)
    return ''.join(chr(ai*(ord(c)-65-b) % 26 + 65) for c in cif)

print(cifrar("OBTER", 3, 7))    # XKMTG
print(decifrar("XKMTG", 3, 7))  # OBTER
```

### 14) Cifra de Hill (Python)

```python
from sympy import Matrix

def hill(K, txt):
    n = K.shape[0]
    v = [ord(c)-65 for c in txt]
    out = []
    for i in range(0, len(v), n):
        out += [x % 26 for x in K * Matrix(v[i:i+n])]
    return ''.join(chr(x+65) for x in out)

K = Matrix([[2, 1], [25, 4]])
c = hill(K, "DOGS")               # UBEO
print(c, hill(K.inv_mod(26), c))  # DOGS
```

### 15) Auto chave (Python)

```python
def cifrar(msg, k):
    out = ''
    for c in msg:
        m = ord(c) - 65
        out += chr((m + k) % 26 + 65)
        k = m
    return out

def decifrar(cif, k):
    out = ''
    for c in cif:
        m = (ord(c) - 65 - k) % 26
        out += chr(m + 65)
        k = m
    return out

print(cifrar("ENCRYPTION", 20))    # YRPTPNIBWB
print(decifrar("YRPTPNIBWB", 20))  # ENCRYPTION
```
