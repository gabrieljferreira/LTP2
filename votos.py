votos_a_favor =0
votos_contra = 0 
invalidos = 0 
contador = 0
quantidade_de_votos =int(input("Quantos Votos Serão Computados? \n"))

while contador < quantidade_de_votos:
  print("votos_a_favor-1\n Votos_contra-2")
  voto = int(input())
  if voto ==1:
    votos_a_favor +=1
    contador +=1
  elif voto ==2 :
    votos_contra +=1
    contador +=1
  else: 
    invalidos +=1
    contador +=1

porcentagem1= votos_a_favor*quantidade_de_votos/100
porcentagem2 = votos_contra*quantidade_de_votos/100
porcentagem3 = invalidos*quantidade_de_votos/100

exibir_dic={}
exibir_dic = votos_a_favor, votos_contra, invalidos
print("votos a favor", exibir_dic[0],"porcentagem de votos a favor", porcentagem1, "votos_contra", exibir_dic[1], "porcentagem de votos_contra", porcentagem2,"invalidos", exibir_dic[2], "porcentagem de votos invalidos", porcentagem3 )

