# DICAS SOBRE PYTHON:
# FUNÇÃO input(): Ela recebe como parâmetro uma String que será visível ao usuário, 
# onde geralmente informa que tipo de informação ele está esperando receber;
# FUNÇÃO print(): Ela é a responsável por imprimir os dados e informar os valores no terminal;
# MÉTODO ord(): Retorna o valor  ASCII de cada letra ou símbolo do teclado;
letra = input()

import string

alfabeto = string.ascii_uppercase
alfabeto_lista = list(alfabeto)

print(alfabeto_lista.index(letra)+1)
# TODO: De acordo com a entrada, imprima a posição dessa letra no Alfabeto;