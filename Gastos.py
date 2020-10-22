gastos = {}

continuar = True
if continuar == True:
  valor_do_gasto = float(input("informe um valor"))
  categoria = input("informe uma categoria").lower()
  #Verifica se a categoria já existe no dicionário 
  if categoria in gastos.keys():
    #categoria já existe
    gastos[categoria] += valor_do_gasto
  else:
    #uma nova categoria vai ser criada 
    gastos[categoria] = valor_do_gasto
    print(gastos)
    continuar = input("continuar").lower() == "s"
