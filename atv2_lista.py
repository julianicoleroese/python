def mostrarLista(lista):
    print("Sua lista atual é essa: ", lista)

def gravarLista(lista):
    nome_arq = input("Digite o nome do arquivo:")
    with open (nome_arq, "w") as arquivo:
        for item in lista:
            arquivo.write(item + "/n")
    print("Gravado com sucesso!", nome_arq)

def adicionarItem(lista):
    item = input("Digite algo que deseja adicionar na sua linda lista: ")
    lista.append(item)
    mostrarLista(lista)

def excluirItem(lista):
    item = input("Digite o item que voce deseja excluir da sua lista: ")
    if item in lista:
        lista.remove(item)
        mostrarLista(lista)
    else:
        print("Erro. Este item não consta em sua lista")

def main():
    lista = []

    while True:
        print("Escolha uma das opções abaixo:")
        print("1 - Adicionar item")
        print("2 - Excluir item")
        print("3 - Exibir lista")
        print("4 - Gravar lista")
        print("5 - Sair")


        opcao = input("Digite o número da opção que voce deseja: ")

        if opcao == "1":
            adicionarItem(lista)
        elif opcao == "2":
            excluirItem(lista)
        elif opcao == "3":
            mostrarLista(lista)
        elif opcao == "4":
            gravarLista(lista)
        elif opcao == "5":
            break
        else:
            print("Opção inválida. Digite novamente.")

        print()

    print("Fim da lista.")

if __name__ == "__main__":
    main()