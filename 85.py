# @cikey d3672fb6624b6c9bd68033513ef13975
# @sid 20251174010013
# @aid V8.5
contatos = "Bloco 85.txt"
def add(user,num):
    with open(contatos,"a",encoding="utf-8") as escreva:
        escreva.write(f"{user};{num}")
def check(contatos):
    with open(contatos,"r",encoding="utf-8") as leia:
       leia.readlines()
       for contato in contatos:
            print(contato.strip())

for n in range(3):
    user = input("Nome:")
    num = input("numero:")  
    add(user,num)

wanted = input("\n""nome que vc quer:")
if wanted in contatos:
    check(contatos)
else:
    print("não tem esse contato na lista")
