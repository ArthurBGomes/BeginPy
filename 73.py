# @cikey d3672fb6624b6c9bd68033513ef13975
# @sid 20251174010013
# @aid V7.3

import random

def sorteio_loteria():
    numeros = random.sample(range(1, 41), 25)
    numeros.sort()
    return numeros
print(sorteio_loteria())



