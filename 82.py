# @cikey d3672fb6624b6c9bd68033513ef13975
# @sid 20251174010013
# @aid V8.2

with open("Bloco 82.txt","w+",encoding="utf-8") as linha:
    linha.write("Linha 1\n")
    linha.write("Linha 2\n")
    linha.write("Linha 3\n")
    linha.write("Linha 4\n")
    linha.write("Linha 5")
with open("Bloco 82.txt","r",encoding="utf-8") as linha:  
    linhas = linha.readlines()
print(f"A quantidade de linhas é {len(linhas)}")