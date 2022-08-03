#Entrada
n = int(input())
for i in range(n):
  P1 = [int(i) for i in input().split()]
  P2 = [int(i) for i in input().split()]

#Leitura de dados
  def combinacao():
      dic = {}
      j = 0
      while j <= (len(P2) - len(P1)):
        matriz_final = []
        i = 0
        while i <= (len(P1) - 1):
          matriz_final.append(P1[i] + P2[j+i])
          i = i + 1
        pontos = 0
        max_1 = 0
        for l in matriz_final:
          if l > max_1:
            max_1 = l
        for m in matriz_final:
          if m < max_1:
            pontos = pontos + (max_1 - m)
          dic[j] = pontos
        j = j + 1
      return dic

  dic_1 = combinacao()
  P1.reverse()
  dic_2 = combinacao()
  l1_values = list(dic_1.values())
  l2_values = list(dic_2.values())
  min_dic1 = min(l1_values)
  min_dic2 = min(l2_values)

  if 0 in l1_values:
    print("Encaixe Perfeito!")
    P = "Normal"
    E = l1_values.index(min_dic1) + 1
  elif 0 in l2_values:
    print("Encaixe Perfeito!")
    P = "Invertida"
    E = l2_values.index(min_dic2) + 1
  else:
    if min_dic1 < min_dic2:
      T = min_dic1
      P = "Normal"
      E = l1_values.index(min_dic1) + 1
    elif min_dic1 > min_dic2:
      T = min_dic2
      P = "Invertida"
      E = l2_values.index(min_dic2) + 1
    else:
      T = min_dic1
      P = "Normal"
      E = l1_values.index(min_dic1) + 1
    print("Pontuacao:", T)

  print("Posicao de Encaixe:", E)
  print("Peca 1:", P)
