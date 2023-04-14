import pandas as pd
from selenium import webdriver

tabela = pd.read_excel(r'coloque o caminho da tabela base')
nav = webdriver.Chrome()
for linha in tabela.index:
    produto = tabela.loc[linha, 'Produto']
    produto = produto.replace('ó', 'o').replace('é', 'e').replace('á', 'a').replace('ã', 'a').replace('ç', 'c').replace('ú', 'u')
    nav.get(f'https://www.melhorcambio.com/{produto}-hoje')
    valor = nav.find_element('xpath', '//*[@id="comercial"]').get_attribute('value')
    valor = valor.replace('.', '').replace(',', '.')    
    valor = float(valor)
    tabela.loc[linha, 'Preço Atual'] = valor
    if tabela.loc[linha, 'Preço Atual'] <= tabela.loc[linha, 'Preço Ideal']:
        tabela.loc[linha, 'Comprar'] = 'Sim'
    else:
        tabela.loc[linha, 'Comprar'] = 'Não'
print(tabela)
tabela.to_excel('new_commodities.xlsx', index=False)
nav.quit()
