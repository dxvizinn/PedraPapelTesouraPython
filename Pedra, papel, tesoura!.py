import random

user_wins = 0
comp_wins = 0

options = ["pedra", "papel", "tesoura"]
options[0]

while True:
    user_input = input("Digite Pedra/Papel/Tesoura ou Q para sair: ").lower()
    if user_input == "q":
        break


    if user_input not in options:
        continue

    random_number = random.randint(0, 2)
    # Pedra: 0, papel: 1, tesoura: 2
    comp_pick = options[random_number]
    print("Bot escolheu", comp_pick + ".")

    if user_input == "pedra" and comp_pick == "tesoura":
        print("Você ganhou!")
        user_wins += 1
        continue

    if user_input == "pedra" and comp_pick == "papel":
        print("Você perdeu!")
        comp_wins += 1
        continue

    if user_input == "tesoura" and comp_pick == "pedra":
        print("Você perdeu!")
        comp_wins += 1
        continue

    if user_input == "papel" and comp_pick == "tesoura":
        print("Você perdeu!")
        comp_wins += 1
        continue

    elif  user_input == "papel" and comp_pick == "pedra":
        print("Você ganhou!")
        user_wins += 1
        continue

    elif user_input == "tesoura" and comp_pick == "papel":
        print("Você ganhou!")
        user_wins += 1
        continue

    elif user_input == "tesoura" and comp_pick == "tesoura":
        print("Empate!")
        user_wins += 0
        continue

    elif user_input == "papel" and comp_pick == "papel":
        print("Empate!")
        user_wins += 0
        continue

    elif user_input == "pedra" and comp_pick == "pedra":
        print("Empate!")
        user_wins += 0
        continue

    elif user_input == "papel" and comp_pick == "papel":
        print("Empate!")
        comp_wins += 0
        continue

    else:
        print("Você perdeu ):")
        comp_wins += 1
        
print("Você ganhou", user_wins, "vez(es)!")
print("O robô ganhou", comp_wins, "vez(es) ):") 
print("Tchau Tchau!")
