# @cikey d3672fb6624b6c9bd68033513ef13975
# @sid 20251174010013
# @aid V5.3


#begin_inputs
cm = 73000
pm = 255000
taipu = 12000
ccm= 1.03
cpm = 1.01
ctaipu = 1.1
ano = 2018

#end_inputs

while pm > (cm + taipu):
    pm = round(pm * cpm)
    cm = round(cm * ccm)
    taipu= round(taipu * ctaipu)
    ano += 1

print(" em {}, a população de Parnamirim ({}) é menor que a de ceara mirim ({}) e a de taipu ({}) juntas ".format(ano,pm,cm,taipu))

	
