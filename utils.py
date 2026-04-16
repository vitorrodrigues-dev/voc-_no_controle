import json
import os

def salvar_json(arquivo, dados):
    with open(arquivo, "w", encoding="utf-8") as f:
        json.dump(dados, f, indent=4, ensure_ascii=False)

def carregar_json(arquivo):
    if os.path.exists(arquivo):
        with open(arquivo, "r", encoding="Utf-8") as f:
            return json.load(f)
    return None
def resposta_sim(resposta):
    return resposta.strip().lower() in ["s", "sim", "y", "yes"]

def resposta_nao(resposta):
    return resposta.strip().lower() in ["n", "nao", "não", "no"]

def perguntar_sim_nao(msg):
    while True:
        resp = input(msg).strip().lower()

        if resp in ["s", "sim"]:
            return True
        elif resp in ["n", "nao", "não"]:
            return False
        else:
            print("Digite s ou n")

def perguntar_int(msg, opcoes_validas=None):
    while True:
        valor = input(msg).strip()

        if not valor.isdigit():
            print("Digite um número válido!")
            continue

        valor = int(valor)

        if opcoes_validas and valor not in opcoes_validas:
            print("Opção inválida!")
            continue

        return valor

def perguntar_float(msg):
    while True:
        valor = input(msg).strip().replace(",", ".")

        try:
            return float(valor)
        except:
            print("Digite um número válido!")