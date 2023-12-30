
import os



lista_de_compras = []


while True:

    print('Selecione uma opção')
    opcao = input('[i]nserir [a]pagar [l]istar: ')
    
    if opcao == 'i':
        inserir_novo_item = input('digite o nome do item: ')
        lista_de_compras.append(inserir_novo_item)
    
    if opcao == 'a':
        numero_item = input('Digite o numero do item que deseja apagar: ')

        try:
            indice = int(numero_item)
            del lista_de_compras[indice]

        except ValueError :
            print('não e possivel apagar esse indice')
        except IndexError :
            print('não e possivel apagar esse indice')
        except Exception :
            print('Erro desconhecido')

    if opcao == 'l':
        os.system('cls')
        if len(lista_de_compras) == 0:
            print('nada a listar')
            continue
        for item , nome in enumerate(lista_de_compras):
            print(item , nome)
    

        

