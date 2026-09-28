# Criptografia Clássica: Exercícios (versão resumida)

A=0, B=1, …, Z=25

**1)** DOGS → DO=(3,14), GS=(6,18)
K·(3,14) = (20, 131) ≡ (20, 1) = UB
K·(6,18) = (30, 222) ≡ (4, 14) = EO
**Cifra: UBEO**
det K = 8 − 25 = −17 ≡ 9 → 9⁻¹ = 3
K⁻¹ = 3·[[4, −1], [−25, 2]] ≡ **[[12, 23], [3, 6]]**
K⁻¹·(20,1) = (3,14) = DO ; K⁻¹·(4,14) = (6,18) = GS → **DOGS**

**2)** FLAM=(5,11,0,12), ENGO=(4,13,6,14)
K·FLAM = (23,5,11,75) ≡ (23,5,11,23) = XFLX
K·ENGO = (27,4,19,104) ≡ (1,4,19,0) = BETA
**Cifra: XFLXBETA**
det K = −5 ≡ 21 → 21⁻¹ = 5
K⁻¹ = 5·adj K = **[[0,1,0,0],[6,21,11,5],[20,5,16,21],[21,5,15,21]]**
K⁻¹·XFLX = FLAM ; K⁻¹·BETA = ENGO → **FLAMENGO**

**3)** det A = 3(3−2) − 1(3−0) + 2(1−0) = 2 → 2⁻¹ = 3 (mod 5)
adj A ≡ [[1,4,0],[2,4,1],[1,2,2]]
A⁻¹ = 3·adj A ≡ **[[3,2,0],[1,2,3],[3,1,1]]**

**4)** e(x) = 3x + 7
O(14)→49≡23=X, B(1)→10=K, T(19)→64≡12=M, E(4)→19=T, R(17)→58≡6=G
**Cifra: XKMTG**
3⁻¹ = 9 → **d(y) = 9(y − 7) mod 26** → XKMTG → **OBTER**

**5)** E→B e T→U:
4a + b ≡ 1 ; 19a + b ≡ 20 → 15a ≡ 19 → a ≡ 19·7 ≡ 3 ; b ≡ 1 − 12 ≡ 15
**e(x) = 3x + 15 ; d(y) = 9(y − 15) mod 26**

**6)** Uma cifra de bloco cifra blocos de tamanho fixo de uma vez (Hill, DES, AES). Uma cifra de fluxo cifra bit a bit (ou letra a letra) com uma chave que muda a cada posição (LFSR, RC4).

**7)** A saída é k1, e k1⊕k2 entra em k4. Começando em (0,1,1,1):
Chave: 0111 1000 1001 101 (período 15, depois repete)
m = 1101 1111 0000 1110 0000 0001
k = 0111 1000 1001 1010 1111 0001
c = 1010 0111 1001 0100 1111 0000 → **c = A794F0h**

**8)** k₀ = 20, kᵢ = mᵢ₋₁
M: E  N  C  R  Y  P  T  I  O  N
m: 4  13 2  17 24 15 19 8  14 13
k: 20 4  13 2  17 24 15 19 8  14
y: 24 17 15 19 15 13 8  1  22 1
**Cifra: YRPTPNIBWB** → decifrando (y − k) volta **ENCRYPTION**

**9)** Na cifra monoalfabética, cada letra vira sempre a mesma letra (César, afim), então ela é quebrada por frequência. Na polialfabética, a mesma letra pode virar letras diferentes, porque usa vários alfabetos (Vigenère, auto chave).

**10)** 47 é primo, então mdc(a, 47) = 1 para todo a ≠ 0. **Só a ≡ 0 (mod 47) não é permitido.**

**11)** São as duas técnicas: as mensagens codificadas são criptografia, e esconder a verdadeira sob a pele é **esteganografia** (oculta a existência da mensagem).

**12)** x = y − 11 → **WE WILL MEET AT MIDNIGHT**

**13, 14, 15)** Os códigos em Python vão em anexo (pasta `codigos/`).
