import func as p

playlists = []


while True:
    opcao = p.menu()

    if opcao == "1":
        p.listar(playlists)
    elif opcao == "2":
        p.cadastrar(playlists)
    elif opcao == "3":
        p.excluir(playlists)
    elif opcao == "4":
        p.exportar(playlists)
    elif opcao == "5":
        print("Programa Encerrado.")
        break
    else:
        print("Opção inválida. Tente novamente.")
