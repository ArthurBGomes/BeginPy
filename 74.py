# @cikey d3672fb6624b6c9bd68033513ef13975
# @sid 20251174010013
# @aid V7.4
tel = {}

for n in range(3):
    user = input("Nome:")
    num = input("numero:")
    tel[user] = num    
print(f"{tel}",)
wanted = input("\n""nome que vc quer:")
if wanted in tel:
    print(f"o nome {wanted} está na lista de telefone{tel[user]}")
else:
    print("não tem esse contato na lista")
