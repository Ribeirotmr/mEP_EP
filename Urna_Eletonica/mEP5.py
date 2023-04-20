#Nome:  Thierry Martins Ribeiro 
#Matrícula:  200221402





def nomeCandidatos(numeroCandidatos, l=[""]):
    if numeroCandidatos == 0:
        return l
    nome = input()
    l = l + [nome]
    return nomeCandidatos(numeroCandidatos - 1, l[:])
    

def votosCandidatos(quantidadeVotos, numeroCandidatos, l = None ):
    if quantidadeVotos == 0:
        return l
    if l == None:
        l = ([0]* numeroCandidatos) + [0,0]
    voto = int(input())
    if voto == 0:
        l[0] = l[0]+1
    elif voto > numeroCandidatos:
        l[-1] = l[-1]+1
    else:
        l[voto] = l[voto]+1
    return votosCandidatos(quantidadeVotos - 1, numeroCandidatos, l[:])
    

def menu(nomes, votos, i = 1):
    if i >= len(nomes):
        print(f"Brancos: {votos[0]}")
        print(f"Nulos: {votos[-1]}")
        return None
    print(f"{nomes[i]}: {votos[i]}")
    return menu(nomes, votos, i+1)

def candidatoVencedor(nomes, votos, i = 1, nomeMaior = "", votoMaior = 0):
    if i >= len(nomes):
        print(f"Vencedor(a): {nomeMaior}")
    else: 
        if votos[i] > votoMaior:
            return candidatoVencedor(nomes, votos, i+1, nomes[i], votos[i])
        return candidatoVencedor(nomes, votos, i+1, nomeMaior, votoMaior)







def main():
    numeroCandidatos = int(input())
    nomes = nomeCandidatos(numeroCandidatos)
    quantidadeVotos = int(input())
    votos = votosCandidatos(quantidadeVotos, numeroCandidatos)
    menu(nomes, votos)
    candidatoVencedor(nomes, votos)
main()