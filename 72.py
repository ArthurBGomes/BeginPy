# @cikey d3672fb6624b6c9bd68033513ef13975
# @sid 20251174010013
# @aid V7.2


#begin_inputs
letras = ['a', 'r', 's', 't',"f", 'u',"r","h"]
palavra = 'rafa'

#end_inputs

def advinhou_palavra(letras, palavra):
    for letra in palavra:
        if letra not in letras:
            return False
    return True
print(advinhou_palavra(letras, palavra))
