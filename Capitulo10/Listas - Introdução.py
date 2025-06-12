# -*- coding: utf-8 -*-
"""
Created on Fri Jun  6 07:22:44 2025

@author: Paulo
"""

# Listas são sequências de itens ou valores

valores = [10, 20, 30, 40]

frutas = ['abacaxi', 'morango', 'uva']

# Listas podem ter elementos de tipos diferentes
# Uma lista dentro de outra lista é uma lista aninhada

lista = ['spam', 2.55, 3, [10, 20]]

vazio = []

print(valores, frutas, vazio)

# Listas são mutáveis 
lista[0] = 'graviola'

# Percorrer elementos de uma lista

for i in frutas:
    print(i)
    
    
for i in frutas:
    print(f'Eu gosto de comer {i}.')
    
for numero in valores:
    print(numero * numero)
    
###### Métodos de lista

# Adicionar um elemento
frutas.append('sapoti')    
    
# Adicionar vários elementos
verduras = ['couve', 'repolho', 'nabo']

frutas.extend(verduras)

compras = frutas

# Ordenar
frutas.sort()

##### Mapeamento, filtragem e redução

# Somar todos os elementos de uma lista
def somar_tudo(lista):
    
    total = 0
    
    for elemento in lista:
        total = total + elemento
        
    return total

resultado = somar_tudo(valores)    
        
    
# Mapeamento em uma lista

def capitalizar(lista):
    
    nova_lista = []
    
    for elemento in lista:
        nova_lista.append(elemento.upper())
        
    return nova_lista    

dados = capitalizar(frutas)

# Função para filtrar elementos de uma lista

def manter_maiuscula(lista):
    
    nova_lista = []
    
    for elemento in lista:
        if elemento.isupper():
            nova_lista.append(elemento)
            
    return nova_lista        


verificar = manter_maiuscula(dados)



# Como excluir elementos?

# Excluindo pelo elemento
frutas.remove('nabo')

# Excluir por índice
del frutas[0]
