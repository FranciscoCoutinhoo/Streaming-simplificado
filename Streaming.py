print ("\nBem-vindo a nossa plataforma Streaming!\n")
print ("O que você está buscando hoje?\n")
print ("1 - Filmes")
print ("2 - Series")
print ("3 - Catálogo completo")



Filmes = ["O Poderoso Chefão", "A Origem", "Interestelar", "Clube da Luta", "O Lobo de Wall Street", "O Senhor dos Anéis", "O Pianista", "O Resgate do Soldado Ryan", "O Show de Truman", "O Iluminado"]
Series = ["Breaking Bad", "Game of Thrones", "Friends", "The Office", "The Big Bang Theory", "How I Met Your Mother", "The Walking Dead", "Stranger Things", "Black Mirror", "Narcos"]


opcao = ""
while opcao not in ["0", "1", "2", "3"]:
    opcao = input("\nDigite número equivalente a opção desejada: ")

if opcao == "1":
    print("\nFilmes:\n")
    for filme in Filmes:
        print(filme)
    print("\n0 - Voltar ao início")
    opcao = input("\nDigite número equivalente a opção desejada: ")
    if opcao == "0":
       
        print ("\nBem-vindo a nossa plataforma Streaming!\n")
        print ("O que você está buscando hoje?\n")
        print ("1 - Filmes")
        print ("2 - Series")
        print ("3 - Catálogo completo")
        
elif opcao == "2":
    print("\nSéries:\n")
    for serie in Series:
        print(serie)
    print("\n0 - Voltar ao início")
    opcao = input("\nDigite número equivalente a opção desejada: ")
    if opcao == "0":
        
        print ("\nBem-vindo a nossa plataforma Streaming!\n")
        print ("O que você está buscando hoje?\n")
        print ("1 - Filmes")
        print ("2 - Series")
        print ("3 - Catálogo completo")
       
elif opcao == "3":
    print("\nCatálogo Completo:\n")
    print(f"{'Filmes:':<25} {'Séries:'}\n")
    for filme, serie, in zip(Filmes, Series,):
        print(f"{filme:<25} {serie}")
    print("\n0 - Voltar ao início")
    opcao = input("\nDigite número equivalente a opção desejada: ")
    if opcao == "0":
       
        print ("\nBem-vindo a nossa plataforma Streaming!\n")
        print ("O que você está buscando hoje?\n")
        print ("1 - Filmes")
        print ("2 - Series")
        print ("3 - Catálogo completo")
        
