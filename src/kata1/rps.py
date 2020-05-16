from random import randint

options = ["Piedra", "Papel", "Tijeras"]



# El resultado de salida son las siguientes String
#'Empate!'
#'Ganaste!'
#'Perdiste!'
def quienGana(player, ai):
    
    if (player.lower() == "piedra" and ai.lower() == "piedra"):
        return "Empate!"
    elif (player.lower() == "piedra" and ai.lower() == "papel"):
        return "Perdiste!"
    elif (player.lower() == "piedra" and ai.lower() == "tijeras"):
        return "Ganaste!"
    elif (player.lower() == "papel" and ai.lower() == "piedra"):
        return "Ganaste!"
    elif (player.lower() == "papel" and ai.lower() == "papel"):
        return "Empate!"
    elif (player.lower() == "papel" and ai.lower() == "tijeras"):
        return "Perdiste!"
    elif (player.lower() == "tijeras" and ai.lower() == "piedra"):
        return "Perdiste!"
    elif (player.lower() == "tijeras" and ai.lower() == "papel"):
        return "Ganaste!"
    elif (player.lower() == "tijeras" and ai.lower() == "tijeras"):
        return "Empate!"

    

# Entry Point
def Game():
    
    index = randint(0,2)
    if (index == 0) :
        ai = options[0]
    elif (index == 1):
        ai = options[1]
    else:
        ai = options[2]
    
    player = input("¿Piedra, Papel o Tijeras?: ")
    

    winner = quienGana(player, ai)

    
    print(winner)

