from ficha import ficha_usuario
from dieta import menu_dieta

def main():
    while True:
        print("=" * 60)
        print("MENU")
        print("=" * 60)
        print("1 - Criar / Ver ficha")
        print("2 - Dieta")
        print("3 - Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            ficha_usuario()
        elif opcao == "2":
            menu_dieta()
        elif opcao == "3":
            print("Saindo...")
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    main()
