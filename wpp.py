from os import read
import pywhatkit as wpp
import datetime as dt
import pandas as pd

texto = input("Digite o nome do arquivo ")

df = pd.read_excel('test.xlsx', sheet_name=0)
contatos = df['Telefone'].tolist()

for contato in contatos:
    op = open(texto, encoding='utf8')
    current_time = dt.datetime.now()
    hour = current_time.hour
    min = current_time.minute+1
    wpp.sendwhatmsg(contato, op.read() , hour, min, 20, True, 15)