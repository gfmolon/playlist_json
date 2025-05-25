import json

playlists = []


# MENU
def menu() -> str:
    print("*" * 30)
    print("MENU")
    print("*" * 30)
    print("(1) Listar")
    print("(2) Cadastrar")
    print("(3) Excluir")
    print("(4) Exportar Dados")
    print("(5) Sair")
    print("*" * 30)
    opcao = input("SELECIONE UMA OPÇÃO: ")
    return opcao


# LISTA PLAYLISTS
def listar(lista: list[str]) -> str:
    if len(lista) > 0:
        for i, playlist in enumerate(lista):
            print(f"{i} - {playlist}")
    else:
        print("Nenhuma lista cadastrada.")


# CADASTRA PLAYLISTS
def cadastrar(lista: list[str]) -> None:
    playlist = input("NOME DA PLAYLIST: ")
    lista.append(playlist)
    listar(lista)


# EXCLUIR PLAYLISTS
def excluir(lista: list[str]) -> None:
    if len(lista) < 1:
        print("Nenhuma lista cadastrada.")
    else:
        listar(lista)
        try:
            playlist = int(input("INFORME O NÚMERO PARA EXCLUIR: "))
            if 0 <= playlist < len(lista):
                lista.pop(playlist)
                listar(lista)
            else:
                print("Número da playlist não encontrado.")
        except ValueError:
            print("Por favor, insira um número válido.")


# EXPORTAR PLAYLISTS PARA JSON
def exportar(lista: list[str]) -> str:
    with open("playlists.json", "w", encoding="utf-8") as f:
        json.dump(lista, f, ensure_ascii=False, indent=4)
    print("Playlists exportadas para 'playlists.json'.")


# PROGRAMA LOOP
while True:
    opcao = menu()

    if opcao == "1":
        listar(playlists)
    elif opcao == "2":
        cadastrar(playlists)
    elif opcao == "3":
        excluir(playlists)
    elif opcao == "4":
        exportar(playlists)
    elif opcao == "5":
        print("Programa Encerrado.")
        break
    else:
        print("Opção inválida. Tente novamente.")
