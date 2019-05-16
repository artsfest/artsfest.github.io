import os
import time
count=1
# exemplo alterado de  EX_10.5.py para 10_5.py
for nome in os.listdir('lembrancas'):
    # alterar conforme sua necessidade de geração de nomes e layout de arquivos    
    dados = str(nome).split(".")
    novo = "img"+str(count)+".jpg"
    #subnumero = dados[1]
    #novo_nome = numero + "_" + subnumero + ".jpg"
    
    os.rename("lembrancas/"+nome, "lembrancas/"+novo)
    #print("arquivo " + nome + " alterado para " + novo_nome)
    print(novo)
    time.sleep(0.2)
    count+=1
