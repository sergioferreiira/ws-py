################### CALCULADORA COM WHILE ###########################

while True:
    # atalhos
    num1 = numero_1 = int(input('Digite o primeiro numero: '))
    num2 = numero_2 = int(input('Digite o primeiro numero: '))

    # operadores
    somar = False
    subtrair = False
    dividir = False
    multiplicar = False

    print('Que tipo de conta voce gostaria de realizar hoje?')
    print('Nossa calculadora opera com somar, subtrair, dividir e multiplicar')
    print('Digite que tipo de conta deseja fazer')
    print('Caso queira sair da calculadora basta digitar: sair')

    # entrada de dados
    tipo_conta = str(input('somar, subtrair, dividir e multiplicar: ').lower())

    # verifica se e alguma conta
    if tipo_conta != somar or subtrair or dividir or multiplicar:
        print('#####################################################################################')
        print('Digite o tipo de conta que deseja realizar ou escreva "sair" para encerrar o progama ')
        print('#####################################################################################')
        continue

    # verificação de conta
    if tipo_conta == 'somar':
        somar = True
    elif tipo_conta == 'subtrair':
        subtrair = True
    elif tipo_conta == 'dividir':
        dividir = True
    elif tipo_conta == 'multiplicar':
        multiplicar = True
    
    # conta e entrada de dados
    if somar == True:
        num1
        num2
    
        continue
    if subtrair == True:
        num1
        num2
        print (numero_1 - numero_2)
        continue
    if dividir == True:
        num1
        num2
        print (numero_1 / numero_2)
        continue
    if multiplicar == True:
        num1
        num2
        print (numero_1 * numero_2) 
        continue
    
    if tipo_conta == 'sair':
        break