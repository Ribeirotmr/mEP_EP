######################################################
# Programação Funcional / Programção I (2022/2)
# E{l[2]} - Jogo da Velha
# Nome: Thierry Martins Ribeiro
# Matrícula: 2022201402
######################################################

import random
from os import system, name


def getMatricula():
    """
    Retorna a matricula do aluno como string
    """
    return "2022201402"


def getNome():
    """
    Retorna o nome completo do aluno
    """
    return "Thierry Martins Ribeiro"


def jogo(l, vez, jogador, computador):
    limpaTela()
    imprimeTabuleiro(l)
    if jogadorVencedor(l) == "Empate":
        print("O jogo empatou ")
    elif jogadorVencedor(l) == computador:
        print(f"Você perdeu")
    elif jogadorVencedor(l) == jogador:
        print(f"Você ganhou")
    else:
        if vez == jogador:
            l[escolhaOcupacao(l[:])] = jogador
            return jogo(l, computador, jogador, computador)
        else:
            input("Vez do computador aperte para continuar: ")
            l[jogadaComputador(l[:], computador)] = computador
            return jogo(l, jogador, jogador, computador)


def limpaTela():
    if name == 'nt':
        system('cls')
    else:
        system('clear')


def imprimeTabuleiro(l):
    """
    Recebe os valores das nove posições do tabuleiro e imprime o tabuleiro
    """
    # Complete o código da função
    print(f" {l[7]} | {l[8]} | {l[9]} ")
    print("---+---+---")
    print(f" {l[4]} | {l[5]} | {l[6]} ")
    print("---+---+---")
    print(f" {l[1]} | {l[2]} | {l[3]} ")


def escolhaXO():
    escolha = input("Escolha O ou X? ")
    if escolha != "X" and escolha != "O" and escolha != "x" and escolha != "o":
        print("Jogada invalida")
        return escolhaXO()
    if escolha == "x" or escolha == "X":
        return "X"
    if escolha == "o" or escolha == "O":
        return "O"


def escolhaNumero():
    jogada = int(input("Escolha de 1 a 9? "))
    if jogada < 1 and jogada > 9:
        print("Jogada invalida")
        return escolhaNumero()
    return jogada


def escolhaOcupacao(l):
    jogada = escolhaNumero()
    if l[jogada] == " ":
        return jogada
    print("Posição ocupada[!]")
    return escolhaOcupacao(l[:])


def jogadorVencedor(l):
    venceu = 0
    if l[1] == "X" and l[2] == "X" and l[3] == "X":
        venceu = "X"
    elif l[1] == "O" and l[2] == "O" and l[3] == "O":
        venceu = "O"
    elif l[4] == "X" and l[5] == "X" and l[6] == "X":
        venceu = "X"
    elif l[4] == "O" and l[5] == "O" and l[6] == "O":
        venceu = "O"
    elif l[7] == "X" and l[8] == "X" and l[9] == "X":
        venceu = "X"
    elif l[7] == "O" and l[8] == "O" and l[9] == "O":
        venceu = "O"
    elif l[1] == "X" and l[4] == "X" and l[7] == "X":
        venceu = "X"
    elif l[1] == "O" and l[4] == "O" and l[7] == "O":
        venceu = "O"
    elif l[2] == "X" and l[5] == "X" and l[8] == "X":
        venceu = "X"
    elif l[2] == "O" and l[5] == "O" and l[8] == "O":
        venceu = "O"
    elif l[3] == "X" and l[6] == "X" and l[9] == "X":
        venceu = "X"
    elif l[3] == "O" and l[6] == "O" and l[9] == "O":
        venceu = "O"
    elif l[1] == "X" and l[5] == "X" and l[9] == "X":
        venceu = "X"
    elif l[1] == "O" and l[5] == "O" and l[9] == "O":
        venceu = "O"
    elif l[3] == "X" and l[5] == "X" and l[7] == "X":
        venceu = "X"
    elif l[3] == "O" and l[5] == "O" and l[7] == "O":
        venceu = "O"
    if venceu != "X" and venceu != "O":
        if l[1] == " " or l[2] == " " or l[3] == " " or l[4] == " " or l[5] == " " or l[6] == " " or l[7] == " " or {l[8]} == " " or l[9] == " ":
            return None
        else:
            return "Empate"
    else:
        return venceu


def jogadaComputador(tabuleiro, simboloComputador):
    """
    Recebe o tabuleiro e o simbolo (X ou O) do computador e determina onde o computador deve jogar
    O tabuleiro pode estar vazio (caso o computador seja o primeiro a jogar) ou com algumas posições preenchidas, 
    sendo a posição 0 do tabuleiro descartada.

    Parâmetros:
    tabuleiro: lista de tamanho 10 representando o tabuleiro
    simboloComputador: letra do computador 

    Retorno:
    Posição (entre 1 e 9) da jogada do computador

    Estratégia: 
    DIGITE AQUI A ESTRATÉGIA USADA PELO COMPUTADOR PARA TENTAR VENCER O JOGADOR
    """

    if simboloComputador == "X":
        simboloJogador = "O"
    if simboloComputador == "O":
        simboloJogador = "X"
    if simboloComputador not in tabuleiro and simboloJogador in tabuleiro:
        if simboloJogador == tabuleiro[5]:
            return random.choice([1, 2, 3, 4, 6, 7, 8, 9])
        return 5

    # se o jogador jogar na posição 1 e 4, o computador tem que jogar na posição 7
    if tabuleiro[1] == simboloJogador and tabuleiro[4] == simboloJogador:
        if tabuleiro[7] == " ":
            return 7
    # se o jogador jogar no 1 e 8, o computador tem que jogar na posição 4,5,6,7,9,6
    if tabuleiro[1] == simboloJogador and tabuleiro[8] == simboloJogador:
        if tabuleiro[4] == " ":
            return 4
        if tabuleiro[5] == " ":
            return 5
        if tabuleiro[6] == " ":
            return 6
        if tabuleiro[7] == " ":
            return 7
        if tabuleiro[9] == " ":
            return 9
        # se o jogador jogar na posição 1 e 9, o computador tem que jogar na posição 4,6
    if tabuleiro[1] == simboloJogador and tabuleiro[9] == simboloJogador:
        if tabuleiro[4] == " ":
            return 4
        if tabuleiro[6] == " ":
            return 6
        # se o jogador jogar na posição 1 e 6, o computador tem que jogar na posição 8,9,3,2
    if tabuleiro[1] == simboloJogador and tabuleiro[6] == simboloJogador:
        if tabuleiro[8] == " ":
            return 8
        if tabuleiro[9] == " ":
            return 9
        if tabuleiro[3] == " ":
            return 3
        if tabuleiro[2] == " ":
            return 2
    # se o jogador jogar na posição 1 e 3, o computador tem que jogar na posição 4 ou 6
    if tabuleiro[1] == simboloJogador and tabuleiro[3] == simboloJogador:
        if tabuleiro[4] == " ":
            return 4
        if tabuleiro[6] == " ":
            return 6
    # se o jogador jogar na posição 1 e 2, o computador tem que jogar na posição 3
    if tabuleiro[1] == simboloJogador and tabuleiro[2] == simboloJogador:
        if tabuleiro[3] == " ":
            return 3

    # se o jogador jogar na posição 4 e 1, o computador tem que jogar na poição 7
    if tabuleiro[4] == simboloJogador and tabuleiro[1] == simboloJogador:
        if tabuleiro[7] == " ":
            return 7
    # se o jogador jogar na posição 4 e 2, o computador tem que jogar na posição 1
    if tabuleiro[4] == simboloJogador and tabuleiro[2] == simboloJogador:
        if tabuleiro[1] == " ":
            return 1
    # se o jogador jogar na posição 4 e 3, o computador tem que jogar na posição 1, 7 , 8
    if tabuleiro[4] == simboloJogador and tabuleiro[3] == simboloJogador:
        if tabuleiro[1] == " ":
            return 1
        if tabuleiro[7] == " ":
            return 7
        if tabuleiro[8] == " ":
            return 8
    # se o jogador jogar na posição 4 e 6, o computador tem que jogar na posição 7,9,3,1
    if tabuleiro[4] == simboloJogador and tabuleiro[6] == simboloJogador:
        if tabuleiro[7] == " ":
            return 7
        if tabuleiro[9] == " ":
            return 9
        if tabuleiro[3] == " ":
            return 3
        if tabuleiro[1] == " ":
            return 1
    # se o jogador jogar na posição 4 e 9, o computador tem que o jogar na posição 2,7
    if tabuleiro[4] == simboloJogador and tabuleiro[9] == simboloJogador:
        if tabuleiro[2] == " ":
            return 2
        if tabuleiro[7] == " ":
            return 7
    # se o jogador jogar na posição 4 e 8, o computador tem que jogar na posição 7
    if tabuleiro[4] == simboloJogador and tabuleiro[8] == simboloJogador:
        if tabuleiro[7] == " ":
            return 7
    # se o jogador jogar na posição 4 e 7, o computador tem que jogar na posição 1
    if tabuleiro[4] == simboloJogador and tabuleiro[7] == simboloJogador:
        if tabuleiro[1] == " ":
            return 1
    # se o jogador jogar na posição 7 e 1, o computador tem que jogar na posição 4
    if tabuleiro[7] == simboloJogador and tabuleiro[1] == simboloJogador:
        if tabuleiro[4] == " ":
            return 4
    # se o jogador jogar na posição 7 e 2, o computador tem que jogar na posição 1,3,4,6
    if tabuleiro[7] == simboloJogador and tabuleiro[2] == simboloJogador:
        if tabuleiro[1] == " ":
            return 1
        if tabuleiro[3] == " ":
            return 3
        if tabuleiro[4] == " ":
            return 4
        if tabuleiro[6] == " ":
            return 6
    # se o jogador jogar na posição 7 e 3, o computador deve jogar na posição 4, 6
    if tabuleiro[7] == simboloJogador and tabuleiro[3] == simboloJogador:
        if tabuleiro[4] == " ":
            return 4
        if tabuleiro[6] == " ":
            return 6
    # se o jogador jogar na posição 7 e 6, o computador deve jogar na posição 2,3,8,9
    if tabuleiro[7] == simboloJogador and tabuleiro[4] == simboloJogador:
        if tabuleiro[2] == " ":
            return 2
        if tabuleiro[3] == " ":
            return 3
        if tabuleiro[8] == " ":
            return 8
        if tabuleiro[9] == " ":
            return 9
    # se o jogador jogar na posição 7 e 4, o computador deve jogar na posição 1
    if tabuleiro[7] == simboloJogador and tabuleiro[4] == simboloJogador:
        if tabuleiro[1] == " ":
            return 1
    # se o jogador jogar na posição 7 e 8, o computador deve jogar na posição 9
    if tabuleiro[7] == simboloJogador and tabuleiro[8] == simboloJogador:
        if tabuleiro[9] == " ":
            return 9
    # se o jogador jogar na posição 7 e 9, o computador deve jogar na posição 8
    if tabuleiro[7] == simboloJogador and tabuleiro[9] == simboloJogador:
        if tabuleiro[8] == " ":
            return 8
    # se o jogador jogar na posição 8 e 1, o computador deve jogar na posição 4,6,7,9
    if tabuleiro[8] == simboloJogador and tabuleiro[1] == simboloJogador:
        if tabuleiro[4] == " ":
            return 4
        if tabuleiro[6] == " ":
            return 6
        if tabuleiro[7] == " ":
            return 7
        if tabuleiro[9] == " ":
            return 9
    # se o jogador jogar na posição 8 e 2, o computador deve jogar na posição 4,6
    if tabuleiro[8] == simboloJogador and tabuleiro[2] == simboloJogador:
        if tabuleiro[4] == " ":
            return 4
        if tabuleiro[6] == " ":
            return 6
    # se o jogador jogar na posição 8 e 3, o computador deve jogar na posição 4,6,7,9
    if tabuleiro[8] == simboloJogador and tabuleiro[3] == simboloJogador:
        if tabuleiro[4] == " ":
            return 4
        if tabuleiro[6] == " ":
            return 6
        if tabuleiro[7] == " ":
            return 7
        if tabuleiro[9] == " ":
            return 9
    # se o jogador jogar na posição 8 e 4, o computador deve jogar na posição 1,7,9
    if tabuleiro[8] == simboloJogador and tabuleiro[4] == simboloJogador:
        if tabuleiro[1] == " ":
            return 1
        if tabuleiro[7] == " ":
            return 7
        if tabuleiro[9] == " ":
            return 9
    # se o jogador jogar na posição 8 e 6, o computador deve jogar na posição 3,7,9
    if tabuleiro[8] == simboloJogador and tabuleiro[6] == simboloJogador:
        if tabuleiro[3] == " ":
            return 3
        if tabuleiro[7] == " ":
            return 7
        if tabuleiro[9] == " ":
            return 9
    # se o jogador jogar na posição 8 e 7, o computador deve jogar na posição 9
    if tabuleiro[8] == simboloJogador and tabuleiro[7] == simboloJogador:
        if tabuleiro[9] == " ":
            return 9
    # se o jogador jogar na posição 8 e 9, o computador deve jogar na posição 7
    if tabuleiro[8] == simboloJogador and tabuleiro[9] == simboloJogador:
        if tabuleiro[7] == " ":
            return 7
    # se o jogador jogar na posição 9 e 1, o computador deve jogar na posição 4,6
    if tabuleiro[9] == simboloJogador and tabuleiro[1] == simboloJogador:
        if tabuleiro[4] == " ":
            return 4
        if tabuleiro[6] == " ":
            return 6
    # se o jogador jogar na posição 9 e 2, o computador deve jogar na posição 1,4,6
    if tabuleiro[9] == simboloJogador and tabuleiro[2] == simboloJogador:
        if tabuleiro[1] == " ":
            return 1
        if tabuleiro[4] == " ":
            return 4
        if tabuleiro[6] == " ":
            return 6
    # se o jogador jogar na posição 9 e 3, o computador deve jogar na posição 6
    if tabuleiro[9] == simboloJogador and tabuleiro[3] == simboloJogador:
        if tabuleiro[6] == " ":
            return 6
    # se o jogador jogar na posição 9 e 4, o computador deve jogar na posição 1,2,3,7,8
    if tabuleiro[9] == simboloJogador and tabuleiro[4] == simboloJogador:
        if tabuleiro[1] == " ":
            return 1
        if tabuleiro[2] == " ":
            return 2
        if tabuleiro[3] == " ":
            return 3
        if tabuleiro[7] == " ":
            return 7
        if tabuleiro[8] == " ":
            return 8
    # se o jogador jogar na posição 9 e 6, o computador deve jogar na posição 3
    if tabuleiro[9] == simboloJogador and tabuleiro[6] == simboloJogador:
        if tabuleiro[3] == " ":
            return 3
    # se o jogador jogar na posição 9 e 7, o computador deve jogar na posição 8
    if tabuleiro[9] == simboloJogador and tabuleiro[7] == simboloJogador:
        if tabuleiro[8] == " ":
            return 8
    # se o jogador jogar na posição 9 e 8, o computador deve jogar na posição 7
    if tabuleiro[9] == simboloJogador and tabuleiro[8] == simboloJogador:
        if tabuleiro[7] == " ":
            return 7
    # se o jogado jogar na posição 6 e 1, o computador deve jogar na posição 2,3,8
    if tabuleiro[6] == simboloJogador and tabuleiro[1] == simboloJogador:
        if tabuleiro[2] == " ":
            return 2
        if tabuleiro[3] == " ":
            return 3
        if tabuleiro[8] == " ":
            return 8
    # se o jogador jogar na posição 6 e 2, o computador deve jogar na posição 1,3,9
    if tabuleiro[6] == simboloJogador and tabuleiro[2] == simboloJogador:
        if tabuleiro[1] == " ":
            return 1
        if tabuleiro[3] == " ":
            return 3
        if tabuleiro[9] == " ":
            return 9
    # se o jogador jogar na posição 6 e 3, o computador deve jogar na posição 9
    if tabuleiro[6] == simboloJogador and tabuleiro[3] == simboloJogador:
        if tabuleiro[9] == " ":
            return 9
    # se o jogador jogar na posição 6 e 4, o computador deve jogar na posição 8,2
    if tabuleiro[6] == simboloJogador and tabuleiro[4] == simboloJogador:
        if tabuleiro[8] == " ":
            return 8
        if tabuleiro[2] == " ":
            return 2
    # se o jogador jogar na posição 6 e 7, o computador deve jogar na posição 2,3,9
    if tabuleiro[6] == simboloJogador and tabuleiro[7] == simboloJogador:
        if tabuleiro[2] == " ":
            return 2
        if tabuleiro[3] == " ":
            return 3
        if tabuleiro[9] == " ":
            return 9
    # se o jogador jogar na posição 6 e 8, o computador deve jogar na posição 3,7,9
    if tabuleiro[6] == simboloJogador and tabuleiro[8] == simboloJogador:
        if tabuleiro[3] == " ":
            return 3
        if tabuleiro[7] == " ":
            return 7
        if tabuleiro[9] == " ":
            return 9
    # se o jogador jogar na posição 6 e 9, o computador deve jogar na posição 3
    if tabuleiro[6] == simboloJogador and tabuleiro[9] == simboloJogador:
        if tabuleiro[3] == " ":
            return 3
    # se o jogador jogar na posição 3 e 1, o computador deve jogar na posição 2
    if tabuleiro[3] == simboloJogador and tabuleiro[1] == simboloJogador:
        if tabuleiro[2] == " ":
            return 2
    # se o jogador jogar na posição 3 e 2, o computador deve jogar na posição 1
    if tabuleiro[3] == simboloJogador and tabuleiro[2] == simboloJogador:
        if tabuleiro[1] == " ":
            return 1
    # se o jogador jogar na posição 3 e 4, o computador deve jogar na posição 1,2,7,8
    if tabuleiro[3] == simboloJogador and tabuleiro[4] == simboloJogador:
        if tabuleiro[1] == " ":
            return 1
        if tabuleiro[2] == " ":
            return 2
        if tabuleiro[7] == " ":
            return 7
        if tabuleiro[8] == " ":
            return 8
    # se o jogador jogar na posição 3 e 6, o computador deve jogar na posição 9
    if tabuleiro[3] == simboloJogador and tabuleiro[6] == simboloJogador:
        if tabuleiro[9] == " ":
            return 9
    # se o jogador jogar na posição 3 e 7, o computador deve jogar na posição 2,4,6,8
    if tabuleiro[3] == simboloJogador and tabuleiro[7] == simboloJogador:
        if tabuleiro[2] == " ":
            return 2
        if tabuleiro[4] == " ":
            return 4
        if tabuleiro[6] == " ":
            return 6
        if tabuleiro[8] == " ":
            return 8
    # se o jogador jogar na posição 3 e 8, o computador deve jogar na posição 1,4,7,9
    if tabuleiro[3] == simboloJogador and tabuleiro[8] == simboloJogador:
        if tabuleiro[1] == " ":
            return 1
        if tabuleiro[4] == " ":
            return 4
        if tabuleiro[7] == " ":
            return 7
        if tabuleiro[9] == " ":
            return 9
    # se o jogador jogar na posição 3 e 9, o computador deve jogar na posição 6
    if tabuleiro[3] == simboloJogador and tabuleiro[9] == simboloJogador:
        if tabuleiro[6] == " ":
            return 6
    # se o jogador jogar na posição 2 e 1, o computador deve jogar na posição 3
    if tabuleiro[2] == simboloJogador and tabuleiro[1] == simboloJogador:
        if tabuleiro[3] == " ":
            return 3
    # se o jogador jogar na posição 2 e 3, o computador deve jogar na posição 1
    if tabuleiro[2] == simboloJogador and tabuleiro[3] == simboloJogador:
        if tabuleiro[1] == " ":
            return 1
    # se o jogador jogar na posição 2 e 4, o computador deve jogar na posição 1,3,7
    if tabuleiro[2] == simboloJogador and tabuleiro[4] == simboloJogador:
        if tabuleiro[1] == " ":
            return 1
        if tabuleiro[3] == " ":
            return 3
        if tabuleiro[7] == " ":
            return 7
    # se o jogador jogar na posição 2 e 6, o computador deve jogar na posição 1,3,9
    if tabuleiro[2] == simboloJogador and tabuleiro[6] == simboloJogador:
        if tabuleiro[1] == " ":
            return 1
        if tabuleiro[3] == " ":
            return 3
        if tabuleiro[9] == " ":
            return 9
    # se o jogador jogar na posição 2 e 7, o computador deve jogar na posição 1,3,4,6
    if tabuleiro[2] == simboloJogador and tabuleiro[7] == simboloJogador:
        if tabuleiro[1] == " ":
            return 1
        if tabuleiro[3] == " ":
            return 3
        if tabuleiro[4] == " ":
            return 4
        if tabuleiro[6] == " ":
            return 6
    # se o jogador jogar na posição 2 e 8, o computador deve jogar na posição 4,6
    if tabuleiro[2] == simboloJogador and tabuleiro[8] == simboloJogador:
        if tabuleiro[4] == " ":
            return 4
        if tabuleiro[6] == " ":
            return 6
    # se o jogador jogar na posição 2 e 9, o computador deve jogar na posição 1,3,4,6,7
    if tabuleiro[2] == simboloJogador and tabuleiro[9] == simboloJogador:
        if tabuleiro[1] == " ":
            return 1
        if tabuleiro[3] == " ":
            return 3
        if tabuleiro[4] == " ":
            return 4
        if tabuleiro[6] == " ":
            return 6
        if tabuleiro[7] == " ":
            return 7
    # se o jogador jogar na posição 5 e 1, o computador deve jogar na posição 9
    if tabuleiro[5] == simboloJogador and tabuleiro[1] == simboloJogador:
        if tabuleiro[9] == " ":
            return 9
    # se o jogador jogar na posição 1 e 5, o computador deve jogar na posição 9
    if tabuleiro[1] == simboloJogador and tabuleiro[5] == simboloJogador:
        if tabuleiro[9] == " ":
            return 9
    # se o jogador jogar na posição 5 e 2, o computador deve jogar na posição 8
    if tabuleiro[5] == simboloJogador and tabuleiro[2] == simboloJogador:
        if tabuleiro[8] == " ":
            return 8
    # se o jogador jogar na posição 2 e 5, o computador deve jogar na posição 8
    if tabuleiro[2] == simboloJogador and tabuleiro[5] == simboloJogador:
        if tabuleiro[8] == " ":
            return 8
    # se o jogador jogar na posição 5 e 3, o computador deve jogar na posição 7
    if tabuleiro[5] == simboloJogador and tabuleiro[3] == simboloJogador:
        if tabuleiro[7] == " ":
            return 7
    # so o jogador jogar na posição 3 e 5, o computador deve jogar na posição 7
    if tabuleiro[3] == simboloJogador and tabuleiro[5] == simboloJogador:
        if tabuleiro[7] == " ":
            return 7

    # se o jogador jogar na posição 5 e 4, o computador deve jogar na posição 6
    if tabuleiro[5] == simboloJogador and tabuleiro[4] == simboloJogador:
        if tabuleiro[6] == " ":
            return 6
    # se o jogador jogar na posição 4 e 5, o computador deve jogar na posição 6
    if tabuleiro[4] == simboloJogador and tabuleiro[5] == simboloJogador:
        if tabuleiro[6] == " ":
            return 6

    # se o jogador jogar na posição 5 e 6, o computador deve jogar na posição 4
    if tabuleiro[5] == simboloJogador and tabuleiro[6] == simboloJogador:
        if tabuleiro[4] == " ":
            return 4
    # se o jogador jogar na posição 6 e 5, o computador deve jogar na posição 4
    if tabuleiro[6] == simboloJogador and tabuleiro[5] == simboloJogador:
        if tabuleiro[4] == " ":
            return 4
    # se o jogador jogar na posição 5 e 7, o computador deve jogar na posição 3
    if tabuleiro[5] == simboloJogador and tabuleiro[7] == simboloJogador:
        if tabuleiro[3] == " ":
            return 3
    # se o jogador jogar na posição 7 e 5, o computador deve jogar na posição 3
    if tabuleiro[7] == simboloJogador and tabuleiro[5] == simboloJogador:
        if tabuleiro[3] == " ":
            return 3
    # se o jogador jogar na posição 5 e 8, o computador deve jogar na posição 2
    if tabuleiro[5] == simboloJogador and tabuleiro[8] == simboloJogador:
        if tabuleiro[2] == " ":
            return 2
    # se o jogador jogar na posição 8 e 5, o computador deve jogar na posição 2
    if tabuleiro[8] == simboloJogador and tabuleiro[5] == simboloJogador:
        if tabuleiro[2] == " ":
            return 2
    # se o jogador jogar na posição 5 e 9, o computador deve jogar na posição 1
    if tabuleiro[5] == simboloJogador and tabuleiro[9] == simboloJogador:
        if tabuleiro[1] == " ":
            return 1
    # se o jogador jogar na posição 9 e 5, o computador deve jogar na posição 1
    if tabuleiro[9] == simboloJogador and tabuleiro[5] == simboloJogador:
        if tabuleiro[1] == " ":
            return 1
    # se o jogador jogar na posição 5, o computador deve jogar an posição 1,3,7,9
    if tabuleiro[5] == simboloJogador:
        if tabuleiro[1] == " ":
            return 1
        if tabuleiro[3] == " ":
            return 3
        if tabuleiro[7] == " ":
            return 7
        if tabuleiro[9] == " ":
            return 9

    listaDesocupado = []

    if tabuleiro[1] == " ":
        listaDesocupado = listaDesocupado+[1]

    if tabuleiro[2] == " ":
        listaDesocupado = listaDesocupado+[2]

    if tabuleiro[3] == " ":
        listaDesocupado = listaDesocupado+[3]

    if tabuleiro[4] == " ":
        listaDesocupado = listaDesocupado+[4]

    if tabuleiro[5] == " ":
        listaDesocupado = listaDesocupado+[5]

    if tabuleiro[6] == " ":
        listaDesocupado = listaDesocupado+[6]

    if tabuleiro[7] == " ":
        listaDesocupado = listaDesocupado+[7]

    if tabuleiro[8] == " ":
        listaDesocupado = listaDesocupado+[8]

    if tabuleiro[9] == " ":
        listaDesocupado = listaDesocupado+[9]

    return random.choice(listaDesocupado)


def main():
    limpaTela()
    jogador = escolhaXO()
    if jogador == "X":
        computador = "O"
    else:
        computador = "X"

    listaTabuleiro = [" "]*10

    vez = random.choice(["X", "O"])

    jogo(listaTabuleiro, vez, jogador, computador)


################################
## NÃO ALTERE O CÓDIGO ABAIXO ##
################################
if __name__ == "__main__":
    main()
