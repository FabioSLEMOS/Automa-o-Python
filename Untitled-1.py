import webbrowser
import pyautogui
import time 

pyautogui.PAUSE = 1

# Passo 1 - Acessar o sistema da empresa.
url = 'https://pages.hashtagtreinamentos.com/aula1-intensivao-sistema'

# Abre o URL no navegador padrão do sistema.
webbrowser.open(url)
pyautogui.press('ENTER')
time.sleep(2)

# Passo 2: Fazer o login no sistema.

pyautogui.doubleClick(x=567, y=342)
pyautogui.write('Fsantos@')

pyautogui.doubleClick(x=700,y=450)
pyautogui.write('1998')

pyautogui.doubleClick(x=670, y=509)
time.sleep(5)

# Passo 3: Baixar a base de dados.'

pyautogui.click(x=1171, y=417)

time.sleep(10)
pyautogui.click(x=987, y=828)
time.sleep(5)

# Passo 4: Calcular os indicadores.
import pandas

#Impotar a base de dados.
tabela = pandas.read_csv('C:\\Users\Carla\\Downloads\\Compras.csv', sep=';')
print(tabela)

# Total gasto - Somar a coluna valor final.
total_gasto = tabela['ValorFinal'].sum() 

# Quantidade - Somar a coluna Quantidade.
Quantidade = tabela['Quantidade'].sum()


#Preco Médio - Total gasto / Valor final.
preco_medio = total_gasto/ Quantidade

print(total_gasto)
print(Quantidade)
print(preco_medio)

# Passo 5: Enviar o e-mail para a diretoria.
import pyperclip

# Entrar no meu e-mai.
url = 'https://mail.google.com/mail/u/0/#inbox'

# Abre o URL no navegador padrão do sistema.
webbrowser.open(url)
pyautogui.press('ENTER')

time.sleep(7)

# Clicar em escrever.
pyautogui.click(x=20, y=180)
time.sleep(8)

pyautogui.write('fabio.lemos.6697@gmail.com')
pyautogui.press('TAB') # Seleciona o e-mail.

pyautogui.press('TAB') # Passar para o campo do assunto.
pyautogui.write('Relatório de Compras')

pyautogui.press('TAB') # Passar para o campo do e-mail.

texto = f'''Boa tarde, Prezados!
Segue em anexo o relatório diário.

Total Gasto = R${total_gasto:,.2f}
Quantidade de {Quantidade:,.1f}
Preço Médio = R${preco_medio:,.2f}

Ao dispor para dúvidas e esclarecimentos.

Atenciosamente,
Fabio Santos
Tel: 9 9026-5205'''

pyperclip.copy(texto)
pyautogui.hotkey('ctrl', 'v')

# Anexar o arquivo baixado. 
time.sleep(5)
pyautogui.click(x=783, y=893)

time.sleep(8)
pyautogui.doubleClick(x=213, y=184)

# Enviar.
pyautogui.hotkey('ctrl', 'enter')


#print(pyautogui.position())



# pyautogui.click - Clicar com o mouse 
# pyautogui.hotkey("ctrl", "t")
# pyautogui.write()

# pyautogui.write - Escrever um texto
# pyautogui.press - Apertar uma unica tecla 
# pyautogui.hotkey- Apertar uma combinacao de teclas