import os  

carro = input("Escolha qual carro você quer\n1-BMW\n2-AUDI\n3-FIAT\n4-FERRARI\nR: ").upper()

if carro == "1" or carro == "BMW":
    gas = 9.8
    alc = 8.9 

elif carro == "2" or carro == "AUDI":
    gas = 12.8 
    alc = 8.9

elif carro == "3" or carro == "FIAT": 
    gas = 26.8
    alc = 24.9

else: 
    gas = 13.8 
    alc = 12.9

p = int(input("\nQuantas portas o carro tem: "))

if p > 3:
    gas - 0.5
    alc - 0.5

V = int (input("\nQuantos viajantes: "))

if V > 2:
    gas - 1.2
    alc - 1.2

b = input("\nTera bagageiro ?\n1-SIm\n2-Não\nR: ").lower()

if b == "1" or b == "sim":
    gas - 0.2
    alc - 0.2

if carro == "1" or carro == "BMW":
    print ("\n\nBMW\nGasolinha: "+ str(gas) +"L/KM\nÁlcool: "+ str(alc) +"L/KM\n\n")

elif carro == "2" or carro == "AUDI":
    print ("\n\nAUDI\nGasolinha: "+ str(gas) +"L/KM\nÁlcool: "+ str(alc) +"L/KM\n\n")

elif carro == "3" or carro == "FIAT": 
    print ("\n\nFIAT\nGasolinha: "+ str(gas) +"L/KM\nÁlcool: "+ str(alc) +"L/KM\n\n")

else:
    print ("\n\nFERRARI\nGasolinha: "+ str(gas) +"L/KM\nÁlcool: "+ str(alc) +"L/KM\n\n")

os.system("pause")