import pygame

import random

import time

import math


# ======================

# CONFIG

# ======================

ANCHO = 400

ALTO = 300


NEGRO = (0, 0, 0)

AZUL = (0, 200, 255)


pantalla = None


estado = "idle"

emocion = "neutral"


# animación suave

boca_actual = 40

boca_objetivo = 40


ojo_offset_x = 0

ojo_offset_y = 0

ojo_target_x = 0

ojo_target_y = 0


# parpadeo

ultimo_parpadeo = 0

duracion_parpadeo = 0.12

parpadeando = False



# ======================

# INIT

# ======================

def iniciar_cara():

    global pantalla, ultimo_parpadeo

    pygame.init()

    pantalla = pygame.display.set_mode((ANCHO, ALTO))

    pygame.display.set_caption("ATLAS")

    ultimo_parpadeo = time.time()



# ======================

# ESTADOS

# ======================

def actualizar_estado(nuevo_estado):

    global estado

    estado = nuevo_estado



def actualizar_emocion(nueva):

    global emocion

    emocion = nueva



# ======================

# OJOS

# ======================

def actualizar_ojos():

    global ojo_offset_x, ojo_offset_y, ojo_target_x, ojo_target_y


    # cambiar objetivo cada cierto tiempo

    if random.random() < 0.02:

        ojo_target_x = random.randint(-10, 10)

        ojo_target_y = random.randint(-5, 5)


    # interpolación suave

    ojo_offset_x += (ojo_target_x - ojo_offset_x) * 0.1

    ojo_offset_y += (ojo_target_y - ojo_offset_y) * 0.1



def dibujar_ojos():

    global parpadeando, ultimo_parpadeo


    ahora = time.time()


    # parpadeo

    if not parpadeando and ahora - ultimo_parpadeo > random.uniform(2, 5):

        parpadeando = True

        ultimo_parpadeo = ahora


    if parpadeando and ahora - ultimo_parpadeo > duracion_parpadeo:

        parpadeando = False

        ultimo_parpadeo = ahora


    x1 = int(130 + ojo_offset_x)

    y1 = int(130 + ojo_offset_y)


    x2 = int(270 + ojo_offset_x)

    y2 = int(130 + ojo_offset_y)


    if parpadeando:

        pygame.draw.rect(pantalla, AZUL, (x1 - 30, y1, 60, 8))

        pygame.draw.rect(pantalla, AZUL, (x2 - 30, y2, 60, 8))

    else:

        pygame.draw.circle(pantalla, AZUL, (x1, y1), 30)

        pygame.draw.circle(pantalla, AZUL, (x2, y2), 30)



# ======================

# BOCA

# ======================

def actualizar_boca():

    global boca_actual, boca_objetivo


    if estado == "hablando":

        boca_objetivo = random.randint(30, 80)

    elif estado == "escuchando":

        boca_objetivo = 10

    elif estado == "pensando":

        boca_objetivo = 25

    else:

        boca_objetivo = 40


    # interpolación suave

    boca_actual += (boca_objetivo - boca_actual) * 0.2



def dibujar_boca():

    ancho = int(boca_actual)


    y = 200


    if emocion == "feliz":

        pygame.draw.arc(pantalla, AZUL, (200 - ancho//2, y, ancho, 40), 0, math.pi, 3)


    elif emocion == "serio":

        pygame.draw.line(pantalla, AZUL, (200 - ancho//2, y+10), (200 + ancho//2, y+10), 3)


    elif emocion == "alerta":

        pygame.draw.rect(pantalla, AZUL, (200 - ancho//2, y, ancho, 25))


    else:

        pygame.draw.rect(pantalla, AZUL, (200 - ancho//2, y, ancho, 15))



# ======================

# LOOP

# ======================

def actualizar_pantalla():

    global pantalla


    for evento in pygame.event.get():

        if evento.type == pygame.QUIT:

            pygame.quit()

            exit()


    pantalla.fill(NEGRO)


    actualizar_ojos()

    actualizar_boca()


    dibujar_ojos()

    dibujar_boca()


    pygame.display.flip()
