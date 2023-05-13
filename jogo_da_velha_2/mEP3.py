######################################################
# Programção I / Programação Funcional (2023/1)
# miniEP3 - Jogo da Velha
# Nome: Thierry martins ribeiro
# Matrícula: 2022201402
######################################################

######################################################
# LEMBRE-SE:
# - Não é permitido usar estruturas de repetição,
#   variáveis globais, funções impuras e operações
#   que não sejam do Paradigma Funcional.
# - Você não pode usar variáveis globais;
# - Não use funções recursivas (não há necessidade);
# - Você deve seguir o código base disponibilizado,
#   não sendo permitido a alteração do nome e/ou
#   lista de parâmetros das funções dadas;
# - Caso precise, você *PODE* criar outras funções;
# - Não é permitido a utilização de lista, tuplas
#   ou qualquer outro tipo estruturado para
#   “facilitar” a manipulação dos dados. Você deve
#   sempre trabalhar com as 9 variáveis que
#   representam as posições no tabuleiro;
#
# Dica: Leia o docstring de cada função para saber o
#       que cada uma deve fazer e retornar.
######################################################


def imprimeTabuleiro(p1, p2, p3, p4, p5, p6, p7, p8, p9):
    """
    Recebe os valores das nove posições do tabuleiro e imprime o tabuleiro
    """

    print(f" {p7} | {p8} | {p9} ")
    print(f"---+---+---")
    print(f" {p4} | {p5} | {p6} ")
    print(f"---+---+---")
    print(f" {p1} | {p2} | {p3} ")


def entradaValida(p1, p2, p3, p4, p5, p6, p7, p8, p9):
    """
    Recebe os valores das nove posições do tabuleiro e
    verifica se os valores são válidos, ou seja, retorna True
    se cada variável possui " " ou "x" ou "o" e False, caso contrário.
    """
    # Complete o código da função

    if p1 != " " and p1 != "x" and p1 != "o":
        return False
    elif p2 != " " and p2 != "x" and p2 != "o":
        return False
    elif p3 != " " and p3 != "x" and p3 != "o":
        return False
    elif p4 != " " and p4 != "x" and p4 != "o":
        return False
    elif p5 != " " and p5 != "x" and p5 != "o":
        return False
    elif p6 != " " and p6 != "x" and p6 != "o":
        return False
    elif p7 != " " and p7 != "x" and p7 != "o":
        return False
    elif p8 != " " and p8 != "x" and p8 != "o":
        return False
    elif p9 != " " and p9 != "x" and p9 != "o":
        return False
    return True


def jogadaValida(p1, p2, p3, p4, p5, p6, p7, p8, p9):
    """
    Recebe os valores das nove posições do tabuleiro e
    verifica se os valores formam uma jogada válida.
    Retorna True se a jogada for válida e False, caso contrário
    """
    # Complete o código da função

    x = 0
    o = 0

    if p1 == "x":
        x += 1
    elif p1 == "o":
        o += 1
    if p2 == "x":
        x += 1
    elif p2 == "o":
        o += 1
    if p3 == "x":
        x += 1
    elif p3 == "o":
        o += 1
    if p4 == "x":
        x += 1
    elif p4 == "o":
        o += 1
    if p5 == "x":
        x += 1
    elif p5 == "o":
        o += 1
    if p6 == "x":
        x += 1
    elif p6 == "o":
        o += 1
    if p7 == "x":
        x += 1
    elif p7 == "o":
        o += 1
    if p8 == "x":
        x += 1
    elif p8 == "o":
        o += 1
    if p9 == "x":
        x += 1
    elif p9 == "o":
        o += 1
    diferenca = abs(x - o)
    if diferenca > 1:
        return False
    return True


def verificaJogada(p1, p2, p3, p4, p5, p6, p7, p8, p9):
    """
    Recebe os valores das nove posições do tabuleiro e
    imprime se um jogador ("x" ou "o") venceu a jogada.
    """
    # Complete o código da função

    venceu = False
    jogador_vencedor = " "

    if p1 == p2 == p3 and p1 != " ":
        venceu = True
        jogador_vencedor = p1
    elif p4 == p5 == p6 and p4 != " ":
        venceu = True
        jogador_vencedor = p4
    elif p7 == p8 == p9 and p7 != " ":
        venceu = True
        jogador_vencedor = p7
    elif p1 == p4 == p7 and p1 != " ":
        venceu = True
        jogador_vencedor = p1
    elif p2 == p5 == p8 and p2 != " ":
        venceu = True
        jogador_vencedor = p2
    elif p3 == p6 == p9 and p3 != " ":
        venceu = True
        jogador_vencedor = p3
    elif p1 == p5 == p9 and p1 != " ":
        venceu = True
        jogador_vencedor = p1
    elif p3 == p5 == p7 and p3 != " ":
        venceu = True
        jogador_vencedor = p3

    if venceu == True:
        print(f"O jogador '{jogador_vencedor}' venceu!")
    else:
        if (
            p1 == " "
            or p2 == " "
            or p3 == " "
            or p4 == " "
            or p5 == " "
            or p6 == " "
            or p7 == " "
            or p8 == " "
            or p9 == " "
        ):
            print("O jogo nao terminou!")
        else:
            print("Empate!")


######################################################
## NÃO ALTERE A FUNÇÃO 'main'                       ##
######################################################
def main():
    t1 = input()
    t2 = input()
    t3 = input()
    t4 = input()
    t5 = input()
    t6 = input()
    t7 = input()
    t8 = input()
    t9 = input()
    imprimeTabuleiro(t1, t2, t3, t4, t5, t6, t7, t8, t9)
    if entradaValida(t1, t2, t3, t4, t5, t6, t7, t8, t9) == False:
        print("Entrada invalida!")
    elif jogadaValida(t1, t2, t3, t4, t5, t6, t7, t8, t9) == False:
        print("Jogada invalida!")
    else:
        verificaJogada(t1, t2, t3, t4, t5, t6, t7, t8, t9)


main()
