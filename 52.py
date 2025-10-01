# @cikey d3672fb6624b6c9bd68033513ef13975
# @sid 20251174010013
# @aid V5.2


#begin_inputs
 

#end_inputs
minutos = 0
vt= 1
vl= 10
while True:
    minutos += 1
    dist =(500 + vt) * minutos
    disl = vl * minutos
    if dist > disl:
        print(round(dist > disl))


	
