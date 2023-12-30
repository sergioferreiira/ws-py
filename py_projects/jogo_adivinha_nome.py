# palavra_secreta = 'sergio'
# palavra_formatada = ''
# tentativas = 5


# while tentativas != 0:

#     letra_digitada = input('Digite uma letra e vamos verificar se ela está na palavra secreta: ').lower()

#     # confirmando se e um caracter

#     if letra_digitada == letra_digitada[:1]:

#         # verificando indice da palavra secreta

#         for letra in palavra_secreta:

#             if letra_digitada == letra:  
#                 palavra_formatada += letra
#                 nova_palavra = palavra_formatada
#                 print(f'Você acertou uma das letras da palavra secreta elá é : {nova_palavra}')

#             else:
#                 print('*')
#         tentativas -= 1
#         print(f'Voce ainda possui {tentativas} tentativas')
#         if tentativas == 1:
#             resposta_final = str(input('Você está na sua ultima tentativa, escreva a palavra secreta: '))
#             if resposta_final == palavra_secreta:
#                 print('parabens você acertou a palavra secreta')
#             else:
#                 print('você errou a palavra secreta')

#     else:
#         print('digite apenas um caracter')

import os      
import time
import random
            
palavras_secretas = {'ana', 'abacate', 'telhado', 'dinheiro'}

palavra_secreta = random.choice(list(palavras_secretas))
nova_palavra = ''

i = 0



while True:


    entrada_de_dado = str(input('digite uma letra e descubra o nome: '))

    if entrada_de_dado in palavra_secreta:
        nova_palavra += entrada_de_dado


    palavra_formada = ''
    for letra_secreta in palavra_secreta:

        if letra_secreta in nova_palavra:
            palavra_formada += letra_secreta

        else:
            palavra_formada += '*'

        i += 1

    print(palavra_formada)
    if palavra_formada == palavra_secreta:
        print('parabens voce ganhou')
        palavra_secreta = random.choice(list(palavras_secretas))
        nova_palavra = ''
        i = 0
        palavra_formada = ''
        time.sleep(3)
        os.system('cls')


            

    
    



