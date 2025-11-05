# @cikey d3672fb6624b6c9bd68033513ef13975
# @sid 20251174010013
# @aid V8.1

def Escreva(Arquivo):
    with open(Arquivo,"a") as w:
     w.write(input("Escreva:"))

def Leia(Arquivo):
    with open(Arquivo,"r") as leia:
        leia.read()
    for ler in leia:
        print(ler.strip())
    print(ler)
Arquivo = "Bloco 81"
print("_______________________")
print("1 - Adicionar Frase")
print("2 - Ver Frases")
print("3 - Sair")
pergunta = input("O que você deseja fazer? ")

while pergunta != "3":
    if pergunta == "1":
        Escreva(Arquivo)
    elif pergunta == "2":
        Leia(Arquivo)
    else:
        print("Escolha inválida")
    pergunta = input("O que você deseja fazer? ")