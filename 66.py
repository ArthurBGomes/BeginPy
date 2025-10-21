# @cikey d3672fb6624b6c9bd68033513ef13975
# @sid 20251174010013
# @aid V6.6
import random

def megasena():
    nummegasena = random.randint(1, 1000)
    trys = 0
    while True:
        palpite = int(input("Digite um numero entre 1 e 1000: "))
        trys += 1
        if trys >= 6:
            print("acabou suas tentativas")
            break

        if palpite < nummegasena:
            print("O numero secreto e MAIOR.")
        elif palpite > nummegasena:
            print("O numero secreto e MENOR.")
        else:
            print(f"Parabens! Você acertou! O numero secreto era {nummegasena}.")
            break
       
megasena()