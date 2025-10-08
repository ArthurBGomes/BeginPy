# @cikey d3672fb6624b6c9bd68033513ef13975
# @sid 20251174010013
# @aid V6.2


#begin_inputs
n = int(input(":"))
#end_inputs
def escada(n):
    for i in range(1, n + 1):
        for j in range(1, i + 1):
            print(j, end=" ")
        print()

escada(n)
