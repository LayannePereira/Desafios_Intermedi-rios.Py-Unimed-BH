# DICAS SOBRE PYTHON:
# FUNÇÃO input(): Ela recebe como parâmetro uma String que será visível ao usuário, 
# onde geralmente informa que tipo de informação ele está esperando receber;
# FUNÇÃO print(): Ela é a responsável por imprimir os dados e informar os valores no terminal;
# MÉTODO split(): permite dividir o conteúdo da variável de acordo com as condições especificadas 
# em cada parâmetro da função ou com os valores predefinidos por padrão;

# Abaixo segue um exemplo de código que você pode ou não utilizar
salario = int(input())

if (0 <= salario <= 600):
    percentual = 17
    reajuste = salario * (percentual / 100)
    salario += reajuste
elif (600.01 <= salario <= 900):
    percentual = 13
    reajuste = salario * (percentual / 100)
    salario += reajuste
elif (900.01 <= salario <= 1500):
    percentual = 12
    reajuste = salario * (percentual / 100)
    salario += reajuste
elif (1500.01 <= salario <= 2000):
    percentual = 10
    reajuste = salario * (percentual / 100)
    salario += reajuste
else:
    percentual = 5
    reajuste = salario * (percentual / 100)
    salario += reajuste

print(f'Novo salario: {salario:.2f}\nReajuste ganho: {reajuste:.2f}\nEm percentual: {percentual} %')


# TODO:  Calcule o salário do funcionário e print o novo salário, bem como o valor de reajuste ganho e o índice reajustado (em porcentagem)