# Ordenando Palavras por Pontuação

# Você deve criar uma função que receba uma lista de palavras como parâmetro e retorne a lista ordenada em ordem decrescente com base em uma pontuação específica. A ordenação deve seguir as seguintes regras:

# Atribuição de Pontuação de Palavras: Cada letra do alfabeto é associada a um valor numérico sequencial, começando com A = 1, B = 2, C = 3 e assim por diante. Letras maiúsculas terão sua pontuação multiplicada por 2. Os acentos devem ser desconsiderados, e letras acentuadas ou especiais devem ser convertidas em suas formas não acentuadas (por exemplo, "é" é convertido para "e", "ç" é convertido para "c").

# Ordenação por Pontuação: As palavras na lista devem ser ordenadas com base na pontuação calculada no passo anterior. As palavras com a maior pontuação devem aparecer primeiro na lista, seguidas pelas palavras com pontuações menores.

# Desempate por Letra de Maior Valor: Se duas palavras tiverem a mesma pontuação, a que possuir a primeira letra com um valor numérico maior (de acordo com a atribuição de pontuação do alfabeto) deve aparecer primeiro na lista. Por exemplo, se as palavras "carro" e "casa" tiverem a mesma pontuação, "carro" deve aparecer antes de "casa" na lista.

import unicodedata
import re
import webbrowser
import os

def mata_acento(palavra):    
    palavra_sem_acênto = ''.join(c for c in unicodedata.normalize('NFD', palavra) if not unicodedata.combining(c))
    return palavra

def calcula_pontuacao(letra):
    alfabeto_lower = 'abcdefghijklmnopqrstuvwxyz'
    alfabeto_upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

    letra_sem_acentò = mata_acento(letra)

    if letra_sem_acentò in alfabeto_lower:
        ponto = alfabeto_lower.index(letra_sem_acentò) + 1
        return ponto
    
    if letra_sem_acentò in alfabeto_upper:
        ponto = alfabeto_upper.index(letra_sem_acentò) + 1
        return ponto * 2
    return 0 


def calcula_pontuacao_palavra(palavra):
    return sum(calcula_pontuacao(letra) for letra in palavra)

def ordena_tudo(palavra):
    pontuacao = calcula_pontuacao_palavra(palavra)
    primeira_letra = palavra[0]
    return (-pontuacao, -calcula_pontuacao(primeira_letra))

# tela
def app (url=None, url1=0):
    control = True

    while control:
        print("\n======================Desafio 01======================")
        print("= 1 -> Adicionar palavras e coisarada                =")
        print("= 2 -> Tocar 'Como tudo deve ser - Charlie Brown Jr  =")
        print("= 3 -> Sair                                          =")
        print("======================================================")


        opcao = int(input("Escolhe ai: "))

        if opcao == 1:

            entrada = input("Testa ai Vini: ")
            entrada = re.sub(r'[^a-zA-Z,]', '', entrada)

            palavras = entrada.split(',')

            palavra_ordenada = sorted(palavras, key=ordena_tudo)

            for palavra in palavra_ordenada: 

                pontuacao = calcula_pontuacao_palavra(palavra)
                letras = [f"{letra} - {calcula_pontuacao_palavra(letra)}" for letra in palavra]
                print(f"{palavra} - {pontuacao} [{', '.join(letras)}]")
        elif opcao == 2:
            url = "https://www.youtube.com/watch?v=k7pr4VTk5cQ"
            webbrowser.open(url)
            os.system('cls')

        elif opcao == 3:
            print("#ehusguri")
            control = False

os.system('cls')
app()