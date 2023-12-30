frase = ' sergio ferreira da silveira filho '

i = 0 
palavra_mais_apareceu = ''
qnt_mais_apareceu = 0


while i < len(frase):
    letra = frase[i]
    contador_letra = frase.count(letra)

    if letra == ' ':
        i += 1
        continue
    
    if qnt_mais_apareceu < contador_letra:
        qnt_mais_apareceu = contador_letra
        palavra_mais_apareceu = letra

    i += 1
print(palavra_mais_apareceu , qnt_mais_apareceu)
   
