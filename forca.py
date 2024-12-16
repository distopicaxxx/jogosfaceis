def jogar():
    print("enforcado ​\n")
    print('Neste jogo você deve descobrir a palavra secreta antes de ser enforcado, boa sorte !\n')

#Palavra secreta é a palavra a qual deverá ser acertada pelo jogador
    palavra_secreta = "cu azul".upper()
    letras_acertadas = ["_" for letra in palavra_secreta]

    enforcou = False
    acertou = False
    erros = 0

    print(letras_acertadas)

    while(not enforcou and not acertou):

        chute = input("Qual letra? ")
        chute = chute.strip().upper()

        if(chute in palavra_secreta):
            index = 0
            for letra in palavra_secreta:
                if(chute == letra):
                   letras_acertadas[index] = letra
                index += 1
        else :
            print("A palavra não possui essa letra")
            erros += 1

        enforcou = erros == 10
        acertou = "_" not in letras_acertadas
        print(letras_acertadas)

    if(acertou):
        print("Voce ganhou !")
    else:
        print("Voce perdeu !")
    print("Fim do jogo")

if(__name__ == "__main__"):
    jogar()
