# @cikey d3672fb6624b6c9bd68033513ef13975
# @sid 20251174010013
# @aid V2.4

#begin_inputs
 
valor_compra=int(input("Digite o valor da sua compra:"))
 
 #end_inputs
 
a_vista= valor_compra * 0.09

parcelado_5= valor_compra/5

valor_do_juros= valor_compra * 1.17
parcelado_10= valor_do_juros/10 

print("{}".format( valor_compra - a_vista))
print("{}".format(parcelado_5))
print("{}".format(round(parcelado_10, 2 )))