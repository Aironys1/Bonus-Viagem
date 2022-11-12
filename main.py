# BIBLIOTECAS A SEREM INSTALADAS
# pandas
# openpyxl
# twilio

import pandas as pd  # importando a biblioteca panda
from twilio.rest import Client # importando a biblioteca para envio de mensagens


# Seu SID da sua conta em twilio
account_sid = "AC44881680a3d66e95d42b69645a84ecf4"
# Seu token de autenticação em twilio
auth_token  = "06f7da1a05a4c474a7b86f633290f3a0"
client = Client(account_sid, auth_token)


# Abrir os 6 arquivos de excel
meta = 30000

lista_meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho']

for mes in lista_meses:
    print(mes)
    tabela_vendas = pd.read_excel(f'{mes}.xlsx') # lendo a tabela vendas
    print(tabela_vendas)

    if (tabela_vendas['Vendas'] > 30000).any(): # encontrando o valor com o any
        vendedor  = tabela_vendas.loc[tabela_vendas['Vendas'] > 30000, 'Vendedor'].values[0]
        vendas = tabela_vendas.loc[tabela_vendas['Vendas'] > 30000, 'Vendas'].values[0]
        print('Meta a ser alcançada: ', meta)

        print(f'No mês {mes} o vendedor(a) {vendedor} bateu a meta com  {vendas} mil em vendas')

        # enviando a mensagem para o número cadastrado
        message = client.messages.create(
            to="+5511957086049",
            from_="+16802244113",
            body=  f' BATEMOS A META 2022: \n\n  No mês {mes} o vendedor(a) {vendedor} bateu a meta com  {vendas} mil em vendas')

        print(message.sid)

print('Boas vendas')




