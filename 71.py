# @cikey d3672fb6624b6c9bd68033513ef13975
# @sid 20251174010013
# @aid V7.1


#begin_inputs
letras = ["a","r","t","h","u","r"]
#end_inputs
from string import ascii_lowercase

def letras_disponiveis(letras):
    return [l for l in ascii_lowercase if l not in letras]

print(letras_disponiveis(letras))

	

































