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

with open("livros_avaliacao.txt", "w", encoding="utf-8") as arq:
    for um in range(len(texto)):
        arq.write(f"{anos[um]}, {nomes[um]}, {autor[um]}, {notas[um]}, {status[um]}\n")
    
avaliadosPrincipal = funcoes.leitor("livros_avaliacao.txt")
avaliados = []
for i in range(len(avaliadosPrincipal)):
    avaliados.append(avaliadosPrincipal[i].removesuffix("\n"))
for j in range(len(avaliados)):
    avaliados[j] = avaliados[j].split(",")

verificando = []
for teste in range(len(avaliados)):
    if avaliados[teste][4] != ' fila':
        verificando.append([avaliados[teste][1], avaliados[teste][3]])

for i in range(len(verificando)):
    verificando[i][1] = int(verificando[i][1])

notasLimpas = []
for lal in range(len(verificando)):
    notasLimpas.append(verificando[lal][1])

notasLimpas = sorted(notasLimpas, reverse=True)

notasFinais= []
for la in range(0, 5, 1):
    notasFinais.append(notasLimpas[la])

listaFinal = []
for ti in range(9):
    for le in range(len(verificando)):
        for teste in range(len(notasFinais)):
            if notasFinais[teste] != verificando[le]:
                notasFinais.remove(notasFinais[teste])
            else:
                listaFinal.append(verificando[le][0])
                if len(listaFinal) == 5:
                    break
print(listaFinal)