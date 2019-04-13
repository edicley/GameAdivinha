 import random

print("*************************************")
print("          JOGO DA ADIVINHAÇÃO        ")
print("*************************************")


tentativa = 1

valor = random.randint(1, 20)

print("Quer jogar em qual dificuldade?")
print("(1) Fácil (2) Médio (3) Difícil")

nivel = int(input("Defina o nível: "))

if(nivel == 1):
    chance = 5
elif(nivel == 2):
    chance = 3
else:
    chance = 2

print("Nível {} escolhido.".format(nivel))

    


print("Você tem", chance, "chances para acertar o número premiado.")

for tentativa in range(1, chance + 1):
#while(tentativa <= 5):
    
    print("Tentativa {} de {}".format(tentativa, chance)  )
    

    print("Digite um número de 1 à 20")
    chute = int(input("Chute um número: "))
     
    if (chute < 1 or chute > 20):
        print("ATENÇÃO! Você perdeu uma chance, escolha um número de 1 à 20!")
        continue
    
    if (chute == valor):
        print("Você acertou!")
        break
    else:
        if(chute > valor):
          print("Você errou! O número correto é menor que ", chute)
        elif(chute < valor):
            print("Você errou! O número correto é maior que ", chute)

tentativa = tentativa + 1
print("Meu número foi", valor)
print("Fim de Jogo")
