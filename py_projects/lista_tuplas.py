"""
listas em python
tipo list - mutavel
suporta varios valores de qualquer tipo
conhecimentos reutilizaveis - indices e fatiamento
metodos uteis :
   append, insert, pop, del, clear, extend, +
Create Read Update Delete
(CRUD)
"""
 
"""
    append - adiciona um item ao final da lista
    insert - adiciona um item no indice escolhido
    pop    - remove do final ou ultimo indice escolhido
    del    - apaga um indice
    clear  - limpa a lista
    extend - estende a lista
    +      - concatena listas

"""

lista = ['Maria', 'Helena', 'Luiz']
# i = 0

# lista.append('igor')

# for nome in lista:
#     print(i , nome)   
#     i+=1 


lista_enumerada = enumerate(lista)

for indice, nome in enumerate(lista):
    print('a')
    print(f'\t{nome}')