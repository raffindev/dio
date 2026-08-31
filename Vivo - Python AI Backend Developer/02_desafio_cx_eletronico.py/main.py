from cx_eletronico import iniciar_caixa, menu_caixa_eletronico
from contas import menu_conta_corrente

diretorio = "Vivo - Python AI Backend Developer/02_desafio_cx_eletronico.py/dados"

usuario, lista_usuarios, lista_contas = iniciar_caixa(diretorio)

conta_corrente = menu_conta_corrente(usuario, lista_contas)

menu_caixa_eletronico(conta_corrente, lista_contas, diretorio)