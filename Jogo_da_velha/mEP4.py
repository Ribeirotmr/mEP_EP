######################################################
# Programção I / Programação Funcional (2022/1)
# miniEP4 - Jogo da Velha
# Nome: Thierry Martins Ribeiro 
# Matrícula: 2022201402
######################################################

######################################################
# LEMBRE-SE:
# - Não é permitido usar estruturas de repetição,
#   funções impuras e operações que não sejam do 
#   Paradigma Funcional.
# - Você não pode usar variáveis globais;
# - Não use funções recursivas (não há necessidade);
# - Você deve seguir o código base disponibilizado, 
#   não sendo permitido a alteração do nome e/ou
#   lista de parâmetros das funções dadas;
# - Caso precise, você PODE criar outras funções;
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
    #Complete o código da função
    print(f" {p7} | {p8} | {p9} ")
    print("---+---+---")
    print(f" {p4} | {p5} | {p6} ")
    print("---+---+---")
    print(f" {p1} | {p2} | {p3} ")

def entradaValida(p1, p2, p3, p4, p5, p6, p7, p8, p9):
    """
    Recebe os valores das nove posições do tabuleiro e
    verifica se os valores são válidos, ou seja, retorna True
    se cada variável possui " " ou "x" ou "o" e False, caso contrário.
    """
    #Complete o código da função
    if verificarEntradaValida(p1) and verificarEntradaValida(p2) and verificarEntradaValida(p3) and verificarEntradaValida(p4) and verificarEntradaValida(p5) and verificarEntradaValida(p6) and verificarEntradaValida(p7) and verificarEntradaValida(p8) and verificarEntradaValida(p9):
        return True
    else:
        return False

def verificarEntradaValida(x):
    if x == "x" or x == "o" or x == " ":
        return True
    else:
        return False
    
    

    

def jogadaValida(p1, p2, p3, p4, p5, p6, p7, p8, p9):
    """
    Recebe os valores das nove posições do tabuleiro e
    verifica se os valores formam uma jogada válida.

    Retorna True se a jogada for válida e False, caso contrário
    """
    #Complete o código da função
    quantidade = 0 
    if p1 == "x":
        quantidade +=1  
    if p2 == "x":
        quantidade +=1
    if p3 == "x":
        quantidade +=1
    if p4 == "x":
        quantidade +=1
    if p5 == "x":
        quantidade +=1
    if p6 == "x":
        quantidade +=1
    if p7 == "x":
        quantidade +=1
    if p8 == "x":
        quantidade +=1
    if p9 == "x":
        quantidade +=1
    if p1 == "o":
        quantidade -=1  
    if p2 == "o":
        quantidade -=1
    if p3 == "o":
        quantidade -=1
    if p4 == "o":
        quantidade -=1
    if p5 == "o":
        quantidade -=1
    if p6 == "o":
        quantidade -=1
    if p7 == "o":
        quantidade -=1
    if p8 == "o":
        quantidade -=1
    if p9 == "o":
        quantidade -=1
    if quantidade > -2 and quantidade < 2:
        return True
    else: 
        return False


def verificaJogada(p1, p2, p3, p4, p5, p6, p7, p8, p9):
    """
    Recebe os valores das nove posições do tabuleiro e
    imprime se um jogador ('x' ou 'o') venceu a jogada. 
    (Cada variável representa uma posição no tabuleiro)
    """
    #Complete o código da função
    venceu = 0 
    if p1 == "x" and p2 == "x" and p3 == "x":
        venceu = "x"
    elif p1 == "o" and p2 == "o" and p3 == "o":
        venceu = "o"
    elif p4 == "x" and p5 == "x" and p6 == "x":
        venceu = "x"
    elif p4 == "o" and p5 == "o" and p6 == "o":
        venceu = "o"
    elif p7 == "x" and p8 == "x" and p9 == "x":
        venceu = "x"
    elif p7 == "o" and p8 == "o" and p9 == "o":
        venceu = "o"
    elif p1 == "x" and p4 == "x" and p7 == "x":
        venceu = "x"
    elif p1 == "o" and p4 == "o" and p7 == "o":
        venceu = "o"
    elif p2 == "x" and p5 == "x" and p8 == "x":
        venceu = "x"
    elif p2 == "o" and p5 == "o" and p8 == "o":
        venceu = "o"
    elif p3 == "x" and p6 == "x" and p9 == "x":
        venceu = "x"
    elif p3 == "o" and p6 == "o" and p9 == "o":
        venceu = "o"
    elif p1 == "x" and p5 == "x" and p9 == "x":
        venceu = "x"
    elif p1 == "o" and p5 == "o" and p9 == "o":
        venceu = "o"
    elif p3 == "x" and p5 == "x" and p7 == "x":
        venceu = "x"
    elif p3 == "o" and p5 == "o" and p7 == "o":
        venceu = "o"
    if venceu != "x" and venceu != "o":
        if p1 == " " or p2 == " " or p3 == " " or p4 == " " or p5 == " " or p6 == " " or p7 == " " or p8 == " " or p9 == " ":
          print("O jogo nao terminou!")
        else:
          print("Empate!")
    else:
      print(f"O jogador '{venceu}' venceu!")

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
