# @cikey d3672fb6624b6c9bd68033513ef13975
# @sid 20251174010013
# @aid V6.5
import random

def megasena():
    nummegasena = random.randint(1, 100)
    while True:
        palpite = int(input("Digite um número entre 1 e 100: "))

        if palpite < nummegasena:
            print("O número secreto é MAIOR.")
        elif palpite > nummegasena:
            print("O número secreto é MENOR.")
        else:
            print(f"Parabéns! Você acertou! O número secreto era {nummegasena}.")
            break

megasena()