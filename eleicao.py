import os
import requests
import pandas as pd
import json


data = requests.get(
     'https://resultados.tse.jus.br/oficial/ele2022/544/dados-simplificados/br/br-c0001-e000544-r.json')
json_data = json.loads(data.content)
tempo = 60
candidato=[]
partido = []
votos=[]
porcentagem=[]
pa=json_data['pst']
os.system('cls')

for informacoes in json_data['cand']:
        
    candidato.append(informacoes['nm'])
    votos.append(informacoes['vap'])
    porcentagem.append(informacoes['pvap'])
    
   
df_eleicao = pd.DataFrame(list(zip(candidato,votos,porcentagem)),columns=['Candidato','N° Votos','Porcentagem'])
print("Porcentagem das urnas apuradas: ",pa,"%")
print(df_eleicao)
    
