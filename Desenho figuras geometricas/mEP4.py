######################################################
# Programção I / Programação Funcional (2023/1)
# miniEP4 - Desenhando objetos geométricos simples
# Nome: Thierry Martins Ribeiro
# Matrícula: 2022020402
######################################################

######################################################
# LEMBRE-SE:
# - Não é permitido usar estruturas de repetição,
#   variáveis globais, funções impuras e operações
#   que não sejam do Paradigma Funcional.
# - Caso precise, você PODE criar outras funções;
#
# Dica: Leia o docstring de cada função para saber o
#       que cada uma deve fazer e retornar.
######################################################


def r(largura, altura, simbolo, linha_atual=1):
    if largura <= 0 or altura <= 0:
        print("Medida invalida.")
        return
    if largura <= 0 or altura <= 0 or linha_atual > altura:
        return
    if linha_atual == 1 or linha_atual == altura:
        print(simbolo * largura)
    else:
        print(simbolo + (" " * (largura - 2)) + simbolo)
    return r(largura, altura, simbolo, linha_atual + 1)


def p(largura, altura, simbolo, linha_atual=1):
    if largura <= 0 or altura <= 0:
        print("Medida invalida.")
        return
    if largura <= 0 or altura <= 0 or linha_atual > altura:
        return
    if linha_atual == 1:
        print(simbolo * largura)
    elif linha_atual == altura:
        print(" " * (linha_atual - 1) + (simbolo * largura))
    else:
        print(" " * (linha_atual - 1) + simbolo + (" " * (largura - 2)) + simbolo)
    return p(largura, altura, simbolo, linha_atual + 1)


def te(altura, simbolo, linha_atual=1):
    if altura <= 0:
        print("Medida invalida.")
        return
    if altura <= 0 or linha_atual > altura:
        return
    if linha_atual == 1:
        print(" " * (altura - linha_atual) + (simbolo))
    elif linha_atual == altura:
        print(simbolo * (linha_atual * 2 - 1))
    else:
        print(
            " " * (altura - linha_atual)
            + simbolo
            + " " * (linha_atual * 2 - 3)
            + simbolo
        )
    return te(altura, simbolo, linha_atual + 1)


def tre(altura, simbolo, linha_atual=1):
    if altura <= 0:
        print("Medida invalida.")
        return
    if altura <= 0 or linha_atual > altura:
        return
    if linha_atual == altura or linha_atual == 1:
        print(simbolo * linha_atual)
    else:
        print(simbolo + (" " * (linha_atual - 2)) + simbolo)
    return tre(altura, simbolo, linha_atual + 1)


def trd(altura, simbolo, linha_atual=1):
    if altura <= 0:
        print("Medida invalida.")
        return
    if altura <= 0 or linha_atual > altura:
        return
    if linha_atual == altura or linha_atual == 1:
        print((" " * (altura - linha_atual)) + (simbolo * linha_atual))
    else:
        print(
            (" " * (altura - linha_atual))
            + simbolo
            + (" " * (linha_atual - 2))
            + simbolo
        )
    return trd(altura, simbolo, linha_atual + 1)


def main():
    # Faça a leitura dos dados na função 'main' e, a partir dela, chame a
    # função para fazer o desenho de acordo com a entrada.
    # Use a 'main' também para imprimir se o objeto ou a médida é inválido
    figura = input()
    if figura == "R" or figura == "P":
        largura = int(input())
    altura = int(input())
    simbolo = input()

    if figura == "R":
        r(largura, altura, simbolo)
    elif figura == "P":
        p(largura, altura, simbolo)
    elif figura == "TE":
        te(altura, simbolo)
    elif figura == "TRE":
        tre(altura, simbolo)
    elif figura == "TRD":
        trd(altura, simbolo)
    else:
        print("Objeto invalido.")


main()
