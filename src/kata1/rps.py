from random import randint

options = ["Piedra", "Papel", "Tijeras"]



# El resultado de salida son las siguientes String
#'Empate!'
#'Ganaste!'
#'Perdiste!'
def quienGana(player, ai):
    
    if (player == "Piedra" and ai == "Piedra"):
        return "Empate!"
    elif (player == "Piedra" and ai == "Papel"):
        return "Perdiste!"
    elif (player == "Piedra" and ai == "Tijeras"):
        return "Ganaste!"
    elif (player == "Papel" and ai == "Piedra"):
        return "Ganaste!"
    elif (player == "Papel" and ai == "Papel"):
        return "Empate!"
    elif (player == "Papel" and ai == "Tijeras"):
        return "Perdiste!"
    elif (player == "Tijeras" and ai == "Piedra"):
        return "Perdiste!"
    elif (player == "Tijeras" and ai == "Papel"):
        return "Ganaste!"
    elif (player == "Tijeras" and ai == "Tijeras"):
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


Game()