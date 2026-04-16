from utils import salvar_json, carregar_json, perguntar_int, perguntar_float, perguntar_sim_nao

ARQUIVO_DIETA = "dieta.json"
ARQUIVO_FICHA = "ficha.json"

alimentos = {
    # PROTEÍNAS
    "frango_cozido": {"categoria": "proteina", "kcal": 165, "prot": 31.0, "carbo": 0.0, "gord": 3.6},
    "frango_frito": {"categoria": "proteina", "kcal": 245, "prot": 28.0, "carbo": 0.0, "gord": 14.0},
    "carne_bovina_cozida": {"categoria": "proteina", "kcal": 220, "prot": 28.0, "carbo": 0.0, "gord": 11.0},
    "carne_bovina_grelhada": {"categoria": "proteina", "kcal": 250, "prot": 30.0, "carbo": 0.0, "gord": 14.0},
    "ovo_cozido": {"categoria": "proteina", "kcal": 155, "prot": 13.0, "carbo": 1.1, "gord": 11.0},
    "ovo_mexido": {"categoria": "proteina", "kcal": 149, "prot": 10.0, "carbo": 1.6, "gord": 11.0},
    "atum_natural": {"categoria": "proteina", "kcal": 132, "prot": 28.0, "carbo": 0.0, "gord": 1.0},
    "atum_oleo": {"categoria": "proteina", "kcal": 198, "prot": 25.0, "carbo": 0.0, "gord": 11.0},
    "tilapia_grelhada": {"categoria": "proteina", "kcal": 128, "prot": 26.0, "carbo": 0.0, "gord": 2.7},
    "whey_protein": {"categoria": "proteina", "kcal": 400, "prot": 80.0, "carbo": 6.0, "gord": 6.0},
    "clara_cozida": {"categoria": "proteina", "kcal": 52, "prot": 11.0, "carbo": 0.7, "gord": 0.2},
    "queijo_cottage": {"categoria": "proteina", "kcal": 98, "prot": 11.0, "carbo": 3.4, "gord": 4.3},

    # CARBOIDRATOS
    "arroz_cozido": {"categoria": "carboidrato", "kcal": 128, "prot": 2.5, "carbo": 28.0, "gord": 0.2},
    "arroz_integral_cozido": {"categoria": "carboidrato", "kcal": 124, "prot": 2.6, "carbo": 26.0, "gord": 0.9},
    "batata_doce_cozida": {"categoria": "carboidrato", "kcal": 86, "prot": 1.6, "carbo": 20.0, "gord": 0.1},
    "batata_inglesa_cozida": {"categoria": "carboidrato", "kcal": 77, "prot": 2.0, "carbo": 17.0, "gord": 0.1},
    "batata_frita": {"categoria": "carboidrato", "kcal": 312, "prot": 3.5, "carbo": 41.0, "gord": 15.0},
    "macarrao_cozido": {"categoria": "carboidrato", "kcal": 158, "prot": 5.8, "carbo": 31.0, "gord": 0.9},
    "macarrao_integral": {"categoria": "carboidrato", "kcal": 149, "prot": 6.5, "carbo": 29.0, "gord": 1.1},
    "aveia": {"categoria": "carboidrato", "kcal": 389, "prot": 17.0, "carbo": 66.0, "gord": 7.0},
    "pao_integral": {"categoria": "carboidrato", "kcal": 247, "prot": 9.0, "carbo": 41.0, "gord": 3.4},
    "pao_frances": {"categoria": "carboidrato", "kcal": 300, "prot": 8.0, "carbo": 58.0, "gord": 3.1},
    "tapioca": {"categoria": "carboidrato", "kcal": 346, "prot": 0.2, "carbo": 85.0, "gord": 0.0},
    "feijao_cozido": {"categoria": "carboidrato", "kcal": 132, "prot": 8.7, "carbo": 24.0, "gord": 0.5},
    "feijao_preto_cozido": {"categoria": "carboidrato", "kcal": 130, "prot": 8.9, "carbo": 23.0, "gord": 0.5},
    "lentilha_cozida": {"categoria": "carboidrato", "kcal": 116, "prot": 9.0, "carbo": 20.0, "gord": 0.4},
    "grao_de_bico_cozido": {"categoria": "carboidrato", "kcal": 164, "prot": 8.9, "carbo": 27.0, "gord": 2.6},
    "quinoa_cozida": {"categoria": "carboidrato", "kcal": 120, "prot": 4.4, "carbo": 22.0, "gord": 1.9},
    "cuscuz_cozido": {"categoria": "carboidrato", "kcal": 112, "prot": 3.8, "carbo": 23.0, "gord": 0.2},
    "milho_cozido": {"categoria": "carboidrato", "kcal": 86, "prot": 3.2, "carbo": 19.0, "gord": 1.2},
    "granola": {"categoria": "carboidrato", "kcal": 471, "prot": 10.0, "carbo": 64.0, "gord": 20.0},
    "inhame_cozido": {"categoria": "carboidrato", "kcal": 118, "prot": 1.5, "carbo": 28.0, "gord": 0.1},
    "mandioca_cozida": {"categoria": "carboidrato", "kcal": 125, "prot": 0.6, "carbo": 30.0, "gord": 0.3},

    # FRUTAS
    "banana": {"categoria": "fruta", "kcal": 89, "prot": 1.1, "carbo": 23.0, "gord": 0.3},
    "maca": {"categoria": "fruta", "kcal": 52, "prot": 0.3, "carbo": 14.0, "gord": 0.2},
    "morango": {"categoria": "fruta", "kcal": 32, "prot": 0.7, "carbo": 7.7, "gord": 0.3},
    "manga": {"categoria": "fruta", "kcal": 60, "prot": 0.8, "carbo": 15.0, "gord": 0.4},
    "abacate": {"categoria": "fruta", "kcal": 160, "prot": 2.0, "carbo": 9.0, "gord": 15.0},
    "laranja": {"categoria": "fruta", "kcal": 47, "prot": 0.9, "carbo": 12.0, "gord": 0.1},
    "melancia": {"categoria": "fruta", "kcal": 30, "prot": 0.6, "carbo": 7.6, "gord": 0.2},
    "uva": {"categoria": "fruta", "kcal": 69, "prot": 0.7, "carbo": 18.0, "gord": 0.2},
    "abacaxi": {"categoria": "fruta", "kcal": 50, "prot": 0.5, "carbo": 13.0, "gord": 0.1},
    "mamao": {"categoria": "fruta", "kcal": 43, "prot": 0.5, "carbo": 11.0, "gord": 0.3},
    "pera": {"categoria": "fruta", "kcal": 57, "prot": 0.4, "carbo": 15.0, "gord": 0.1},
    "pessego": {"categoria": "fruta", "kcal": 39, "prot": 0.9, "carbo": 10.0, "gord": 0.3},
    "kiwi": {"categoria": "fruta", "kcal": 61, "prot": 1.1, "carbo": 15.0, "gord": 0.5},
    "melao": {"categoria": "fruta", "kcal": 34, "prot": 0.8, "carbo": 8.2, "gord": 0.2},
    "lichia": {"categoria": "fruta", "kcal": 66, "prot": 0.8, "carbo": 17.0, "gord": 0.4},
    "framboesa": {"categoria": "fruta", "kcal": 52, "prot": 1.2, "carbo": 12.0, "gord": 0.7},
    "mirtilo": {"categoria": "fruta", "kcal": 57, "prot": 0.7, "carbo": 14.0, "gord": 0.3},
    "goiaba": {"categoria": "fruta", "kcal": 68, "prot": 2.6, "carbo": 14.0, "gord": 1.0},
    "maracuja": {"categoria": "fruta", "kcal": 97, "prot": 2.2, "carbo": 23.0, "gord": 0.7},

    # GORDURAS BOAS
    "azeite": {"categoria": "gordura", "kcal": 884, "prot": 0.0, "carbo": 0.0, "gord": 100.0},
    "amendoim": {"categoria": "gordura", "kcal": 567, "prot": 26.0, "carbo": 16.0, "gord": 49.0},
    "castanha_do_para": {"categoria": "gordura", "kcal": 659, "prot": 14.0, "carbo": 12.0, "gord": 67.0},
    "amendoim_pasta": {"categoria": "gordura", "kcal": 588, "prot": 25.0, "carbo": 20.0, "gord": 50.0},

    # LATICÍNIOS
    "leite_integral": {"categoria": "laticinios", "kcal": 61, "prot": 3.2, "carbo": 4.8, "gord": 3.3},
    "leite_desnatado": {"categoria": "laticinios", "kcal": 35, "prot": 3.4, "carbo": 5.0, "gord": 0.2},
    "iogurte_natural": {"categoria": "laticinios", "kcal": 61, "prot": 3.5, "carbo": 4.7, "gord": 3.3},
    "iogurte_grego": {"categoria": "laticinios", "kcal": 97, "prot": 9.0, "carbo": 3.6, "gord": 5.0},

    # VEGETAIS
    "brocolis_cozido": {"categoria": "vegetal", "kcal": 35, "prot": 2.4, "carbo": 7.2, "gord": 0.4},
    "espinafre_cozido": {"categoria": "vegetal", "kcal": 23, "prot": 2.9, "carbo": 3.8, "gord": 0.3},
    "cenoura_crua": {"categoria": "vegetal", "kcal": 41, "prot": 0.9, "carbo": 10.0, "gord": 0.2},
    "alface": {"categoria": "vegetal", "kcal": 15, "prot": 1.4, "carbo": 2.9, "gord": 0.2},
    "tomate": {"categoria": "vegetal", "kcal": 18, "prot": 0.9, "carbo": 3.9, "gord": 0.2},
    "pepino": {"categoria": "vegetal", "kcal": 16, "prot": 0.7, "carbo": 3.6, "gord": 0.1},
    "abobrinha_cozida": {"categoria": "vegetal", "kcal": 17, "prot": 1.2, "carbo": 3.5, "gord": 0.3},
    "couve_cozida": {"categoria": "vegetal", "kcal": 28, "prot": 2.5, "carbo": 5.6, "gord": 0.4},
    "repolho_cru": {"categoria": "vegetal", "kcal": 25, "prot": 1.3, "carbo": 5.8, "gord": 0.1},
    "chuchu_cozido": {"categoria": "vegetal", "kcal": 24, "prot": 0.8, "carbo": 5.5, "gord": 0.2},
    "beterraba_cozida": {"categoria": "vegetal", "kcal": 44, "prot": 1.7, "carbo": 10.0, "gord": 0.2},
    "couve_flor_cozida": {"categoria": "vegetal", "kcal": 23, "prot": 1.8, "carbo": 4.9, "gord": 0.1},
    "berinjela_cozida": {"categoria": "vegetal", "kcal": 35, "prot": 0.8, "carbo": 8.7, "gord": 0.2},
    "vagem_cozida": {"categoria": "vegetal", "kcal": 35, "prot": 1.9, "carbo": 7.9, "gord": 0.3},
    "quiabo_cozido": {"categoria": "vegetal", "kcal": 33, "prot": 1.9, "carbo": 7.5, "gord": 0.2},
}

def listar_por_categoria(categoria):
    return [nome for nome, dados in alimentos.items() if dados["categoria"] == categoria]

def checar_reset_diario():
    hoje = str(date.today())
    dados = carregar_json(ARQUIVO_DIETA)

    if dados and dados.get("data") != hoje:
        dados_zerados = {
            "data": hoje,
            "total_calorias": 0,
            "total_proteina": 0,
            "total_carbo": 0,
            "total_gordura": 0,
            "refeicoes": []
        }
        salvar_json(ARQUIVO_DIETA, dados_zerados)
        print("✔ Novo dia! Dieta resetada.")

def menu_dieta():
    checar_reset_diario()
    while True:
        print("\n1 - Registrar refeição")
        print("2 - Mostrar progresso")
        print("3 - Excluir refeição")
        print("4 - Usar Dieta Pronta")
        print("5 - Voltar")

        op = perguntar_int("Escolha: ", [1, 2, 3, 4, 5])

        if op == 1:
            registrar_refeicao()
        elif op == 2:
            mostrar_progresso()
        elif op == 3:
            excluir_refeicao()
        elif op == 4:
            usar_dieta_pronta()
        else:
            break


from datetime import date

def registrar_refeicao():
    hoje = str(date.today())
    dados = carregar_json(ARQUIVO_DIETA)

    if not dados or dados.get("data") != hoje:
        dados = {
            "data": hoje,
            "total_calorias": 0,
            "total_proteina": 0,
            "total_carbo": 0,
            "total_gordura": 0,
            "refeicoes": []
        }
    else:
        dados.setdefault("total_proteina", 0)
        dados.setdefault("total_carbo", 0)
        dados.setdefault("total_gordura", 0)
        dados.setdefault("refeicoes", [])

    categorias = {
        1:"proteina",
        2:"carboidrato",
        3:"fruta",
        4:"gordura",
        5:"vegetal",
        6:"laticinios"
    }

    nome_ref = input("Nome desta refeição (ex: almoço, jantar): ").strip()
    while True:
        print("\n1-Proteina 2-Carbo 3-Fruta 4-Gordura 5-Vegetal 6-Laticinios")
        cat = perguntar_int("Escolha: ", [1,2,3,4,5,6])

        lista = listar_por_categoria(categorias[cat])

        for i, a in enumerate(lista,1):
            print(f"{i} - {a}")

        escolha = perguntar_int("Escolha: ", list(range(1,len(lista)+1))) - 1
        alimento = lista[escolha]

        gramas = perguntar_float("Gramas: ")
        info = alimentos[alimento]

        kcal = (info["kcal"] / 100) * gramas
        prot = (info["prot"] / 100) * gramas
        carbo = (info["carbo"] / 100) * gramas
        gord = (info["gord"] / 100) * gramas

        if "total_proteina" not in dados:
            dados["total_proteina"] = 0
            dados["total_carbo"] = 0
            dados["total_gordura"] = 0

        dados["total_calorias"] += kcal
        dados["total_proteina"] += prot
        dados["total_carbo"] += carbo
        dados["total_gordura"] += gord

        dados["refeicoes"].append({
            "refeicao": nome_ref,
            "nome": alimento,
            "gramas": gramas,
            "kcal": kcal,
            "prot": prot,
            "carbo": carbo,
            "gord": gord
        })
        print(f"\nAdicionado: {alimento}")
        print(f"Kcal: {kcal:.0f} | Prot: {prot:.1f}g | Carbo: {carbo:.1f}g | Gord: {gord:.1f}g")

        if not perguntar_sim_nao("Continuar? (s/n): "):
            break

    salvar_json(ARQUIVO_DIETA, dados)  # <- estava faltando isso!
    print("Refeição salva!")

def excluir_refeicao():
    dados = carregar_json(ARQUIVO_DIETA)

    if not dados or not dados["refeicoes"]:
        print("Nenhuma refeição registrada.")
        return

    print("\n=== REFEIÇÕES DO DIA ===")
    for i, r in enumerate(dados["refeicoes"], 1):
        print(f"{i} - [{r.get('refeicao', 'sem nome')}] {r['nome']} | {r['gramas']}g | {r['kcal']:.0f} kcal")

    escolha = perguntar_int("Qual deseja excluir? ", list(range(1, len(dados["refeicoes"]) + 1))) - 1

    removida = dados["refeicoes"].pop(escolha)

    dados["total_calorias"] -= removida["kcal"]
    dados["total_proteina"] -= removida["prot"]
    dados["total_carbo"]    -= removida["carbo"]
    dados["total_gordura"]  -= removida["gord"]

    salvar_json(ARQUIVO_DIETA, dados)
    print(f"{removida['nome']} removido!")

def usar_dieta_pronta():
    hoje = str(date.today())
    dados = carregar_json(ARQUIVO_DIETA)

    if not dados or dados.get("data") != hoje:
        dados = {
            "data": hoje,
            "total_calorias": 0,
            "total_proteina": 0,
            "total_carbo": 0,
            "total_gordura": 0,
            "refeicoes": []
        }
    else:
        dados.setdefault("total_proteina", 0)
        dados.setdefault("total_carbo", 0)
        dados.setdefault("total_gordura", 0)
        dados.setdefault("refeicoes", [])

    nomes_refeicoes = ["Café da manhã", "Lanche da manhã", "Almoço", "Lanche da tarde", "Jantar", "Ceia"]

    print("\n" + "="*50)
    print("=== USAR DIETA PRONTA ===")
    print("="*50)
    print("Vamos montar suas refeições do dia uma por uma.")

    dieta_temp = []

    for nome_refeicao in nomes_refeicoes:
        print(f"\n{'='*50}")
        print(f"  {nome_refeicao.upper()}")
        print(f"{'='*50}")

        if not perguntar_sim_nao(f"Deseja adicionar '{nome_refeicao}'? (s/n): "):
            continue

        itens_refeicao = []
        kcal_ref = prot_ref = carbo_ref = gord_ref = 0

        while True:
            categorias = {
                1: "proteina",
                2: "carboidrato",
                3: "fruta",
                4: "gordura",
                5: "vegetal",
                6: "laticinios"
            }

            print("\n1-Proteina  2-Carbo  3-Fruta  4-Gordura  5-Vegetal  6-Laticinios")
            cat = perguntar_int("Categoria: ", [1, 2, 3, 4, 5, 6])

            lista = listar_por_categoria(categorias[cat])
            for i, a in enumerate(lista, 1):
                print(f"{i} - {a}")

            escolha = perguntar_int("Escolha o alimento: ", list(range(1, len(lista) + 1))) - 1
            alimento = lista[escolha]

            gramas = perguntar_float("Gramas: ")
            info = alimentos[alimento]

            kcal = (info["kcal"] / 100) * gramas
            prot = (info["prot"] / 100) * gramas
            carbo = (info["carbo"] / 100) * gramas
            gord = (info["gord"] / 100) * gramas

            itens_refeicao.append({
                "nome": alimento,
                "gramas": gramas,
                "kcal": kcal,
                "prot": prot,
                "carbo": carbo,
                "gord": gord
            })

            kcal_ref += kcal
            prot_ref += prot
            carbo_ref += carbo
            gord_ref += gord

            print(f"  ✔ {alimento}: {kcal:.0f} kcal | P:{prot:.1f}g C:{carbo:.1f}g G:{gord:.1f}g")

            if not perguntar_sim_nao("Adicionar mais alimento nesta refeição? (s/n): "):
                break

        print(f"\n--- Resumo: {nome_refeicao} ---")
        for item in itens_refeicao:
            print(f"  {item['nome']}: {item['gramas']}g | {item['kcal']:.0f} kcal")
        print(f"  TOTAL: {kcal_ref:.0f} kcal | Prot: {prot_ref:.1f}g | Carbo: {carbo_ref:.1f}g | Gord: {gord_ref:.1f}g")

        dieta_temp.append({
            "refeicao": nome_refeicao,
            "itens": itens_refeicao,
            "kcal": kcal_ref,
            "prot": prot_ref,
            "carbo": carbo_ref,
            "gord": gord_ref
        })

    if not dieta_temp:
        print("\nNenhuma refeição adicionada.")
        return

    print("\n" + "="*50)
    print("=== RESUMO GERAL DA DIETA ===")
    print("="*50)

    total_kcal = total_prot = total_carbo = total_gord = 0

    for ref in dieta_temp:
        print(f"\n{ref['refeicao']}:")
        for item in ref["itens"]:
            print(f"  - {item['nome']}: {item['gramas']}g")
        print(f"  Subtotal: {ref['kcal']:.0f} kcal | P:{ref['prot']:.1f}g | C:{ref['carbo']:.1f}g | G:{ref['gord']:.1f}g")

        total_kcal  += ref["kcal"]
        total_prot  += ref["prot"]
        total_carbo += ref["carbo"]
        total_gord  += ref["gord"]

    print(f"\n{'='*50}")
    print(f"TOTAL DO DIA")
    print(f"  Calorias:    {total_kcal:.0f} kcal")
    print(f"  Proteína:    {total_prot:.1f} g")
    print(f"  Carboidrato: {total_carbo:.1f} g")
    print(f"  Gordura:     {total_gord:.1f} g")
    print("="*50)

    if not perguntar_sim_nao("\nSalvar esta dieta no registro do dia? (s/n): "):
        print("Dieta descartada.")
        return

    # Salva todos os itens no registro do dia
    for ref in dieta_temp:
        for item in ref["itens"]:
            dados["refeicoes"].append(item)
            dados["total_calorias"] += item["kcal"]
            dados["total_proteina"] += item["prot"]
            dados["total_carbo"]    += item["carbo"]
            dados["total_gordura"]  += item["gord"]

    salvar_json(ARQUIVO_DIETA, dados)
    print("\nDieta salva com sucesso!")

def mostrar_progresso():
    dieta = carregar_json(ARQUIVO_DIETA)
    ficha = carregar_json(ARQUIVO_FICHA)

    if not dieta:
        print("Nada registrado.")
        return

    total = dieta["total_calorias"]
    meta = ficha["meta"] if ficha else 0
    meta_prot = (meta * 0.30) / 4
    meta_carbo = (meta * 0.45) / 4
    meta_gord = (meta * 0.25) / 9

    print("\n=== PROGRESSO ===")
    print(f"Calorias:    {total:.0f} / {meta:.0f} kcal  |  Restante: {meta - total:.0f} kcal")

    if "total_proteina" in dieta:
        prot = dieta['total_proteina']
        carbo = dieta['total_carbo']
        gord = dieta['total_gordura']

        print(f"Proteína:    {prot:.1f} / {meta_prot:.1f} g  |  Restante: {meta_prot - prot:.1f} g")
        print(f"Carboidrato: {carbo:.1f} / {meta_carbo:.1f} g  |  Restante: {meta_carbo - carbo:.1f} g")
        print(f"Gordura:     {gord:.1f} / {meta_gord:.1f} g  |  Restante: {meta_gord - gord:.1f} g")