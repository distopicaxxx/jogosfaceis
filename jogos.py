import forca
import adivinhacao


print("𝑬𝒔𝒄𝒐𝒍𝒉𝒂 𝒔𝒆𝒖 𝒋𝒐𝒈𝒐: \n")


print("(1) Forca (2) Adivinhação ")

jogo = int(input("Qual jogo você deseja jogar? "))

if(jogo == 1):
    print("Iniciando o Jogo da forca \n")
    forca.jogar()
elif(jogo  == 2):
    print("Iniciando o Jogo da Adivinhação \n")
    adivinhacao.jogar()