
import pyautogui
import time
import pandas as pd

# Para cada comando esperar 0.5 segundos, para não encavalar os comandos
pyautogui.PAUSE = 1

url = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
email = "moises@email.com"
senha = "12345678910"

# 1º Abrir sistema
# Abrindo navegador
pyautogui.press("win")

# Procurando o navegador
pyautogui.write("chrome")

# Abrindo o navegador
pyautogui.press("enter")

# Move o mouse para a barra de endereço
pyautogui.click(x=430, y=72)

# Informa o endereço do sistema (url)
pyautogui.write(url)

# Pressiona enter para entrar no sistema
pyautogui.press("enter")

# Espera um tempo até que a pagina seja carregada
time.sleep(5)

# 2º Logar no sistema
# Move o mouse até o campo de email
pyautogui.click(x=737, y=515)

# Informa o usuário
pyautogui.write(email)

# Muda para o campo de senha
pyautogui.press("tab")

# Informa a senha
pyautogui.write(senha)

# Muda para o botão de enviar
pyautogui.press("tab")

# Preciona enter para efetuar o login
pyautogui.press("enter")

# 3º Abrir a base de dados
tabela = pd.read_csv("produtos.csv")

# 4º Cadastrar um produto
# 5º Repetir o passo 4 até o termino dos produtos
# Clicar no campo codigo do produto
for linha in tabela.index:
    pyautogui.click(x=666, y=367)

    # Informar o codigo do produto
    codigo_produto = str(tabela.loc[linha, "codigo"])
    pyautogui.write(codigo_produto)

    # Ir para o próximo campo
    pyautogui.press("tab")

    # Informar a marca do produto
    marca = str(tabela.loc[linha, 'marca'])
    pyautogui.write(marca)

    # Ir para o proximo campos
    pyautogui.press("tab")

    # Informar o tipo
    tipo = str(tabela.loc[linha, 'tipo'])
    pyautogui.write(tipo)

    # Ir para o proximo campo
    pyautogui.press("tab")

    # Informar a categoria
    categoria = str(tabela.loc[linha, 'categoria'])
    pyautogui.write(categoria)

    # Ir para o proximo campo
    pyautogui.press("tab")

    # Informaro campo preço unitário
    preco_unitario = str(tabela.loc[linha, 'preco_unitario'])
    pyautogui.write(preco_unitario)

    # Ir para o proximo campo
    pyautogui.press("tab")

    # Informar o custo
    custo = str(tabela.loc[linha, 'custo'])
    pyautogui.write(custo)

    # Ir para o proximo campo
    pyautogui.press("tab")

    # Informar a Obs
    obs = str(tabela.loc[linha, 'obs'])
    if obs != "nan":
        pyautogui.write(obs)

    # Ir para o botão de incluir
    pyautogui.press("tab")

    # Precionar o botão para incluir
    pyautogui.press("enter")

    # Esperar um tempo para inclusão acontecer
    time.sleep(3)

    # Mover o curso par ao incio da tela
    pyautogui.scroll(5000)

