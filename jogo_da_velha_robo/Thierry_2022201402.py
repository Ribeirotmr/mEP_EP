######################################################
# Programção I / Programação Funcional (2023/1)
# EP2 - Jogo da Velha
# Nome: Thierry Martins Ribeiro
# Matrícula: 2022201402
######################################################

import random


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





def abertura():
    """
    Imprime a tela de abertura do jogo, com o nome do jogo
    """
    print(
        "\033[34m       __    ______     _______   ______       _______       ___         ____    ____  _______  __       __    __       ___ \033[0m"
    )
    print(
        "\033[34m      |  |  /  __  \   /  _____| /  __  \     |       \     /   \        \   \  /   / |   ____||  |     |  |  |  |     /   \ \033[0m"
    )
    print(
        "\033[33m      |  | |  |  |  | |  |  __  |  |  |  |    |  .--.  |   /  ^  \        \   \/   /  |  |__   |  |     |  |__|  |    /  ^  \ \033[0m"
    )
    print(
        "\033[31m.--.  |  | |  |  |  | |  | |_ | |  |  |  |    |  |  |  |  /  /_\  \        \      /   |   __|  |  |     |   __   |   /  /_\  \ \033[0m"
    )
    print(
        "\033[32m|  `--'  | |  `--'  | |  |__| | |  `--'  |    |  '--'  | /  _____  \        \    /    |  |____ |  `----.|  |  |  |  /  _____  \ \033[0m"
    )
    print(
        "\033[32m \______/   \______/   \______|  \______/     |_______/ /__/     \__\        \__/     |_______||_______||__|  |__| /__/     \__\ \033[0m"
    )


def imprimir_simbolo(simbolo, posicao):
    """
    Funcao que imprime o simbolo X, O ou espaco vazio, de acordo com a posicao (que é a linha) que esta sendo impressa
    """
    if simbolo == "O":
        if posicao == 2 or posicao == 9:
            return "\033[33m      " + "██" * 4 + "      \033[0m"
        if posicao == 3 or posicao == 8:
            return "\033[33m    ██" + " " * 8 + "██    \033[0m"
        if posicao >= 4 and posicao <= 7:
            return "\033[33m  ██" + " " * 12 + "██  \033[0m"

    if simbolo == "X":
        if posicao == 2 or posicao == 9:
            return "\033[34m  ██" + " " * 12 + "██  \033[0m"
        if posicao == 3 or posicao == 8:
            return "\033[34m    ██" + " " * 8 + "██    \033[0m"
        if posicao == 4 or posicao == 7:
            return "\033[34m      ██" + " " * 4 + "██      \033[0m"
        if posicao == 5 or posicao == 6:
            return "\033[34m        ████        \033[0m"
    # vazio
    return " " * 20


def tabuleiro_linha(L, linha):
    """
    Imprime os simbolos de uma linha do tabuleiro
    """
    print(
        imprimir_simbolo(L[linha], 1)
        + "\033[32m██"
        + imprimir_simbolo(L[linha + 1], 1)
        + "\033[0m██"
        + imprimir_simbolo(L[linha + 2], 1)
    )
    print(
        imprimir_simbolo(L[linha], 2)
        + "\033[32m██"
        + imprimir_simbolo(L[linha + 1], 2)
        + "\033[0m██"
        + imprimir_simbolo(L[linha + 2], 2)
    )
    print(
        imprimir_simbolo(L[linha], 3)
        + "\033[32m██"
        + imprimir_simbolo(L[linha + 1], 3)
        + "\033[0m██"
        + imprimir_simbolo(L[linha + 2], 3)
    )
    print(
        imprimir_simbolo(L[linha], 4)
        + "\033[32m██"
        + imprimir_simbolo(L[linha + 1], 4)
        + "\033[0m██"
        + imprimir_simbolo(L[linha + 2], 4)
    )
    print(
        imprimir_simbolo(L[linha], 5)
        + "\033[32m██"
        + imprimir_simbolo(L[linha + 1], 5)
        + "\033[0m██"
        + imprimir_simbolo(L[linha + 2], 5)
    )
    print(
        imprimir_simbolo(L[linha], 6)
        + "\033[32m██"
        + imprimir_simbolo(L[linha + 1], 6)
        + "\033[0m██"
        + imprimir_simbolo(L[linha + 2], 6)
    )
    print(
        imprimir_simbolo(L[linha], 7)
        + "\033[32m██"
        + imprimir_simbolo(L[linha + 1], 7)
        + "\033[0m██"
        + imprimir_simbolo(L[linha + 2], 7)
    )
    print(
        imprimir_simbolo(L[linha], 8)
        + "\033[32m██"
        + imprimir_simbolo(L[linha + 1], 8)
        + "\033[0m██"
        + imprimir_simbolo(L[linha + 2], 8)
    )
    print(
        imprimir_simbolo(L[linha], 9)
        + "\033[32m██"
        + imprimir_simbolo(L[linha + 1], 9)
        + "\033[0m██"
        + imprimir_simbolo(L[linha + 2], 9)
    )
    print(
        imprimir_simbolo(L[linha], 10)
        + "\033[32m██"
        + imprimir_simbolo(L[linha + 1], 10)
        + "\033[0m██"
        + imprimir_simbolo(L[linha + 2], 10)
    )


def tabuleiro(L):
    """
    Imprime o tabuleiro inteiro, primeiro a linha 7, depois a linha 4 e por ultimo a linha 1
    """
    tabuleiro_linha(L[:], 7)
    print("\033[36m" + "█" * 64 + "\033[0m")
    tabuleiro_linha(L[:], 4)
    print("\033[36m" + "█" * 64 + "\033[0m")
    tabuleiro_linha(L[:], 1)


def primeiro_a_jogar():
    """
    Retorna quem vai jogar primeiro, o computador ou o jogador humano, além de imprimir na tela o mesmo
    """
    if random.choice([0, 1]) == 0:
        print("\033[31mO Computador começa\033[0m")
        return "C"
    else:
        print("\033[31mO Jogador começa\033[0m")
        return "H"


def escolhe_bola_xis():
    """
    Função que escolhe se o jogador humano vai jogar com X ou O
    """
    escolhe = input("\033[33mEscolha X ou O: \033[0m")
    if escolhe != "X" and escolhe != "x" and escolhe != "O" and escolhe != "o":
        # tratamento de erro
        print("\033[31mEscolha inválida\033[0m")
        return escolhe_bola_xis()
    else:
        # converte para maiúsculo
        if escolhe == "x":
            escolhe = "X"
        elif escolhe == "o":
            escolhe = "O"
        return escolhe


def escolher_numero():
    """
    Funcao que escolhe um numero entre 1 e 9, caso o numero seja invalido
    a função deve chamar a si mesma para escolher outro numero ate que o mesmo seja valido
    """
    try:
        escolhe = int(input("\033[1m\033[34mEscolha um número entre 1 e 9: \033[0m"))
        if escolhe < 1 or escolhe > 9:
            print("\033[1m\033[31mEscolha inválida\033[0m")
            return escolher_numero()
        return escolhe
    except:
        # tratamento de erro
        print("\033[1mEscolha de 1 a 9\033[0m")
        return escolher_numero()


def escolha_posicao(L, simbolo):
    """
    Funcao que escolhe a posicao que o jogador humano vai jogar, caso a posicao ja esteja ocupada, a funcao chama a si mesma para escolher outra posicao
    """
    posicao = escolher_numero()
    if L[posicao] == " ":
        L[posicao] = simbolo
    else:
        print("\033[1m\033[31mPosição já ocupada \033[31m\033[0m")
        return escolha_posicao(L[:], simbolo)
    return L


def jogada_jogador(tabuleiro, simboloJogador):
    """
    Recebe o tabuleiro e o simbolo (X ou O) do jogador e determina onde o jogador deve jogar
    """
    posicao = escolher_numero()
    tabuleiro = escolha_posicao(tabuleiro[:], posicao, simboloJogador)
    return tabuleiro


def contar_simbolo(L, simbolo):
    """
    Recebe quantas vezes um simbolo aparece em uma lista
    """
    return len(list(filter(lambda x: x == simbolo, L)))


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

    Estratégia: Resumidamente, o computador deve sempre tentar ganhar o jogo, bloquear o jogador de ganhar ou tentar empatar.
    Ele joga jogadas aleatórias quando jogadas especiais para determinados casos não foram implementadas/necessárias.
    Ele sempre começa jogando nos cantos se for primeiro a jogar.
    Se for o segundo, ele joga no meio se o jogador jogou em um canto, ou joga em um canto se o jogador jogou no meio.
    Ele tenta ganhar se o computador tiver 2 símbolos em uma linha, coluna ou diagonal.
    Ele tenta bloquear o jogador de ganhar se o jogador tiver 2 símbolos em uma linha, coluna ou diagonal.
    Se o computador não pode ganhar ou bloquear o jogador de ganhar, ele tenta empatar.
    """

    if simboloComputador == "X":
        simbolo_jogador = "O"
    else:
        simbolo_jogador = "X"

    # conta quantas vezes o jogador jogou
    jogador_jogou_quantas = contar_simbolo(tabuleiro[:], simbolo_jogador)
    # conta quantas vezes o computador jogou
    computador_jogou_quantas = contar_simbolo(tabuleiro[:], simboloComputador)

    # estrategia quando o computador comeca
    if jogador_jogou_quantas == 0 and computador_jogou_quantas == 0:
        return random.choice([1, 3, 7, 9])

    if jogador_jogou_quantas == 1 and computador_jogou_quantas == 1:
        if tabuleiro[1] == simboloComputador and tabuleiro[9] == simbolo_jogador:
            return random.choice([3, 7])
        if tabuleiro[3] == simboloComputador and tabuleiro[7] == simbolo_jogador:
            return random.choice([1, 9])
        if tabuleiro[7] == simboloComputador and tabuleiro[3] == simbolo_jogador:
            return random.choice([1, 9])
        if tabuleiro[9] == simboloComputador and tabuleiro[1] == simbolo_jogador:
            return random.choice([3, 7])

        if tabuleiro[5] == simbolo_jogador:
            if tabuleiro[1] == simboloComputador:
                return random.choice([8, 6])
            if tabuleiro[3] == simboloComputador:
                return random.choice([4, 8])
            if tabuleiro[7] == simboloComputador:
                return random.choice([2, 6])
            if tabuleiro[9] == simboloComputador:
                return random.choice([2, 4])

        if tabuleiro[1] == simboloComputador and tabuleiro[2] == simbolo_jogador:
            return 7
        if tabuleiro[1] == simboloComputador and tabuleiro[4] == simbolo_jogador:
            return 3
        if tabuleiro[3] == simboloComputador and tabuleiro[2] == simbolo_jogador:
            return 9
        if tabuleiro[3] == simboloComputador and tabuleiro[6] == simbolo_jogador:
            return 1
        if tabuleiro[7] == simboloComputador and tabuleiro[8] == simbolo_jogador:
            return 1
        if tabuleiro[7] == simboloComputador and tabuleiro[4] == simbolo_jogador:
            return 9
        if tabuleiro[9] == simboloComputador and tabuleiro[6] == simbolo_jogador:
            return 7
        if tabuleiro[9] == simboloComputador and tabuleiro[8] == simbolo_jogador:
            return 3

        if (
            tabuleiro[1] == simboloComputador
            or tabuleiro[3] == simboloComputador
            or tabuleiro[7] == simboloComputador
            or tabuleiro[9] == simboloComputador
        ) and (
            tabuleiro[2] == simbolo_jogador
            or tabuleiro[4] == simbolo_jogador
            or tabuleiro[6] == simbolo_jogador
            or tabuleiro[8] == simbolo_jogador
        ):
            return 5

    if jogador_jogou_quantas == 2 and computador_jogou_quantas == 2:
        if tabuleiro[1] == simboloComputador:
            if (
                tabuleiro[2] == simbolo_jogador
                and tabuleiro[7] == simboloComputador
                and tabuleiro[4] == simbolo_jogador
            ):
                return 5
            if (
                tabuleiro[4] == simbolo_jogador
                and tabuleiro[3] == simboloComputador
                and tabuleiro[2] == simbolo_jogador
            ):
                return 5
            if (
                tabuleiro[5] == simbolo_jogador
                and tabuleiro[6] == simboloComputador
                and tabuleiro[9] == simbolo_jogador
            ):
                return 7
            if (
                tabuleiro[5] == simbolo_jogador
                and tabuleiro[8] == simboloComputador
                and tabuleiro[9] == simbolo_jogador
            ):
                return 3
        if tabuleiro[3] == simboloComputador:
            if (
                tabuleiro[2] == simbolo_jogador
                and tabuleiro[9] == simboloComputador
                and tabuleiro[6] == simbolo_jogador
            ):
                return 5
            if (
                tabuleiro[6] == simbolo_jogador
                and tabuleiro[1] == simboloComputador
                and tabuleiro[2] == simbolo_jogador
            ):
                return 5
            if (
                tabuleiro[5] == simbolo_jogador
                and tabuleiro[4] == simboloComputador
                and tabuleiro[7] == simbolo_jogador
            ):
                return 9
            if (
                tabuleiro[5] == simbolo_jogador
                and tabuleiro[8] == simboloComputador
                and tabuleiro[7] == simbolo_jogador
            ):
                return 1
        if tabuleiro[7] == simboloComputador:
            if (
                tabuleiro[8] == simbolo_jogador
                and tabuleiro[1] == simboloComputador
                and tabuleiro[4] == simbolo_jogador
            ):
                return 5
            if (
                tabuleiro[4] == simbolo_jogador
                and tabuleiro[9] == simboloComputador
                and tabuleiro[8] == simbolo_jogador
            ):
                return 5
            if (
                tabuleiro[5] == simbolo_jogador
                and tabuleiro[2] == simboloComputador
                and tabuleiro[3] == simbolo_jogador
            ):
                return 9
            if (
                tabuleiro[5] == simbolo_jogador
                and tabuleiro[6] == simboloComputador
                and tabuleiro[3] == simbolo_jogador
            ):
                return 1
        if tabuleiro[9] == simboloComputador:
            if (
                tabuleiro[8] == simbolo_jogador
                and tabuleiro[3] == simboloComputador
                and tabuleiro[6] == simbolo_jogador
            ):
                return 5
            if (
                tabuleiro[6] == simbolo_jogador
                and tabuleiro[7] == simboloComputador
                and tabuleiro[8] == simbolo_jogador
            ):
                return 5
            if (
                tabuleiro[5] == simbolo_jogador
                and tabuleiro[4] == simboloComputador
                and tabuleiro[1] == simbolo_jogador
            ):
                return 3
            if (
                tabuleiro[5] == simbolo_jogador
                and tabuleiro[2] == simboloComputador
                and tabuleiro[1] == simbolo_jogador
            ):
                return 7

    # estrategia quando o jogador comeca
    if (
        tabuleiro[1] == simbolo_jogador
        and jogador_jogou_quantas == 1
        and computador_jogou_quantas == 0
    ):
        return 5
    if (
        tabuleiro[3] == simbolo_jogador
        and jogador_jogou_quantas == 1
        and computador_jogou_quantas == 0
    ):
        return 5
    if (
        tabuleiro[7] == simbolo_jogador
        and jogador_jogou_quantas == 1
        and computador_jogou_quantas == 0
    ):
        return 5
    if (
        tabuleiro[9] == simbolo_jogador
        and jogador_jogou_quantas == 1
        and computador_jogou_quantas == 0
    ):
        return 5
    if (
        tabuleiro[2] == simbolo_jogador
        and jogador_jogou_quantas == 1
        and computador_jogou_quantas == 0
    ):
        return 5
    if (
        tabuleiro[4] == simbolo_jogador
        and jogador_jogou_quantas == 1
        and computador_jogou_quantas == 0
    ):
        return 5
    if (
        tabuleiro[6] == simbolo_jogador
        and jogador_jogou_quantas == 1
        and computador_jogou_quantas == 0
    ):
        return 5
    if (
        tabuleiro[8] == simbolo_jogador
        and jogador_jogou_quantas == 1
        and computador_jogou_quantas == 0
    ):
        return 5
    if (
        tabuleiro[5] == simbolo_jogador
        and jogador_jogou_quantas == 1
        and computador_jogou_quantas == 0
    ):
        return random.choice([1, 3, 7, 9])

    # quando o computador tem 2 simbolos em linha
    if (
        tabuleiro[1] == simboloComputador
        and tabuleiro[2] == simboloComputador
        and tabuleiro[3] == " "
    ):
        return 3
    if (
        tabuleiro[1] == simboloComputador
        and tabuleiro[3] == simboloComputador
        and tabuleiro[2] == " "
    ):
        return 2
    if (
        tabuleiro[2] == simboloComputador
        and tabuleiro[3] == simboloComputador
        and tabuleiro[1] == " "
    ):
        return 1

    if (
        tabuleiro[4] == simboloComputador
        and tabuleiro[5] == simboloComputador
        and tabuleiro[6] == " "
    ):
        return 6
    if (
        tabuleiro[4] == simboloComputador
        and tabuleiro[6] == simboloComputador
        and tabuleiro[5] == " "
    ):
        return 5
    if (
        tabuleiro[5] == simboloComputador
        and tabuleiro[6] == simboloComputador
        and tabuleiro[4] == " "
    ):
        return 4

    if (
        tabuleiro[7] == simboloComputador
        and tabuleiro[8] == simboloComputador
        and tabuleiro[9] == " "
    ):
        return 9
    if (
        tabuleiro[7] == simboloComputador
        and tabuleiro[9] == simboloComputador
        and tabuleiro[8] == " "
    ):
        return 8
    if (
        tabuleiro[8] == simboloComputador
        and tabuleiro[9] == simboloComputador
        and tabuleiro[7] == " "
    ):
        return 7

    # quando o computador tem 2 simbolos em coluna
    if (
        tabuleiro[1] == simboloComputador
        and tabuleiro[4] == simboloComputador
        and tabuleiro[7] == " "
    ):
        return 7
    if (
        tabuleiro[1] == simboloComputador
        and tabuleiro[7] == simboloComputador
        and tabuleiro[4] == " "
    ):
        return 4
    if (
        tabuleiro[4] == simboloComputador
        and tabuleiro[7] == simboloComputador
        and tabuleiro[1] == " "
    ):
        return 1

    if (
        tabuleiro[2] == simboloComputador
        and tabuleiro[5] == simboloComputador
        and tabuleiro[8] == " "
    ):
        return 8
    if (
        tabuleiro[2] == simboloComputador
        and tabuleiro[8] == simboloComputador
        and tabuleiro[5] == " "
    ):
        return 5
    if (
        tabuleiro[5] == simboloComputador
        and tabuleiro[8] == simboloComputador
        and tabuleiro[2] == " "
    ):
        return 2

    if (
        tabuleiro[3] == simboloComputador
        and tabuleiro[6] == simboloComputador
        and tabuleiro[9] == " "
    ):
        return 9
    if (
        tabuleiro[3] == simboloComputador
        and tabuleiro[9] == simboloComputador
        and tabuleiro[6] == " "
    ):
        return 6
    if (
        tabuleiro[6] == simboloComputador
        and tabuleiro[9] == simboloComputador
        and tabuleiro[3] == " "
    ):
        return 3

    # quando o computador tem 2 simbolos em diagonal
    if (
        tabuleiro[1] == simboloComputador
        and tabuleiro[5] == simboloComputador
        and tabuleiro[9] == " "
    ):
        return 9
    if (
        tabuleiro[1] == simboloComputador
        and tabuleiro[9] == simboloComputador
        and tabuleiro[5] == " "
    ):
        return 5
    if (
        tabuleiro[5] == simboloComputador
        and tabuleiro[9] == simboloComputador
        and tabuleiro[1] == " "
    ):
        return 1

    if (
        tabuleiro[3] == simboloComputador
        and tabuleiro[5] == simboloComputador
        and tabuleiro[7] == " "
    ):
        return 7
    if (
        tabuleiro[3] == simboloComputador
        and tabuleiro[7] == simboloComputador
        and tabuleiro[5] == " "
    ):
        return 5
    if (
        tabuleiro[5] == simboloComputador
        and tabuleiro[7] == simboloComputador
        and tabuleiro[3] == " "
    ):
        return 3

    # quando o jogador tem 2 simbolos em linha
    if (
        tabuleiro[1] == simbolo_jogador
        and tabuleiro[2] == simbolo_jogador
        and tabuleiro[3] == " "
    ):
        return 3
    if (
        tabuleiro[1] == simbolo_jogador
        and tabuleiro[3] == simbolo_jogador
        and tabuleiro[2] == " "
    ):
        return 2
    if (
        tabuleiro[2] == simbolo_jogador
        and tabuleiro[3] == simbolo_jogador
        and tabuleiro[1] == " "
    ):
        return 1

    if (
        tabuleiro[4] == simbolo_jogador
        and tabuleiro[5] == simbolo_jogador
        and tabuleiro[6] == " "
    ):
        return 6
    if (
        tabuleiro[4] == simbolo_jogador
        and tabuleiro[6] == simbolo_jogador
        and tabuleiro[5] == " "
    ):
        return 5
    if (
        tabuleiro[5] == simbolo_jogador
        and tabuleiro[6] == simbolo_jogador
        and tabuleiro[4] == " "
    ):
        return 4

    if (
        tabuleiro[7] == simbolo_jogador
        and tabuleiro[8] == simbolo_jogador
        and tabuleiro[9] == " "
    ):
        return 9
    if (
        tabuleiro[7] == simbolo_jogador
        and tabuleiro[9] == simbolo_jogador
        and tabuleiro[8] == " "
    ):
        return 8
    if (
        tabuleiro[8] == simbolo_jogador
        and tabuleiro[9] == simbolo_jogador
        and tabuleiro[7] == " "
    ):
        return 7

    # quando o jogador tem 2 simbolos em coluna
    if (
        tabuleiro[1] == simbolo_jogador
        and tabuleiro[4] == simbolo_jogador
        and tabuleiro[7] == " "
    ):
        return 7
    if (
        tabuleiro[1] == simbolo_jogador
        and tabuleiro[7] == simbolo_jogador
        and tabuleiro[4] == " "
    ):
        return 4
    if (
        tabuleiro[4] == simbolo_jogador
        and tabuleiro[7] == simbolo_jogador
        and tabuleiro[1] == " "
    ):
        return 1

    if (
        tabuleiro[2] == simbolo_jogador
        and tabuleiro[5] == simbolo_jogador
        and tabuleiro[8] == " "
    ):
        return 8
    if (
        tabuleiro[2] == simbolo_jogador
        and tabuleiro[8] == simbolo_jogador
        and tabuleiro[5] == " "
    ):
        return 5
    if (
        tabuleiro[5] == simbolo_jogador
        and tabuleiro[8] == simbolo_jogador
        and tabuleiro[2] == " "
    ):
        return 2

    if (
        tabuleiro[3] == simbolo_jogador
        and tabuleiro[6] == simbolo_jogador
        and tabuleiro[9] == " "
    ):
        return 9
    if (
        tabuleiro[3] == simbolo_jogador
        and tabuleiro[9] == simbolo_jogador
        and tabuleiro[6] == " "
    ):
        return 6
    if (
        tabuleiro[6] == simbolo_jogador
        and tabuleiro[9] == simbolo_jogador
        and tabuleiro[3] == " "
    ):
        return 3

    # quando o jogador tem 2 simbolos em diagonal
    if (
        tabuleiro[1] == simbolo_jogador
        and tabuleiro[5] == simbolo_jogador
        and tabuleiro[9] == " "
    ):
        return 9
    if (
        tabuleiro[1] == simbolo_jogador
        and tabuleiro[9] == simbolo_jogador
        and tabuleiro[5] == " "
    ):
        return 5
    if (
        tabuleiro[5] == simbolo_jogador
        and tabuleiro[9] == simbolo_jogador
        and tabuleiro[1] == " "
    ):
        return 1

    if (
        tabuleiro[3] == simbolo_jogador
        and tabuleiro[5] == simbolo_jogador
        and tabuleiro[7] == " "
    ):
        return 7
    if (
        tabuleiro[3] == simbolo_jogador
        and tabuleiro[7] == simbolo_jogador
        and tabuleiro[5] == " "
    ):
        return 5
    if (
        tabuleiro[5] == simbolo_jogador
        and tabuleiro[7] == simbolo_jogador
        and tabuleiro[3] == " "
    ):
        return 3

    if jogador_jogou_quantas == 2 and computador_jogou_quantas == 1:
        # se o jogador jogou no meio
        if tabuleiro[5] == simbolo_jogador:
            if tabuleiro[1] == simboloComputador and tabuleiro[9] == simbolo_jogador:
                return random.choice([3, 7])
            if tabuleiro[3] == simboloComputador and tabuleiro[7] == simbolo_jogador:
                return random.choice([1, 9])
            if tabuleiro[7] == simboloComputador and tabuleiro[3] == simbolo_jogador:
                return random.choice([1, 9])
            if tabuleiro[9] == simboloComputador and tabuleiro[1] == simbolo_jogador:
                return random.choice([3, 7])
        # se o jogador começou no canto e jogou mais uma vez, joga na borda
        if tabuleiro[1] == simbolo_jogador and tabuleiro[6] == simbolo_jogador:
            return 3
        if tabuleiro[1] == simbolo_jogador and tabuleiro[8] == simbolo_jogador:
            return 7
        if tabuleiro[3] == simbolo_jogador and tabuleiro[4] == simbolo_jogador:
            return 1
        if tabuleiro[3] == simbolo_jogador and tabuleiro[8] == simbolo_jogador:
            return 9
        if tabuleiro[7] == simbolo_jogador and tabuleiro[2] == simbolo_jogador:
            return 1
        if tabuleiro[7] == simbolo_jogador and tabuleiro[6] == simbolo_jogador:
            return 9
        if tabuleiro[9] == simbolo_jogador and tabuleiro[2] == simbolo_jogador:
            return 3
        if tabuleiro[9] == simbolo_jogador and tabuleiro[4] == simbolo_jogador:
            return 7

        # se o jogador esta tentando fazer um "l"
        if tabuleiro[5] == simboloComputador:
            if tabuleiro[2] == simbolo_jogador and tabuleiro[4] == simbolo_jogador:
                return 1
            if tabuleiro[2] == simbolo_jogador and tabuleiro[6] == simbolo_jogador:
                return 3
            if tabuleiro[4] == simbolo_jogador and tabuleiro[8] == simbolo_jogador:
                return 7
            if tabuleiro[6] == simbolo_jogador and tabuleiro[8] == simbolo_jogador:
                return 9

        espacos_vazios = []
        if tabuleiro[2] == " ":
            espacos_vazios += [2]
        if tabuleiro[4] == " ":
            espacos_vazios += [4]
        if tabuleiro[6] == " ":
            espacos_vazios += [6]
        if tabuleiro[8] == " ":
            espacos_vazios += [8]

        return random.choice(espacos_vazios)

    # Se chegou até aqui, tem nehum caso especial, então joga aleatoriamente, já que tanto faz
    # jogando apenas nos espaços vazios
    jogadas = [i for i in range(1, 10) if tabuleiro[i] == " "]
    escolheu = random.choice(jogadas)
    return escolheu


def ganhador(L):
    """
    Recebe uma lista de tamanho 10 representando o tabuleiro e retorna o simbolo do ganhador (X ou O) ou
    a string "E" de empate caso não haja vencedor.

    Parâmetros:
    L: lista de tamanho 10 representando o tabuleiro

    Retorno:
    Simbolo do ganhador (X ou O) ou string "E" caso não haja vencedor
    """
    if L[1] == L[2] == L[3] != " ":
        return L[1]
    elif L[4] == L[5] == L[6] != " ":
        return L[4]
    elif L[7] == L[8] == L[9] != " ":
        return L[7]
    elif L[1] == L[4] == L[7] != " ":
        return L[1]
    elif L[2] == L[5] == L[8] != " ":
        return L[2]
    elif L[3] == L[6] == L[9] != " ":
        return L[3]
    elif L[1] == L[5] == L[9] != " ":
        return L[1]
    elif L[3] == L[5] == L[7] != " ":
        return L[3]
    elif (
        L[1] != " "
        and L[2] != " "
        and L[3] != " "
        and L[4] != " "
        and L[5] != " "
        and L[6] != " "
        and L[7] != " "
        and L[8] != " "
        and L[9] != " "
    ):
        return "E"
    else:
        return " "


def jogo(L, simbolo_jogador, jogador_atual):
    """
    Funcao principal recursiva do jogo da velha. Imprime o tabuleiro
    recebe a jogada do jogador atual, verifica se houve vencedor e chama a si mesma recursivamente
    caso não haja vencedor ou empate.
    """
    
    tabuleiro(L[:])
    if jogador_atual == "H":
        L = escolha_posicao(L[:], simbolo_jogador)
    else:
        if simbolo_jogador == "X":
            simbolo_computador = "O"
        else:
            simbolo_computador = "X"
        input("\033[33mAperte enter para o computador jogar\033[0m")
        escolheu = jogadaComputador(L[:], simbolo_computador)
        L[escolheu] = simbolo_computador
    if jogador_atual == "C":
        jogador_atual = "H"
    elif jogador_atual == "H":
        jogador_atual = "C"

    ganhou = ganhador(L[:])

    if ganhou == " ":
        return jogo(L[:], simbolo_jogador, jogador_atual)
    tabuleiro(L[:])
    if ganhou == "E":
        print("\033[34mDeu empate\033[0m")
    if ganhou == "H":
        print(f"\033[31mJogador ganhou\033[0m")
    if ganhou == "C":
        print(f"\033[34mComputador ganhou\033[0m")


def jogar_novamente():
    """
    Pergunta ao jogador se ele deseja jogar novamente e retorna True caso a resposta seja sim e False caso seja não.
    """
    opcao = input("\033[34m Deseja jogar novamente (S/N): \033[0m")
    if opcao.lower() == "s":
        return True
    if opcao.lower() == "n":
        return False
    print("\033[31m Opção inválida!\033[0m")
    return jogar_novamente()


def antes_jogo():
    """
    Prepara o jogo, chamando as funções de escolha de simbolo, sorteia quem começa e começa o jogo.
    """
    L = [" " for i in range(10)]
    simbolo_jogador = escolhe_bola_xis()
    primeiro = primeiro_a_jogar()
    jogo(L[:], simbolo_jogador, primeiro)
    jogar_denovo = jogar_novamente()

    if jogar_denovo == True:
        return antes_jogo()


def main():
    """
    Função principal do programa. Chama a função de abertura e a função que prepara o jogo.
    A abertura é chamada apenas uma vez, enquanto a preparação do jogo é chamada recursivamente caso o jogador deseje jogar novamente.
    """
    abertura()
    antes_jogo()


################################
## NÃO ALTERE O CÓDIGO ABAIXO ##
################################
if __name__ == "__main__":
    main()
