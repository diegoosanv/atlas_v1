import pygame

import random

import threading

import time


pygame.init()


ANCHO = 400

ALTO = 300


pantalla = pygame.display.set_mode((ANCHO, ALTO))

pygame.display.set_caption("ATLAS")


NEGRO = (0, 0, 0)

AZUL = (0, 200, 255)


estado = "idle"

corriendo = True



def dibujar_ojos(parpadeo=False):

    if parpadeo:

        pygame.draw.rect(pantalla, AZUL, (100, 120, 60, 10))

        pygame.draw.rect(pantalla, AZUL, (240, 120, 60, 10))

    else:

        pygame.draw.circle(pantalla, AZUL, (130, 130), 30)

        pygame.draw.circle(pantalla, AZUL, (270, 130), 30)



def dibujar_boca():

    if estado == "hablando":

        ancho = random.randint(20, 80)

        pygame.draw.rect(pantalla, AZUL, (200 - ancho//2, 200, ancho, 20))

    elif estado == "escuchando":

        pygame.draw.circle(pantalla, AZUL, (200, 200), 10)

    elif estado == "pensando":

        pygame.draw.rect(pantalla, AZUL, (180, 200, 40, 10))

    else:

        pygame.draw.rect(pantalla, AZUL, (170, 200, 60, 5))



def loop():

    global corriendo


    ultimo_parpadeo = time.time()


    while corriendo:

        pantalla.fill(NEGRO)


        ahora = time.time()

        parpadeo = False


        if ahora - ultimo_parpadeo > random.uniform(2, 5):

            parpadeo = True

            if ahora - ultimo_parpadeo > 0.2:

                ultimo_parpadeo = ahora


        dibujar_ojos(parpadeo)

        dibujar_boca()


        pygame.display.flip()


        for evento in pygame.event.get():

            if evento.type == pygame.QUIT:

                corriendo = False


        pygame.time.delay(100)


    pygame.quit()




def iniciar_cara():

    hilo = threading.Thread(target=loop, daemon=True)

    hilo.start()



def actualizar_estado(nuevo_estado):

    global estado

    estado = nuevo_estado
