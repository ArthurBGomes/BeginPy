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
    tartaruga = 500 + vt * minutos
    lebre = vl * minutos
    if lebre > tartaruga:
        print(minutos)
        break


	
