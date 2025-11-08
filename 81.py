# @cikey d3672fb6624b6c9bd68033513ef13975
# @sid 20251174010013
# @aid V8.1

def Escreva(Arquivo):
    with open(Arquivo,"a") as w :
     w.write(input("Escreva:")+("\n"))

def Leia(Arquivo):
    with open(Arquivo,"r") as leia:
       conteudo = leia.readlines()
    for ler in conteudo:
        print(ler.strip())
Arquivo = "Bloco 81"
print("_______________________")
print("1 - Adicionar Frase")
print("2 - Ver Frases")
print("3 - Sair")
pergunta = input("O que voce deseja fazer? ")

while pergunta != "3":
    if pergunta == "1":
        Escreva(Arquivo)
    elif pergunta == "2":
        Leia(Arquivo)
    else:
        print("Escolha invalida")
    pergunta = input("O que voce deseja fazer? ")