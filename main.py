def pertence_anbn(w: str) -> bool:
    """
    Verifica se a palavra w pertence à linguagem L = { aⁿbⁿ | n ≥ 0 }.
    """
    n = len(w)
    a_count = 0
    for c in w:
        if c == 'a':
            a_count += 1
        else:
            break
    return w == 'a' * a_count + 'b' * a_count

def pertence_anbm(w: str) -> bool:
    """
    Verifica se a palavra w pertence à linguagem L = { aⁿbᵐ | n, m ≥ 0 }.
    """
    i = 0
    while i < len(w) and w[i] == 'a':
        i += 1
    while i < len(w) and w[i] == 'b':
        i += 1
    return i == len(w)

def pertence_ww(w: str) -> bool:
    """
    Verifica se w pertence à linguagem L = { ww | w ∈ {a, b}* }.
    """
    n = len(w)
    if n % 2 != 0:
        return False
    meio = n // 2
    return w[:meio] == w[meio:]

# Dicionário de linguagens disponíveis (atualizado)
linguagens_disponiveis = {
    '1': {
        'descricao': 'L = { aⁿbⁿ | n ≥ 0 }',
        'funcao': pertence_anbn
    },
    '2': {
        'descricao': 'L = { aⁿbᵐ | n, m ≥ 0 }',
        'funcao': pertence_anbm
    },
    '3': {
        'descricao': 'L = { ww | w ∈ {a, b}* }',
        'funcao': pertence_ww
    }
}

def aplicar_lema_bombeamento(w: str, p: int, linguagem_func) -> None:
    """
    Simula o lema do bombeamento para uma linguagem específica.
    """
    print(f"\nPalavra w: '{w}' (|w| = {len(w)})")
    print(f"Comprimento mínimo de bombeamento p: {p}\n")

    encontrou_quebra = False

    for i in range(1, p + 1):
        x = w[:i]
        for j in range(1, p - i + 2):  # Garante |xy| ≤ p e |y| ≥ 1
            if i + j > len(w):
                continue
            y = w[i:i+j]
            z = w[i+j:]

            print(f"Divisão {i}-{j}: x='{x}', y='{y}', z='{z}'")

            for k in [0, 1, 2]:
                nova = x + (y * k) + z
                pertence = linguagem_func(nova)
                status = "PERTENCE" if pertence else "NÃO PERTENCE"
                print(f"  i={k}: {nova} → {status}")

                if not pertence:
                    encontrou_quebra = True
                    print("  → Quebra detectada! ←")

            print("-" * 50)

    if encontrou_quebra:
        print("\n✅ Conclusão: A linguagem NÃO É REGULAR (lema violado).")
    else:
        print("\n❌ Conclusão: Nenhuma quebra encontrada. O lema não foi suficiente.")

if __name__ == "__main__":
    # Seleção da linguagem
    print("Selecione a linguagem:")
    for key in linguagens_disponiveis:
        print(f"{key}. {linguagens_disponiveis[key]['descricao']}")
    opcao = input("Opção: ").strip()

    if opcao not in linguagens_disponiveis:
        print("Opção inválida!")
        exit()

    linguagem = linguagens_disponiveis[opcao]
    funcao_verificacao = linguagem['funcao']
    print(f"\n💡 Linguagem selecionada: {linguagem['descricao']}")

    # Entrada da cadeia w
    w = input("\nDigite a cadeia w (ex: aabb para L1): ").strip()
    if not funcao_verificacao(w):
        print(f"Erro: '{w}' não pertence à linguagem!")
        exit()

    # Entrada do p
    while True:
        try:
            p = int(input("Digite p (comprimento de bombeamento): "))
            if p <= 0:
                print("p deve ser positivo!")
            elif len(w) < p:
                print(f"Erro: |w|={len(w)} deve ser ≥ p={p}!")
            else:
                break
        except ValueError:
            print("Digite um número inteiro válido!")

    # Executa a análise
    aplicar_lema_bombeamento(w, p, funcao_verificacao)
