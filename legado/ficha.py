from utils import salvar_json, carregar_json, perguntar_int, perguntar_float, perguntar_sim_nao

ARQUIVO_FICHA = "ficha.json"

def pausar():
    input("\nPressione ENTER para voltar ao menu...")

def ficha_usuario():
    ficha = carregar_json(ARQUIVO_FICHA)

    if ficha:
        print("\n" + "="*50)
        print("=== SUA FICHA ===")
        print("="*50)
        print(f"Nome: {ficha['nome']}")
        print(f"Idade: {ficha['idade']}")
        print(f"Peso atual: {ficha['peso_atual']}")
        print(f"Peso desejado: {ficha['peso_desejado']}")
        print(f"Altura: {ficha['altura']}")
        print(f"Sexo: {ficha['sexo']}")
        print(f"Meta: {ficha['meta']:.0f} kcal")

        if ficha["objetivo"] == 1:
            print("Objetivo: Cut")
        elif ficha["objetivo"] == 2:
            print("Objetivo: Bulk")
        else:
            print("Objetivo: Manutenção")

        print("="*50)

        if not perguntar_sim_nao("\nDeseja editar a ficha? (s/n): "):
            pausar()
            return ficha

    print("\n" + "="*50)
    print("--- CRIAR / EDITAR FICHA ---")
    print("="*50)

    nome = input("Nome: ")
    idade = perguntar_int("Idade: ")
    peso_atual = perguntar_float("Peso atual: ")
    peso_desejado = perguntar_float("Peso desejado: ")
    altura = perguntar_float("Altura (cm): ")

    # SEXO VALIDADO
    while True:
        sexo = input("Sexo (M/F): ").strip().upper()
        if sexo in ["M", "F"]:
            break
        print("Digite M ou F")

    print("""
Nível de atividade física:
1 - Baixo
2 - Médio
3 - Bom
4 - Ótimo
""")

    nivel = perguntar_int("Escolha: ", [1,2,3,4])

    print("""
Objetivo:
1 - Cut
2 - Bulk
3 - Manutenção
""")

    objetivo = perguntar_int("Escolha: ", [1,2,3])

    # TMB (AGORA CERTO PRA HOMEM E MULHER)
    if sexo == "M":
        tmb = 88.36 + (13.4 * peso_atual) + (4.8 * altura) - (5.7 * idade)
    else:
        tmb = 447.6 + (9.2 * peso_atual) + (3.1 * altura) - (4.3 * idade)

    # FATOR ATIVIDADE
    fatores = {
        1: 1.2,
        2: 1.375,
        3: 1.55,
        4: 1.725
    }

    tmb_total = tmb * fatores[nivel]

    # META
    if objetivo == 1:
        meta = tmb_total - 500
    elif objetivo == 2:
        meta = tmb_total + 400
    else:
        meta = tmb_total

    # TEMPO ESTIMADO
    diferenca = abs(peso_desejado - peso_atual)
    total_semanas = 0

    if objetivo == 1:
        total_semanas = (7700 * diferenca) / (500 * 7)
    elif objetivo == 2:
        total_semanas = (7700 * diferenca) / (400 * 7)

    # RESULTADO
    print("\n" + "="*50)
    print("RESULTADO")
    print("="*50)
    print(f"TMB: {tmb:.0f} kcal")
    print(f"Gasto total: {tmb_total:.0f} kcal")
    print(f"Meta diária: {meta:.0f} kcal")

    if objetivo == 3:
        print("Manutenção — sem prazo")
    else:
        print(f"{total_semanas:.1f} semanas estimadas")

    print("="*50)

    dados = {
        "nome": nome,
        "idade": idade,
        "sexo": sexo,
        "peso_atual": peso_atual,
        "peso_desejado": peso_desejado,
        "altura": altura,
        "nivel_atividade": nivel,
        "objetivo": objetivo,
        "meta": meta,
        "total_semanas": total_semanas
    }

    salvar_json(ARQUIVO_FICHA, dados)

    print("\nFicha salva com sucesso!")
    pausar()

    return dados