#Automação de tarefas em python utilizando a bilbioteca pyautogui

import pyautogui #biblioteca voltada para a automação de tarefas
import time #biblioteca do python
import pandas as pd
pyautogui.PAUSE = 0.5 #pausa de 0.5 segundos para cada comando do código INTEIRO
#time.sleep(3) #espera 3 segundos entre tarefas ESPECÍFICAS

#Comandos do pyautogui:
#pyautogui.press -> pressionar uma tecla
#pyautogui.click -> clicar
#pyautogui.write -> escrever
#pyautogui.hotkey -> atalho do teclado

#Passos
#Passo 1: abrir o sistema da empresa 
pyautogui.press("win")
pyautogui.write("firefox")
pyautogui.press("enter")
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")

#Passo 2: fazer o login
time.sleep(3)
pyautogui.click(x=651, y=465)
pyautogui.write("ilovecode@gmail.com")
pyautogui.press("tab")
pyautogui.write("password")
pyautogui.press("tab")
pyautogui.press("enter")

#Passo 3: importar a base de dados dos produtos
tabela = pd.read_csv("produtos.csv")

#Passo 4: cadastrar um produto
for linha in tabela.index: #index é linha e column coluna 
    pyautogui.click(x=630, y=321)

    #ecreve codigo
    #codigo = 
    pyautogui.write(str(tabela.loc[linha, "codigo"])) #tabela.loc é pra localizar algo na tabela
    pyautogui.press("tab")

    #ecreve marca
    pyautogui.write(str(tabela.loc[linha, "marca"]))
    pyautogui.press("tab")

    #ecreve tipo
    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press("tab")

    #ecreve categoria
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")

    #ecreve preco_unitario
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")

    #ecreve custo
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")

    #ecreve obs
    pyautogui.write(str(tabela.loc[linha, "codigo"]))
    pyautogui.press("tab")

#Passo 5: repitir o passo 4 até acabar os produtos