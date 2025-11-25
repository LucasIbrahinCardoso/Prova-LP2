def escreve(nome, tag, informacao):
    if tag == "w":
        with open(nome, tag, encoding="utf-8") as arquivo:
            arquivo.write(informacao)
    else:
        with open(nome, tag, encoding="utf-8") as arquivo:
            arquivo.write(informacao)

def leitor(nome):
    with open(nome, "r", encoding="utf-8") as arquivo:
        a = arquivo.readlines()
        return a
    

        