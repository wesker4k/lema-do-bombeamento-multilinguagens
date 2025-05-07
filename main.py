# Linguagem 1: L = { a^n b^n | n ≥ 0 } (não regular)
def linguagem1(w):
    a_count = 0
    i = 0
    while i < len(w) and w[i] == 'a':
        a_count += 1
        i += 1
    b_count = 0
    while i < len(w) and w[i] == 'b':
        b_count += 1
        i += 1
    return i == len(w) and a_count == b_count

# Linguagem 2: L = { a^n b^m | n, m ≥ 0 } (regular)
def linguagem2(w):
    i = 0
    while i < len(w) and w[i] == 'a':
        i += 1
    while i < len(w) and w[i] == 'b':
        i += 1
    return i == len(w)

# Linguagem 3: L = { ww | w ∈ {a, b}* } (não regular)
def linguagem3(w):
    n = len(w)
    if n % 2 != 0:
        return False
    mid = n // 2
    return w[:mid] == w[mid:]

# Função principal de teste do lema
def testar_lema_bombeamento(linguagem, p, w):
    if len(w) < p:
        print("Erro: |w| deve ser maior ou igual a p.")
        return

    print(f"\nTestando w = '{w}' com p = {p}")
    encontrou_quebra = False

    for i in range(1, p + 1):
        for j in range(i):
            x = w[:j]
            y = w[j:i]
            z = w[i:]
            if y == "":
                continue

            print(f"\nTestando divisão: x='{x}', y='{y}', z='{z}'")

            for i_val in [0, 1, 2]:
                teste = x + y * i_val + z
                pertence = linguagem(teste)
                print(f"  i={i_val}: '{teste}' -> {'PERTENCE' if pertence else 'NÃO PERTENCE'}")
                if not pertence:
                    encontrou_quebra = True
                    print("  >> Lema FALHA para esta divisão.")
                    break

            if encontrou_quebra:
                break
        if encontrou_quebra:
            break

    if encontrou_quebra:
        print("\nConclusão: A linguagem NÃO PODE ser regular (lema falha).")
    else:
        print("\nConclusão: Nenhuma quebra encontrada. O lema não foi violado com esta entrada.")


def escolher_linguagem():
    print("Escolha uma linguagem para testar:")
    print("1 - L = { a^n b^n | n ≥ 0 } (não regular)")
    print("2 - L = { a^n b^m | n, m ≥ 0 } (regular)")
    print("3 - L = { ww | w ∈ {a,b}* } (não regular)")
    escolha = input("Digite 1, 2 ou 3: ")

    if escolha == "1":
        return linguagem1
    elif escolha == "2":
        return linguagem2
    elif escolha == "3":
        return linguagem3
    else:
        print("Escolha inválida.")
        return escolher_linguagem()

def main():
    linguagem = escolher_linguagem()
    w = input("\nDigite a cadeia w: ")
    p = int(input("Digite o valor de bombeamento p (p ≤ |w|): "))
    testar_lema_bombeamento(linguagem, p, w)


if __name__ == "__main__":
    main()
