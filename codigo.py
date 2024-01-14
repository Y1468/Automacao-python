#Passo a passp dp proeto

#Passo1:Entra no sistema da inpresa
#https://dlp.hashtagtreinamentos.com/python/intencivao/login

#Passo2:Fazê o login
#passo3:importa a base de dados
#Passo4:cadastra um produlto
#Passo5:Repetir ate acabar a base de dados

#pip install pyautogui
#pip install pandas numpy openpyxl
import pyautogui
import time

#clicar->pyautogui.click
#escrever->pyauyogui.write
#apertar uma tecla->pyautogui.press
#atalho->pyautogui.hotkey
#Rolar pagina->pyautogui.scroll

#.index->Linhas
#.columns->Colunas

pyautogui.PAUSE=2
#Aperta tecla do windows

pyautogui.press("win")
#Escrever
pyautogui.write("edge")
#Apertar enter
pyautogui.press("enter")

link="https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(link)
pyautogui.press("enter")

#Pausar 5 segundos
time.sleep(5)

#Fazer login
pyautogui.click(x=477, y=353)

pyautogui.write("ivan@gmail.com")
pyautogui.press("tab")
pyautogui.write("1234")
pyautogui.click(x=696, y=519)
time.sleep(3)

#importando base de dados
import pandas

tabela=pandas.read_csv("produtos.csv")
print(tabela)


for linha in tabela.index:

    pyautogui.click(x=397, y=239)

    #Cadastrando produlto
    codigo=tabela.loc[linha,"codigo"]
    pyautogui.write(codigo)
    pyautogui.press('tab')

    pyautogui.write(tabela.loc[linha,"marca"])
    pyautogui.press("tab")

    pyautogui.write(tabela.loc[linha,"tipo"])
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha,"categoria"]))
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha,"preco_unitario"]))
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha,"custo"]))
    pyautogui.press("tab")

    obs=tabela.loc[linha,"obs"]
    #Verifica se o obs ta vazio
    if not pandas.isna(obs):
        pyautogui.write(obs)
    pyautogui.press("tab")

    #Emviar o produlto
    pyautogui.press("enter")
    #Rolando a pagina

    pyautogui.scroll(5000)




