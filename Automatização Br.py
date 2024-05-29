import pyautogui
import time
import webbrowser
import os


# Aqui acessamos o site
url = 'https://credenciados.grupobrmed.com.br/'
webbrowser.open(url)
pyautogui.PAUSE = 2
pyautogui.hotkey('alt', 'space', 'x')


# Fazer login no sistema 
time.sleep(3)
pyautogui.click(x=952, y=343)
pyautogui.write('****')

pyautogui.click(x=943, y=412)
pyautogui.write('****')

pyautogui.click(x=929, y=483)

time.sleep(3)

pyautogui.click(x=1624, y=250)

#Aqui acessaremos relatorios de agendamentos
time.sleep(1)
pyautogui.click(x=735, y=924)

#Aqui acessaremos a aba solicitados
time.sleep(1)
pyautogui.click(x=779, y=527)

#Aqui acessaremos agendados para:
pyautogui.click(x=779, y=574)

#Aqui acessaremos a primeira data
time.sleep(1)

pyautogui.click(x=912, y=583)
pyautogui.press('ENTER')

#Aqui acessaremos a segunda data
time.sleep(1)
pyautogui.click(x=913, y=640)
pyautogui.press('ENTER')

#Aqui fazemos o donwload do arquivo
time.sleep(1)
pyautogui.click(x=599, y=748)


# Caminho para o arquivo que você deseja abrir
time.sleep(7)
caminho_arquivo = ('C:\\Users*********') 

# Verifique se o arquivo existe antes de tentar abrir
os.path.isfile(caminho_arquivo)
os.system(f"start {caminho_arquivo}")  # Abre o arquivo com o programa padrão associado

# Selecionamos "sim" para abrir o arquivo
time.sleep(8)
pyautogui.click(x=872, y=584)

# Selecionamos habilitar edição
time.sleep(5)
pyautogui.click(x=1483, y=115)

# Abrir o arquivo
time.sleep(3)
pyautogui.click(x=43, y=79)

# Salvar Como
time.sleep(3)
pyautogui.click(x=94, y=482)

# Campo selecionar o Doc.
time.sleep(3)
pyautogui.click(x=773, y=220)

# Extensão do doc.
time.sleep(3)
pyautogui.click(x=951, y=246)

# Salvar
time.sleep(3)
pyautogui.click(x=1573, y=215)

# Automatização finalizada
print ("Automatização finalizada com sucesso")