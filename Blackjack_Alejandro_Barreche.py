import random
import time

cartas = {chr(0x1f0a1): 11, 
    chr(0x1f0a2): 2, 
    chr(0x1f0a3): 3, 
    chr(0x1f0a4): 4, 
    chr(0x1f0a5): 5, 
    chr(0x1f0a6): 6, 
    chr(0x1f0a7): 7, 
    chr(0x1f0a8): 8, 
    chr(0x1f0a9): 9, 
    chr(0x1f0aa): 10, 
    chr(0x1f0ab): 10, 
    chr(0x1f0ad): 10, 
    chr(0x1f0ae): 10,
    }

def reglas_blackjack():
    print()
    print("El objetivo de cualquier mano de blackjack es derrotar a la banca. \nPara esto, debes tener una mano que puntúe más alto que la mano de la banca, \npero que no supere los 21 puntos en valor total. O bien, puedes ganar con una puntuación \ninferior a 22 cuando la mano de la banca supera los 21 puntos.")
    print()

def dar_carta():
    card = random.choice(list(cartas))
    return card 

lista_valores_jugador = []
lista_valores_crupier = []

def seguir_jugando():
    while True:
        pregunta = input("¿Quieres jugar otra mano? Sí (s) o no (n): ")
        try:
            pregunta = str(pregunta)
            if pregunta == "s" or pregunta == "n":
                break
            else:
                print("Esa letra no es válida")
        except:
            print("No has puesto una letra válida")
    return pregunta


def suma_total(list):
    j = 0
    for i in list:
        j += i 
    return j


def preguntar_segunda_carta():
    while True:
        pregunta = input("¿Quieres otra carta? Sí (s) o no (n): ")
        try:
            pregunta = str(pregunta)
            if pregunta == "s" or pregunta == "n":
                break
            else:
                print("Esa letra no es válida")
        except:
            print("No has puesto una letra válida")
    return pregunta

def continuar():
    while True:
        cont = input("Pulsa enter para continuar: ")
        try:
            cont = str(cont)
            if cont == "":
                break
            else:
                print("Pulsa enter para continuar: ")
        except:
            ("Pulsa enter para continuar: ")
       
def empezar():
    reglas_blackjack()
    print("Vamos a empezar a jugar")
    print()
    while True:
        cont = input("Pulsa enter para comenzar y recibir la primera carta: ")
        try:
            cont = str(cont)
            if cont == "":
                break
            else:
                print("Pulsa enter para comenzar y recibir la primera carta: ")
        except:
            ("Pulsa enter para comenzar: ")     
            
def jugador():
    print("Comienzas tú pidiendo cartas, es tu turno")
    print()
        
    carta = dar_carta()
    lista_valores_jugador.append(cartas[carta])
    print("{} : {}".format(carta, cartas[carta]))
    print()
            
    respuesta = preguntar_segunda_carta()
    print()
    if respuesta == "s":    
        carta_2 = dar_carta() 
        lista_valores_jugador.append(cartas[carta_2])
        valor_jugador = suma_total(lista_valores_jugador)
        print("{} : {} \n{} : {} \nSuma total: {}".format(carta, cartas[carta], carta_2, cartas[carta_2], valor_jugador))
        print()
    else:
        valor_jugador = suma_total(lista_valores_jugador)
        print("{} : {} \nSuma total: {}".format(carta, cartas[carta], valor_jugador))
        print()
        
    return valor_jugador

def crupier():
    print("Ahora es turno del crupier")
    print()
        
    carta_3 = dar_carta()
    lista_valores_crupier.append(cartas[carta_3])
    print("{} : {}".format(carta_3, cartas[carta_3]))
    print()
        
    continuar()
    print()
        
    carta_4 = dar_carta() 
    lista_valores_crupier.append(cartas[carta_4])
    valor_crupier = suma_total(lista_valores_crupier)
    print("{} : {} \n{} : {} \nSuma total: {}".format(carta_3, cartas[carta_3], carta_4, cartas[carta_4], valor_crupier))
    print()
    return valor_crupier
    
def quien_gana(x, y):    
    if x > y:
        print("Has ganado al crupier !!")
    elif x <= y: 
        if x == y:
            print("Los dos habeis ganado")
        else:
            print("Ha ganado la banca")
    print()

def jugar():
    
    global lista_valores_jugador
    global lista_valores_crupier
    
    empezar()
    print()
    
    while True:
        
        valor_jugador = jugador()        
        continuar()
        print()
        valor_crupier = crupier()     
        continuar()
        print()
        
        quien_gana(valor_jugador, valor_crupier)
        
        pregunta = seguir_jugando()
        print()
        if pregunta == "s":
            lista_valores_jugador = []
            lista_valores_crupier = []
            print()
            print("Barajeando las cartas, espere un momento ...")
            time.sleep(2)
            print()
            print("De acuerdo, continuemos")
            print()
            continue
        else:
            print("La partida ha acabado")
            input()
            break
            
            
           
jugar()

            
            
    

