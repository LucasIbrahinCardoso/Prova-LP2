import funcoes

textoPrincipal = funcoes.leitor("livros.txt")
textoLimpo= []
texto = []
for i in range(len(textoPrincipal)):
    textoLimpo.append(textoPrincipal[i].removesuffix("\n"))
for j in range(len(textoLimpo)):
    texto.append(textoLimpo[j].split(","))
nomes = []
notas = []
anos = []
autor = []
for a in range(len(texto)):
    nomes.append(texto[a][1].removeprefix(" "))
    anos.append(texto[a][0])
    autor.append(texto[a][2])
    while True:
        nota_ = int(input(f"Digite uma nota para o filme {nomes[a]}: "))
        if nota_ > 0 and nota_ <= 10:
            notas.append(nota_)
            break
status = []
for a in range(len(nomes)):
    while True:
        leitura = input(f"Digite qual o status de leitura de {nomes[a]}: ")
        if leitura == "lido" or leitura == "lendo" or leitura == "fila":
            status.append(leitura)
            break
        else:
            print("Resposta inválida, tente 'lido', 'lendo' ou 'fila':")

with open("livros_avaliacao.txt", "w") as arq:
    for um in range(len(texto)):
        arq.write(f"{anos[um]}, {nomes[um]}, {autor[um]}, {notas[um]}, {status[um]}")