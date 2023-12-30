##############################  CODIGO GERADO PELO PROFESSOR  ##############################

# cpf = '74682489070'
# nove_digitos = cpf[:9]
# contador_regressivo_1 = 10

# resultado_digito_1 = 0
# for digito_1 in nove_digitos:
#     resultado_digito_1 += int(digito_1) * contador_regressivo_1
#     contador_regressivo_1 -= 1
# digito_1 = (resultado_digito_1 * 10) % 11
# digito_1 = digito_1 if digito_1 <= 9 else 0
# print(digito_1)
##############################^^CODIGO GERADO PELO PROFESSOR^^##############################

##############################\/\/CODIGO QUE EU FIZ\/\/##############################

# digitos = input('Digite os nove primeiros digitos do seu CPF: ')
# numeros_digitados = digitos

# contagem = 0
# multiplicador_regressivo = 10
# soma = []



# while contagem < 9:
#     formatacao = int(numeros_digitados[contagem]) 
#     multiplicar = formatacao * multiplicador_regressivo
#     soma.append(multiplicar)
#     contagem += 1
#     multiplicador_regressivo -= 1


# print(soma)

# soma_dos_numeros = 0

# for n in soma:
#     soma_dos_numeros += n

# print(soma_dos_numeros)

# multiplicar_10 = soma_dos_numeros * 10
# print(f'A multiplicação da soma é: {multiplicar_10}')
# resto_divisao = multiplicar_10 % 11
# print(f'O resto da divisão é : {resto_divisao}')

# if resto_divisao > 9:
#     primeiro_digito = 0
#     print(primeiro_digito)
# else:
#     primeiro_digito = resto_divisao
#     print(primeiro_digito)

# print(f'O primeiro digito do seu CPF é : {primeiro_digito}')
import re

digitos = input('digite seu CPF: ')

digitos = re.sub(
    r'[^0-9]',
    '',
    digitos
    )

print(digitos)
nove_digitos = digitos[:9]

soma = int()

contagem_regressiva = 10
valores = []
for digito in nove_digitos:
    multiplicar = int(digito) * contagem_regressiva
    contagem_regressiva -= 1
    valores.append(multiplicar)

for n in valores:
    soma += n

digito1 = (soma * 10) % 11

digito1 = digito1 if digito1 < 9 else 0
print(digito1)

#  segundo digito
dez_digitos = digitos[:10]

soma1 = int()

contagem_regressiva1 = 11
valores_dez_digitos = []
for digito in dez_digitos:
    multiplicar = int(digito) * contagem_regressiva1
    contagem_regressiva1 -= 1
    valores_dez_digitos.append(multiplicar)

for n in valores_dez_digitos:
    soma1 += n

digito2 = (soma1 * 10) % 11

digito2 = digito2 if digito2 < 9 else 0

print(digito2)