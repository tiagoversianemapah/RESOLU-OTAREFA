# Exercícios de Aprendizagem: Criptografia Clássica (resolução)

**Convenções usadas em todas as questões:**
A=0, B=1, C=2, D=3, E=4, F=5, G=6, H=7, I=8, J=9, K=10, L=11, M=12,
N=13, O=14, P=15, Q=16, R=17, S=18, T=19, U=20, V=21, W=22, X=23, Y=24, Z=25

Hill: cada bloco é um **vetor coluna** P, e C = K · P (mod 26).

---

## 1) Cifra de Hill: DOGS, K = [[2, 1], [25, 4]]

**Blocos:** DO = (3, 14) GS = (6, 18)

**Cifrando:**

K·(3,14) = (2·3 + 1·14 ; 25·3 + 4·14) = (20 ; 131) ≡ (20 ; 1) → **U B**

K·(6,18) = (2·6 + 1·18 ; 25·6 + 4·18) = (30 ; 222) ≡ (4 ; 14) → **E O**

**Cifra: UBEO**

**Inversa de K:**

det K = 2·4 − 1·25 = 8 − 25 = −17 ≡ 9 (mod 26)
mdc(9, 26) = 1 → existe inversa. 9⁻¹ mod 26 = 3 (pois 9·3 = 27 ≡ 1)

adj K = [[4, −1], [−25, 2]] ≡ [[4, 25], [1, 2]]

K⁻¹ = 3 · [[4, 25], [1, 2]] = [[12, 75], [3, 6]] ≡ **[[12, 23], [3, 6]]**

(Verificação: K·K⁻¹ = [[27, 52], [312, 599]] ≡ [[1, 0], [0, 1]] ✔)

**Decifrando:**

K⁻¹·(20,1) = (240 + 23 ; 60 + 6) = (263 ; 66) ≡ (3 ; 14) → D O

K⁻¹·(4,14) = (48 + 322 ; 12 + 84) = (370 ; 96) ≡ (6 ; 18) → G S

**Mensagem decifrada: DOGS** ✔

---

## 2) Cifra de Hill: FLAMENGO, K 4×4

K = [[0,1,0,1], [1,0,0,0], [0,1,1,0], [1,2,3,4]]

**Blocos:** FLAM = (5, 11, 0, 12) ENGO = (4, 13, 6, 14)

**Cifrando:**

K·(5,11,0,12):
- linha 1: 0 + 11 + 0 + 12 = 23
- linha 2: 5 = 5
- linha 3: 11 + 0 = 11
- linha 4: 5 + 22 + 0 + 48 = 75 ≡ 23

→ (23, 5, 11, 23) = **X F L X**

K·(4,13,6,14):
- linha 1: 13 + 14 = 27 ≡ 1
- linha 2: 4
- linha 3: 13 + 6 = 19
- linha 4: 4 + 26 + 18 + 56 = 104 ≡ 0

→ (1, 4, 19, 0) = **B E T A**

**Cifra: XFLXBETA**

**Inversa de K:**

det K (expansão pela linha 2, que é (1,0,0,0)):
det K = (−1)²⁺¹ · 1 · det[[1,0,1],[1,1,0],[2,3,4]]
det[[1,0,1],[1,1,0],[2,3,4]] = 1·(4 − 0) − 0 + 1·(3 − 2) = 5
det K = −5 ≡ 21 (mod 26)

mdc(21, 26) = 1 → existe inversa. 21⁻¹ mod 26 = 5 (pois 21·5 = 105 = 4·26 + 1)

adj K (mod 26) = [[0,21,0,0], [22,25,23,1], [4,1,24,25], [25,1,3,25]]

K⁻¹ = 5 · adj K (mod 26) =

```
        | 0   1   0   0 |
K⁻¹ =   | 6  21  11   5 |
        |20   5  16  21 |
        |21   5  15  21 |
```

**Decifrando:**

K⁻¹·(23,5,11,23) = (5 ; 138+105+121+115 ; 460+25+176+483 ; 483+25+165+483)
= (5 ; 479 ; 1144 ; 1156) ≡ (5, 11, 0, 12) → F L A M

K⁻¹·(1,4,19,0) = (4 ; 6+84+209+0 ; 20+20+304+0 ; 21+20+285+0)
= (4 ; 299 ; 344 ; 326) ≡ (4, 13, 6, 14) → E N G O

**Mensagem decifrada: FLAMENGO** ✔

---

## 3) Inversa em Z₅ de A = [[3,1,2], [1,1,2], [0,1,3]]

det A = 3·(1·3 − 2·1) − 1·(1·3 − 2·0) + 2·(1·1 − 1·0)
      = 3·1 − 1·3 + 2·1 = 2

det A ≡ 2 (mod 5) → 2⁻¹ mod 5 = 3 (pois 2·3 = 6 ≡ 1)

Cofatores:
- C11 = +(3−2) = 1  C12 = −(3−0) = −3  C13 = +(1−0) = 1
- C21 = −(3−2) = −1  C22 = +(9−0) = 9  C23 = −(3−0) = −3
- C31 = +(2−2) = 0  C32 = −(6−2) = −4  C33 = +(3−1) = 2

adj A = (cofatores)ᵀ = [[1, −1, 0], [−3, 9, −4], [1, −3, 2]]
≡ [[1, 4, 0], [2, 4, 1], [1, 2, 2]] (mod 5)

A⁻¹ = 3 · adj A = [[3, 12, 0], [6, 12, 3], [3, 6, 6]] ≡

```
        | 3  2  0 |
A⁻¹ =   | 1  2  3 |
        | 3  1  1 |
```

(Verificação: A·A⁻¹ = [[16,10,5],[10,6,5],[10,5,6]] ≡ I (mod 5) ✔)

---

## 4) Cifra afim: OBTER, eₖ(x) = 3x + 7 mod 26

| Letra | x  | 3x + 7 | mod 26 | Cifra |
|-------|----|--------|--------|-------|
| O     | 14 | 49     | 23     | X     |
| B     | 1  | 10     | 10     | K     |
| T     | 19 | 64     | 12     | M     |
| E     | 4  | 19     | 19     | T     |
| R     | 17 | 58     | 6      | G     |

**Cifra: XKMTG**

**Função inversa:** 3⁻¹ mod 26 = 9 (pois 3·9 = 27 ≡ 1)

**dₖ(y) = 9·(y − 7) mod 26**  (equivalente: 9y − 63 ≡ 9y + 15 mod 26)

| Cifra | y  | 9(y − 7) | mod 26 | Letra |
|-------|----|----------|--------|-------|
| X     | 23 | 144      | 14     | O     |
| K     | 10 | 27       | 1      | B     |
| M     | 12 | 45       | 19     | T     |
| T     | 19 | 108      | 4      | E     |
| G     | 6  | −9       | 17     | R     |

**Mensagem decifrada: OBTER** ✔

---

## 5) Quebra da cifra afim por análise de frequência

Em inglês as letras mais frequentes são **E** (4) e **T** (19). Então:
- E → B: a·4 + b ≡ 1 (mod 26)
- T → U: a·19 + b ≡ 20 (mod 26)

Subtraindo a 1ª da 2ª: 15a ≡ 19 (mod 26)

15⁻¹ mod 26 = 7 (pois 15·7 = 105 ≡ 1)
a ≡ 19·7 = 133 ≡ **3**

b ≡ 1 − 4·3 = −11 ≡ **15**

mdc(3, 26) = 1 → a chave é válida.

**Chave: e(x) = 3x + 15 mod 26**
**Decifragem: d(y) = 3⁻¹(y − 15) = 9(y − 15) mod 26**

(Teste: d(B) = 9·(1−15) = −126 ≡ 4 = E ✔ ; d(U) = 9·(20−15) = 45 ≡ 19 = T ✔)

---

## 6) Cifra de bloco × cifra de fluxo

- **Cifra de bloco:** divide a mensagem em blocos de tamanho fixo (ex.: 64 ou 128 bits, ou pares de letras no Hill) e cifra cada bloco inteiro de uma vez com a mesma chave. Ex.: Hill, DES, AES.
- **Cifra de fluxo:** cifra a mensagem bit a bit (ou caractere a caractere), combinando cada símbolo com um elemento de uma sequência de chave (keystream), geralmente com XOR / soma mod 2. Ex.: One-Time Pad, LFSR, RC4, auto chave.

Resumindo: a cifra de bloco opera sobre grupos de símbolos, e a cifra de fluxo opera símbolo a símbolo usando uma chave que varia ao longo da mensagem. Cifras de fluxo costumam ser mais rápidas e simples em hardware. Cifras de bloco são mais usadas em software e em protocolos.

---

## 7) LFSR: vetor inicial (k1,k2,k3,k4) = (0,1,1,1), m = DF0E01h

Pelo diagrama:
- a saída é **k1**;
- a realimentação é **k1 ⊕ k2**, que entra em **k4**;
- o deslocamento é k1 ← k2 ← k3 ← k4.

| clock | k1 k2 k3 k4 | saída kᵢ = k1 | realim. k1⊕k2 |
|-------|-------------|---------------|---------------|
| 0     | 0 1 1 1     | 0             | 1             |
| 1     | 1 1 1 1     | 1             | 0             |
| 2     | 1 1 1 0     | 1             | 0             |
| 3     | 1 1 0 0     | 1             | 0             |
| 4     | 1 0 0 0     | 1             | 1             |
| 5     | 0 0 0 1     | 0             | 0             |
| 6     | 0 0 1 0     | 0             | 0             |
| 7     | 0 1 0 0     | 0             | 1             |
| 8     | 1 0 0 1     | 1             | 1             |
| 9     | 0 0 1 1     | 0             | 0             |
| 10    | 0 1 1 0     | 0             | 1             |
| 11    | 1 1 0 1     | 1             | 0             |
| 12    | 1 0 1 0     | 1             | 1             |
| 13    | 0 1 0 1     | 0             | 1             |
| 14    | 1 0 1 1     | 1             | 1             |
| 15    | 0 1 1 1     | ← volta ao estado inicial | |

Período = 15 = 2⁴ − 1 (período máximo).

**Chave de fluxo:** k = 0111 1000 1001 101 | 0111 1000 1 ... (repete a cada 15 bits)

**Cifragem:** m = DF0E01h tem 24 bits.

```
m  = 1101 1111 0000 1110 0000 0001   (D F 0 E 0 1)
k  = 0111 1000 1001 1010 1111 0001
     ---------------------------- XOR (soma mod 2)
c  = 1010 0111 1001 0100 1111 0000
```

**c = A794F0h**

(Decifragem: c ⊕ k = m, porque XOR é a sua própria inversa.)

---

## 8) Auto chave (não-síncrona): M = ENCRYPTION, K = 20

A chave inicial é k₀ = 20, e as seguintes são kᵢ = mᵢ₋₁ (a letra anterior do texto claro).

| i  | 0  | 1  | 2  | 3  | 4  | 5  | 6  | 7  | 8  | 9  |
|----|----|----|----|----|----|----|----|----|----|----|
| M  | E  | N  | C  | R  | Y  | P  | T  | I  | O  | N  |
| mᵢ | 4  | 13 | 2  | 17 | 24 | 15 | 19 | 8  | 14 | 13 |
| kᵢ | 20 | 4  | 13 | 2  | 17 | 24 | 15 | 19 | 8  | 14 |
| mᵢ+kᵢ | 24 | 17 | 15 | 19 | 41 | 39 | 34 | 27 | 22 | 27 |
| yᵢ (mod 26) | 24 | 17 | 15 | 19 | 15 | 13 | 8 | 1 | 22 | 1 |
| Cifra | Y | R | P | T | P | N | I | B | W | B |

**Chave de fluxo:** 20, 4, 13, 2, 17, 24, 15, 19, 8, 14
**Texto cifrado: YRPTPNIBWB**

**Decifragem:** mᵢ = yᵢ − kᵢ mod 26. Cada letra decifrada vira a chave da próxima.

| i | yᵢ | kᵢ | yᵢ − kᵢ | mod 26 | mᵢ |
|---|----|----|---------|--------|----|
| 0 | 24 | 20 | 4   | 4  | E |
| 1 | 17 | 4  | 13  | 13 | N |
| 2 | 15 | 13 | 2   | 2  | C |
| 3 | 19 | 2  | 17  | 17 | R |
| 4 | 15 | 17 | −2  | 24 | Y |
| 5 | 13 | 24 | −11 | 15 | P |
| 6 | 8  | 15 | −7  | 19 | T |
| 7 | 1  | 19 | −18 | 8  | I |
| 8 | 22 | 8  | 14  | 14 | O |
| 9 | 1  | 14 | −13 | 13 | N |

**Mensagem decifrada: ENCRYPTION** ✔

---

## 9) Cifra polialfabética × monoalfabética

- **Monoalfabética:** usa um único alfabeto de substituição fixo. Cada letra do texto claro vira sempre a mesma letra cifrada (ex.: A→D sempre). Ex.: César, cifra afim. A frequência das letras do idioma é preservada, então ela é quebrada facilmente por análise de frequência (como na questão 5).
- **Polialfabética:** usa vários alfabetos de substituição, que mudam conforme a posição na mensagem ou a chave. Uma mesma letra do texto claro pode virar letras cifradas diferentes. Ex.: Vigenère, auto chave, Enigma. Ela "achata" a distribuição de frequências e dificulta a análise de frequência.

---

## 10) Valores de a não permitidos em E(x) = ax + b mod 47

A cifra só é inversível se mdc(a, 47) = 1.
Como 47 é **primo**, mdc(a, 47) = 1 para todo a que não é múltiplo de 47.

**Não é permitido: a ≡ 0 (mod 47)**, ou seja, a = 0 (e seus equivalentes 47, 94, ...).
Todos os valores a = 1, 2, ..., 46 são permitidos (46 valores).

---

## 11) Criptografia ou esteganografia?

O exemplo usa **as duas técnicas**:
- **Criptografia:** as mensagens (a falsa e a verdadeira) são codificadas com uma chave que o agente conhece. O conteúdo fica ilegível, mas a existência da mensagem não é escondida.
- **Esteganografia:** a mensagem verdadeira fica **oculta** numa cápsula sob a pele. O objetivo é esconder a própria existência da mensagem. A mensagem falsa serve de "isca" para um eventual interceptador.

A proteção da mensagem verdadeira, que é o ponto central do exemplo, é **esteganografia**, combinada com criptografia.

---

## 12) César com deslocamento 11

Decifrar: x = y − 11 (mod 26)

```
Cifra : H  P  H  T  W  W  X  P  P  E  L  E  X  T  O  Y  T  R  S  E
y     : 7 15  7 19 22 22 23 15 15  4 11  4 23 19 14 24 19 17 18  4
y−11  :-4  4 -4  8 11 11 12  4  4 -7  0 -7 12  8  3 13  8  6  7 -7
mod 26:22  4 22  8 11 11 12  4  4 19  0 19 12  8  3 13  8  6  7 19
Claro : W  E  W  I  L  L  M  E  E  T  A  T  M  I  D  N  I  G  H  T
```

**Mensagem: WE WILL MEET AT MIDNIGHT** ("Nós nos encontraremos à meia-noite")

---

## 13), 14) e 15) Implementações (Python)

Os códigos completos estão na pasta `codigos/`:
- `codigos/cifra_afim.py`: questão 13
- `codigos/cifra_hill.py`: questão 14
- `codigos/cifra_autochave.py`: questão 15

### 13) Cifra afim
```python
from math import gcd

def cifrar(msg, a, b):
    if gcd(a, 26) != 1:
        raise ValueError("a deve ser inversível mod 26")
    return ''.join(chr((a*(ord(c)-65) + b) % 26 + 65) for c in msg.upper() if c.isalpha())

def decifrar(cifra, a, b):
    a_inv = pow(a, -1, 26)
    return ''.join(chr((a_inv*(ord(c)-65-b)) % 26 + 65) for c in cifra.upper() if c.isalpha())

print(cifrar("OBTER", 3, 7))     # XKMTG
print(decifrar("XKMTG", 3, 7))   # OBTER
```

### 14) Cifra de Hill
```python
from sympy import Matrix

def _aplicar(K, texto):
    n = K.shape[0]
    nums = [ord(c)-65 for c in texto.upper() if c.isalpha()]
    while len(nums) % n:
        nums.append(23)                 # completa com 'X'
    saida = []
    for i in range(0, len(nums), n):
        saida += [x % 26 for x in K * Matrix(nums[i:i+n])]
    return ''.join(chr(x+65) for x in saida)

def cifrar(msg, K):   return _aplicar(Matrix(K), msg)
def decifrar(c, K):   return _aplicar(Matrix(K).inv_mod(26), c)

K = [[2, 1], [25, 4]]
print(cifrar("DOGS", K))     # UBEO
print(decifrar("UBEO", K))   # DOGS
```

### 15) Cifra de fluxo auto chave
```python
def cifrar(msg, semente):
    m = [ord(c)-65 for c in msg.upper() if c.isalpha()]
    k = [semente] + m[:-1]
    return ''.join(chr((mi+ki) % 26 + 65) for mi, ki in zip(m, k))

def decifrar(cifra, semente):
    k, m = semente, []
    for c in cifra.upper():
        mi = (ord(c)-65-k) % 26
        m.append(mi)
        k = mi
    return ''.join(chr(x+65) for x in m)

print(cifrar("ENCRYPTION", 20))    # YRPTPNIBWB
print(decifrar("YRPTPNIBWB", 20))  # ENCRYPTION
```
