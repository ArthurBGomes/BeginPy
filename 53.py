# @cikey d3672fb6624b6c9bd68033513ef13975
# @sid 20251174010013
# @aid V5.3


#begin_inputs


#end_inputs
cm = 73000
pm = 255000
taipu = 12000
ccm= 1.03
cpm = 1.01
ctaipu = 1.1
ano = 2018
while pm > cm and taipu:
    pm = round(pm * cpm)
    cm = round(cm * ccm)
    taipu= round(taipu * ctaipu)
    ano += 1

print("Parnamirim sera a terceira cidade em:{}".format(ano))
print("Populacao de Parnamirim:{}".format(pm))
print("Populacao de Ceara-Mirim:{}".format(cm))	
print("Populacao de Taipu: {}".format(taipu))