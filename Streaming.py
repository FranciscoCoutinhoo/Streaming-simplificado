print ("\nBem-vindo a nossa plataforma Streaming!\n")
print ("O que você está buscando hoje?\n")
print ("1 - Filmes")
print ("2 - Series")
print ("3 - Documentários")
print ("4 - Catálogo completo")

Filmes = ["O Poderoso Chefão", "A Origem", "Interestelar", "Clube da Luta", "O Lobo de Wall Street", "O Senhor dos Anéis", "O Pianista", "O Resgate do Soldado Ryan", "O Show de Truman", "O Iluminado"]
Series = ["Breaking Bad", "Game of Thrones", "Friends", "The Office", "The Big Bang Theory", "How I Met Your Mother", "The Walking Dead", "Stranger Things", "Black Mirror", "Narcos"]
Documentarios = ["The Last Dance", "Mundo Segundo os Brasileiros", "The Beatles: Eight Days a Week", "The Fog of War", "The Act of Killing", "The Look of Silence", "The Thin Blue Line", "The King of Kong", "The Imposter", "The Act of Killing"]

opcao = ""
while opcao not in ["1", "2", "3", "4"]:
    opcao = input("\nDigite número equivalente a opção desejada: ")

if opcao == "1":
    print("\nFilmes:\n")
    for filme in Filmes:
        print(filme)            
elif opcao == "2":
    print("\nSéries:\n")
    for serie in Series:
        print(serie)
elif opcao == "3":
    print("\nDocumentários:\n")
    for documentario in Documentarios: 
        print(documentario)
elif opcao == "4":
    print("\nCatálogo Completo:\n")
    print(f"{'Filmes:':<25} {'Séries:':<25} {'Documentários:'}\n")
    for filme, serie, documentario in zip(Filmes, Series, Documentarios):
        print(f"{filme:<25} {serie:<25} {documentario}")

