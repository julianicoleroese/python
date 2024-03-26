def adicionarItem(lista):
    item = input("Digite oque deseja adicionar: ")
    lista.append(item)
    print("Item adicionado.")
    exibirLista(lista)

def excluirItem(lista):
    item = input("Digite oque deseja excluir: ")
    if item in lista:
        lista.remove(item)
        print("Item removido.")
    else:
        print("Não está na lista.")
    exibirLista(lista)

def exibirLista(lista):
    print("Atual Lista:", lista)

def main():
    lista = []
    while True:
        print("=== OPÇÕES DA LISTA ===")
        print("1. ADICIONAR ITEM.")
        print("2. EXCLUIR ITEM.")
        print("3. EXIBIR LISTA.")
        print("4. SAIR.")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            adicionarItem(lista)
        elif opcao == "2":
            excluirItem(lista)
        elif opcao == "3":
            exibirLista(lista)
        elif opcao == "4":
            print("Tchau.")
            break
        else:
            print("Número inválido, tente novamente.")

if __name__ == "__main__":
    main()