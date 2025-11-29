import funcoes


avaliadosPrincipal = funcoes.leitor("livros_avaliacao.txt")

avaliados = []
for linha in avaliadosPrincipal:
    linha = linha.removesuffix("\n")
    avaliados.append(linha.split(","))

validos = []
for item in avaliados:
    status = item[4].strip()     # remove espaços
    if status == "lido" or status == "lendo":
        nome = item[1].strip()
        nota = int(item[3].strip())
        ano = item[0].strip()
        autor = item[2].strip()
        validos.append([nome, nota, ano, autor])

notas = []
for v in validos:
    notas.append(v[1])

notas_ordenadas = sorted(notas, reverse=True)

# Pegar as 5 maiores
top5_notas = notas_ordenadas[:5]

recomendados = []
for nota in top5_notas:
    for livro in validos:
        if livro[1] == nota and livro not in recomendados:
            recomendados.append(livro)
            break
    if len(recomendados) == 5:
        break

with open("livros_recomendados.txt", "w", encoding="utf-8") as arq:
    for item in recomendados:
        arq.write(f"{item[2]}, {item[0]}, {item[3]}, {item[1]}\n")
