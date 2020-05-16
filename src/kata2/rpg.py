#!/usr/bin/python

import random
import string

letras= "abcdefghijklmnñopqrstuvwxyzABCDEFGHIJKLMNÑOPQRSTUVWXYZ"
numeros= "1234567890"
simbolos= "ª!$%&/()=?¿+Ç|@#~€"
letras_y_simbolos="ª!$%&/()=?¿+Ç|@#~€abcdefghijklmnñopqrstuvwxyzABCDEFGHIJKLMNÑOPQRSTUVWXYZ"

def RandomPasswordGenerator(passLen):
    
    password = ""
    
    if (passLen % 3 == 0):
        for index in range(0,passLen,3) :
             password = password + random.choice(letras) + random.choice(numeros) + random.choice(simbolos)
    else:
        for index in range(0,passLen,2) :
            password = password + random.choice(letras_y_simbolos) + random.choice(numeros)

    return password
