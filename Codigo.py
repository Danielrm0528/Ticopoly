import pygame
import time
from boton import Boton
import random
from pygame.locals import *
from propiedades import propiedad
from jugador import Player
from banco import Banco 

#Inicializa Pygame
pygame.init()
pygame.display.set_caption('Un viaje por Costa Rica')

#carga configuraciones
conf = []
with open('setup.txt','r') as file:
    for line in file:
        conf = line.strip().split(",")
        conf = [int(x) for x in conf]

#carga baraja de la suerte
baraja = []
with open('suerte.txt','r') as file:
    for line in file:
        carta = line.strip().split(",")
        carta[1] = int(carta[1])
        carta[2] = int(carta[2])
        baraja += [carta]
banco = Banco(conf[0],baraja)

#Tamaño de la pantalla y la tablero
pantallaLargo = 1510
pantallaAncho = 600
dimension_tablero = 7
pantalla = pygame.display.set_mode((pantallaLargo, pantallaAncho))

#Tamaño de cada celda en la tablero
dimension_casilla = (pantallaAncho // dimension_tablero)*1.52

#Colores
blanco = (255, 255, 255)
negro = (0, 0, 0)
celeste = (98, 180, 255)
amarillo = (255, 255, 0)
rojo = (255, 0, 0)
violeta = (38, 42, 86)
verde = (34, 139, 34)
cafe = (139, 69, 19)
azul = (0, 71, 171)
crema = (209, 190, 157)
naranja = (210,105,30)

#Colores del tablero 
parquePared = (31, 76, 77)
parqueCamino = (119, 171, 161)
playaPared = (86,158,230)
playaCamino = (144, 211, 238)
colorPared = playaPared
colorCamino = playaCamino

#Colores o piezas de los jugadores incial
jugadorAmarillo = (71,61,111)
jugadorVerde = verde
jugadorAzul = (30,144,255)
jugadorRojo = (114, 47, 55)

#Fuentes
fuente = pygame.font.Font("Fuentes/NexaHeavy.ttf", 20)
fuente2 = pygame.font.Font("Fuentes/NexaHeavy.ttf", 40)
fuenteJuego = pygame.font.Font("Fuentes/NexaHeavy.ttf", 38)

#Imagen de fondo del juego
playaGolfito = pygame.image.load("Imagenes/playaGolfito.png")
parqueIrazu = pygame.image.load("Imagenes/parqueIrazu.png")
gamSanJose = pygame.image.load("Imagenes/sanjose.png")
fondoImagen = playaGolfito

#Imágenes del tablero
playaGolfitoTablero = "Imagenes/playaGolfito.png"
parqueIrazuTablero = "Imagenes/parqueIrazu.png"
gamSanJoseTablero = "Imagenes/sanjose.png"
fondoTablero = playaGolfitoTablero

#Imágenes del dado
dice_images = [
    pygame.image.load("Imagenes/dados/1.png"),
    pygame.image.load("Imagenes/dados/2.png"),
    pygame.image.load("Imagenes/dados/3.png"),
    pygame.image.load("Imagenes/dados/4.png"),
    pygame.image.load("Imagenes/dados/5.png"),
    pygame.image.load("Imagenes/dados/6.png")
]
#Valor inicial del dado
dice_value = 1
#Posición y tamaño del dado en la pantalla
dice_rect = pygame.Rect(pantallaLargo - 500, 580, 50, 50)
dice_rect_Inicio = pygame.Rect(pantallaLargo - 970, 300, 50, 50)
#Variable para el movimiento de agitación del dado
shake_offset = 0
shake_direction = 1
shake_amplitude = 10
shake_frames = 30
#Variable para controlar si se está lanzando el dado
rolling = False
#Variable para almacenar la imagen del último dado lanzado
last_dice_image = pygame.transform.scale(pygame.image.load("Imagenes/dados/1.png"), (dice_rect.width, dice_rect.height))
# Variable para almacenar la imagen del último dado lanzado
last_dice_index = 0
# Variable para controlar la visualización del último resultado del dado
show_last_dice = False
show_last_dice_frames = 120  # Número de frames para mostrar el último resultado del dado
numeroJugadores=2
propiedadesAmbiente='Ambientes/propiedades_playa.txt'

# Definir la tablero
tablero = [
    [7, 8, 9, 10, 11, 12, 13],
    [6, 0, 0, 0, 0, 0, 14],
    [5, 0, 0, 0, 0, 0, 15],
    [4, 0, 0, 0, 0, 0, 16],
    [3, 0, 0, 0, 0, 0, 17],
    [2, 0, 0, 0, 0, 0, 18],
    [1, 24, 23, 22, 21, 20, 19]
]

#Color de botones y el tablero del juego
colorBotones = azul

#Imagenes de los ambientes
playa = playaGolfito
anchoImagenAmbiente = 198
largoImagenAmbiente = 140

#Botón de interfaz de configuración
botonImagenParques = Boton(130, 210, anchoImagenAmbiente, largoImagenAmbiente, azul)
botonImagenPlaya = Boton(390, 210, anchoImagenAmbiente, largoImagenAmbiente, azul)
botonImagenGam = Boton(650, 210, anchoImagenAmbiente, largoImagenAmbiente, azul)

# Botones de interfaz
botonEntrar = Boton(370, 350, 100, 50, colorBotones)
botonConfiguracion = Boton(477, 350, 150, 50, colorBotones)
botonSalir = Boton(635, 350, 100, 50, colorBotones)
botonRegresar = Boton(800, 500, 125, 50, colorBotones)
botonRegresarConfiguracion = Boton((pantallaLargo / 2 - (pantallaLargo/1.2) / 2 + 700),(pantallaAncho / 2 - (pantallaAncho/1.2) / 2 + 435), 125, 50, colorBotones)
botonCargar = Boton(500, 250, 125, 50, colorBotones)
botonGenerar = Boton(500, 325, 125, 50, colorBotones)
botonAventura = Boton(500, 400, 125, 50, colorBotones)
botonCompetitivo = Boton(500, 475, 125, 50, colorBotones)
botonOk = Boton(485,450,120,50, colorBotones)
botonJugar = Boton(385,450,120,50, colorBotones)
botonResolver = Boton(585,450,120,50, colorBotones)
botonTerminarPartida = Boton(pantalla.get_width()-220, pantallaAncho // 2+500, 180, 50, colorBotones)
boton2jugadores = Boton(pantallaLargo // 2 - 350, pantallaAncho // 2-30, 90, 50, colorBotones)
boton3jugadores = Boton(pantallaLargo // 2 - 250, pantallaAncho // 2-30, 90, 50, colorBotones)
boton4jugadores = Boton(pantallaLargo // 2 - 150, pantallaAncho // 2-30, 90, 50, colorBotones)
botonRegresarEstablecerJugadores = Boton(pantallaLargo // 2 - 270, pantallaAncho // 2+30, 125, 50, colorBotones)
botonContinuarEstablecerJugadores = Boton(pantallaLargo // 2, pantallaAncho // 2+30, 125, 50, colorBotones)

#cambia colores de los botones
def cambiarColorBotones(nuevoColor):
    global colorBotones
    colorBotones = nuevoColor
    botonEntrar.color = nuevoColor
    botonConfiguracion.color = nuevoColor
    botonSalir.color = nuevoColor
    botonRegresar.color = nuevoColor
    botonRegresarConfiguracion.color = nuevoColor
    botonTerminarPartida.color = nuevoColor
    botonRegresarEstablecerJugadores.color = nuevoColor
    botonContinuarEstablecerJugadores.color = nuevoColor
    botonCargar.color = nuevoColor
    botonGenerar.color = nuevoColor
    botonAventura.color = nuevoColor
    botonCompetitivo.color = nuevoColor
    botonOk.color = nuevoColor
    botonJugar.color = nuevoColor
    botonResolver.color = nuevoColor
    boton2jugadores.color = nuevoColor
    boton3jugadores.color = nuevoColor
    boton4jugadores.color = nuevoColor

#Título, sombra e imagen del juego
texto = fuente.render("Un viaje por Costa Rica", True, blanco)
textoSombra = fuente.render("Un viaje por Costa Rica", True, negro)
imagenInicio = pygame.image.load("Imagenes/logoInicio.png")
imagenInicioLargo = 500
imagenInicioAncho = 70

#Reloj de pygame e imagen, ambos para gif forzado de inicio
reloj = pygame.time.Clock()
imagenesRichUncle = ["Imagenes/RichUncle1.png", "Imagenes/RichUncle2.png"]

#Tamaño de las celdas
tamanoCelda = 20

#Funcion de configuracion de ambientes
def configuracion():
    pantallaLargo = 1100
    pantallaAncho = 600

    global fondoImagen, colorPared, colorCamino, pacmanColor,Jug2Color,mataColor,congelaColor,propiedadesAmbiente,fondoTablero
    corriendo = True
    while corriendo:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                corriendo = False

        fondoPantalla = pygame.transform.scale(fondoImagen, (pantallaLargo, pantallaAncho))
        pantalla.blit(fondoPantalla, (0, 0))

        #Textos
        textoinstrucciones = fuente.render("Selección de tema:", True, negro)
        textoIntro = fuente.render("Le damos la bienvenida a la configuración de Un viaje por Costa Rica", True, negro)
        textoEscojaAmbiente = fuente.render("Haga click en la imagen del tema que desea para el juego:", True, negro)
        textoAmbienteTropical = fuente.render("Parques nacionales", True, negro)
        textoAmbienteCongelado = fuente.render("Playas", True, negro)
        textoAmbienteGam = fuente.render("GAM", True, negro)
        textoCerrar = fuente.render("Si desea cerrar el programa, presione regresar y luego salir.", True, negro) 

        rectanguloX = pantallaLargo / 2 - (pantallaLargo/1.2) / 2
        rectanguloY = pantallaAncho / 2 - (pantallaAncho/1.2) / 2
        pygame.draw.rect(pantalla, crema, (rectanguloX, rectanguloY, (pantallaLargo/1.2), (pantallaAncho/1.2)))
        pygame.draw.rect(pantalla, (100, 81, 59), (rectanguloX, rectanguloY, (pantallaLargo/1.2), (pantallaAncho/1.2)), 2)

        #Símbolo de pregunta en pantalla principal
        pantalla.blit(textoinstrucciones, ((pantalla.get_width() // 9)+3, (pantalla.get_height() // 10)+4))
        pantalla.blit(textoIntro, ((pantalla.get_width() // 9)+4, (pantalla.get_height() // 10)+50))
        pantalla.blit(textoEscojaAmbiente, ((pantalla.get_width() // 9)+4, (pantalla.get_height() // 10)+100))
        pantalla.blit(textoAmbienteTropical, ((pantalla.get_width() // 9)+10, (pantalla.get_height() // 10)+300))
        pantalla.blit(textoAmbienteCongelado, ((pantalla.get_width() // 9)+330, (pantalla.get_height() // 10)+300))
        pantalla.blit(textoAmbienteGam, ((pantalla.get_width() // 9)+600, (pantalla.get_height() // 10)+300))
        pantalla.blit(textoCerrar, ((pantalla.get_width() // 9)+4, (pantalla.get_height() // 10)+345))

        if botonRegresarConfiguracion.imprimirBotonInteractivo(negro):
            inicio()
        botonRegresarConfiguracion.textoEnBoton(fuente,'Regresar',blanco)

        #Cambiar temas
        if botonImagenPlaya.imprimirBotonInteractivo(negro):
            cambiarColorBotones(azul)
            fondoImagen = playaGolfito
            colorPared = playaPared
            colorCamino = playaCamino
            pacmanColor = (71,61,111)
            Jug2Color = (118,132,220)
            congelaColor = (30,144,255)
            mataColor = (114, 47, 55)
            fondoTablero = playaGolfitoTablero
            change_data("Ambientes/playa.txt")
            propiedadesAmbiente='Ambientes/propiedades_playa.txt'
        botonImagenPlaya.textoEnBoton(fuente, 'Congelado', blanco)

        if botonImagenParques.imprimirBotonInteractivo(negro):
            cambiarColorBotones(verde)
            fondoImagen = parqueIrazu
            colorPared = parquePared
            colorCamino = parqueCamino
            pacmanColor = (154,72,122)
            Jug2Color = (110,114,72)
            congelaColor = (0,76,125)
            mataColor = (255,87,51)
            fondoTablero = parqueIrazuTablero
            change_data("Ambientes/parque.txt")
            propiedadesAmbiente='Ambientes/propiedades_parque.txt'
        botonImagenParques.textoEnBoton(fuente, 'Tropical', blanco)

        if botonImagenGam.imprimirBotonInteractivo(negro):
            cambiarColorBotones(naranja)
            fondoImagen = gamSanJose
            colorPared = azul
            fondoTablero = gamSanJoseTablero
            change_data("Ambientes/gam.txt")
            propiedadesAmbiente='Ambientes/propiedades_gam.txt'
        botonImagenGam.textoEnBoton(fuente, 'Tropical', blanco)

        #Imagen del botón para cambiar el ambiente a Congelado
        playaGolfitoEscalada = pygame.transform.scale(playaGolfito, (botonImagenPlaya.ancho, botonImagenPlaya.largo))
        posicionplayaGolfito = playaGolfitoEscalada.get_rect(center=botonImagenPlaya.rect.center)
        pantalla.blit(playaGolfitoEscalada, posicionplayaGolfito)

        #Imagen del botón para cambiar el ambiente a Tropical
        parqueIrazuEscalada = pygame.transform.scale(parqueIrazu, (botonImagenParques.ancho, botonImagenParques.largo))
        posicionparqueIrazu = parqueIrazuEscalada.get_rect(center=botonImagenParques.rect.center)
        pantalla.blit(parqueIrazuEscalada, posicionparqueIrazu)

        #Imagen del botón para cambiar el ambiente a Tropical
        gamSanJoseEscalada = pygame.transform.scale(gamSanJose, (botonImagenGam.ancho, botonImagenGam.largo))
        posiciongamSanJose = gamSanJoseEscalada.get_rect(center=botonImagenGam.rect.center)
        pantalla.blit(gamSanJoseEscalada, posiciongamSanJose)

        pygame.display.update()

    pygame.quit()

# Función para dibujar los botones
def dibujar_botones_inicio():
    if botonSalir.imprimirBotonInteractivo(negro):
        pygame.quit()
    botonSalir.textoEnBoton(fuente, 'Salir', blanco)

    if botonEntrar.imprimirBotonInteractivo(negro):
        juego()
    botonEntrar.textoEnBoton(fuente, 'Entrar', blanco)

    if botonConfiguracion.imprimirBotonInteractivo(negro):
        configuracion()
    botonConfiguracion.textoEnBoton(fuente, 'Configuración', blanco)

#Cargar nombres y ubicaciones de imágenes desde un archivo de texto
def load_data(filename):
    data = []
    with open(filename, "r") as file:
        next(file)  #Saltar la primera línea del encabezado
        for line in file:
            position, name, image_path= line.strip().split(",")
            position = int(position)
            data.append((position, name, image_path))
    return data

def change_data(filename):
    global data, cells_with_data
    data = load_data(filename)
    cells_with_data = []
    for row in range(dimension_tablero):
        for col in range(dimension_tablero):
            number = tablero[row][col]
            if number != 0:
                cell_data = next((data_item for data_item in data if data_item[0] == number), None)
                if cell_data:
                    position, name, image_path = cell_data
                    image = pygame.image.load(image_path)
                    scaled_image = pygame.transform.scale(image, (dimension_casilla, dimension_casilla))
                    cells_with_data.append(((col, row), name, scaled_image))

data = load_data("Ambientes/playa.txt")

#Crear una lista de celdas con nombres y ubicaciones de imágenes
cells_with_data = []
for row in range(dimension_tablero):
    for col in range(dimension_tablero):
        number = tablero[row][col]
        if number != 0:
            cell_data = next((data_item for data_item in data if data_item[0] == number), None)
            if cell_data:
                position, name, image_path = cell_data
                image = pygame.image.load(image_path)
                scaled_image = pygame.transform.scale(image, (dimension_casilla, dimension_casilla))
                cells_with_data.append(((col, row), name, scaled_image))

#Jugadores
jugadores = []
def crear_jugadores(num_jugadores):
    colors = [jugadorAmarillo,jugadorAzul,jugadorVerde,jugadorRojo]
    for i in range(num_jugadores):
        jugadores.append(Player('Jugador '+str(i+1),1,colors[i],dimension_casilla))

#Propiedades
propiedades = []
def crearPropiedades(propTxt):
    with open(propTxt,'r') as file:
        for line in file:
            atributos = line.strip().split(',')
            propiedades.append(propiedad(atributos[1],int(atributos[0]),int(atributos[2]),int(atributos[3])))

#Obtener coordenadas extremas de los ceros
min_col = dimension_tablero
min_row = dimension_tablero
max_col = 0
max_row = 0
for row in range(dimension_tablero):
    for col in range(dimension_tablero):
        if tablero[row][col] == 0:
            min_col = min(min_col, col)
            min_row = min(min_row, row)
            max_col = max(max_col, col)
            max_row = max(max_row, row)

#funcion que muestra el ganador de una partida 
def mostrarGanador():
    pantallaLargo = 1100
    pantallaAncho = 600
    pantalla = pygame.display.set_mode((pantallaLargo, pantallaAncho))
    fondoPantalla = pygame.transform.scale(fondoImagen, (pantallaLargo, pantallaAncho))
    pantalla.blit(fondoPantalla, (0, 0))
    texto = fuente2.render(f'¡El ganador es: {banco.determinaGanador(jugadores).nombre}, felicidades!',True,negro)
    textorect = texto.get_rect(center=(pantallaLargo //2, pantallaAncho //2))
    pantalla.blit(texto,textorect)
    botonSalir = Boton(500, 370, 100, 50, colorBotones)
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        if botonSalir.imprimirBotonInteractivo(negro):
            pygame.quit()
        botonSalir.textoEnBoton(fuente,'Salir',blanco)    
        pygame.display.update()

#dibuja el tablero del juego 
def dibujar_tablero():
    #Cargar la imagen
    image = pygame.image.load(fondoTablero)

    #Ajustar la imagen al tamaño de la celda de la tablero
    scaled_image = pygame.transform.scale(image, ((max_col - min_col + 1) * dimension_casilla, (max_row - min_row + 1) * dimension_casilla))

    #Crear una celda para representar la fotografía
    photo_cell = ((min_col, min_row), scaled_image)
    for cell, name, image in cells_with_data:
        col, row = cell
        x = col * dimension_casilla
        y = row * dimension_casilla

        pygame.draw.rect(pantalla, blanco, (x, y, dimension_casilla, dimension_casilla))

        # Dibujar imagen en la celda
        image_rect = image.get_rect(center=(x + dimension_casilla // 2, y + dimension_casilla // 2))
        pantalla.blit(image, image_rect)

        # Dibujar contorno negro alrededor de la celda
        pygame.draw.rect(pantalla, negro, (x, y, dimension_casilla, dimension_casilla), 1)

        font = pygame.font.Font("Fuentes/NexaHeavy.ttf", 20)

        # Ajustar texto a la celda
        lines = []
        words = name.split()
        current_line = ""
        for word in words:
            test_line = current_line + word + " "
            if font.size(test_line)[0] < dimension_casilla:
                current_line = test_line
            else:
                lines.append(current_line)
                current_line = word + " "
        lines.append(current_line)
    
    # Dibujar la fotografía
    col, row = photo_cell[0]
    x = col * dimension_casilla
    y = row * dimension_casilla
    pantalla.blit(photo_cell[1], (x, y))

    # Dibujar jugadores
    for player in jugadores:
        col, row = get_position_coordinates(player.posicion)
        player.rect.center = (col * dimension_casilla + dimension_casilla // 2, row * dimension_casilla + dimension_casilla // 2)
        pygame.draw.ellipse(pantalla, player.color, player.rect)

    if botonTerminarPartida.imprimirBotonInteractivo(negro):
        #Agregar mostrar resultados
        mostrarGanador()
    botonTerminarPartida.textoEnBoton(fuente,'Terminar partida',blanco)

    imagenInicioEscalada = pygame.transform.scale(imagenInicio, (imagenInicioLargo, imagenInicioAncho))
    imagenInicioRectEscalada = imagenInicioEscalada.get_rect()
    imagenInicioRectEscalada.center = ((pantalla.get_width() // 2) + 400, (pantalla.get_height() // 2) -370)
    pantalla.blit(imagenInicioEscalada, imagenInicioRectEscalada)

    #Mostrar texto
    text = fuenteJuego.render("Un viaje por Costa Rica", True, (255, 255, 255))
    text_rect = text.get_rect(center=((pantallaLargo // 2)+400, pantallaAncho - 520))
    pantalla.blit(text, text_rect)

def get_position_coordinates(position):
    for row in range(dimension_tablero):
        for col in range(dimension_tablero):
            if tablero[row][col] == position:
                return col, row

def get_input(): #no debo hacer nada
    global fondoImagen, numeroJugadores

    pantallaLargo = 1100
    pantallaAncho = 600
    pantalla = pygame.display.set_mode((pantallaLargo, pantallaAncho))

    font = pygame.font.Font("Fuentes/NexaHeavy.ttf", 20)
    text = font.render("Ingrese la cantidad de jugadores:", True, (0, 0, 0))
    text_rect = text.get_rect(center=(pantallaLargo // 2, pantallaAncho // 2 - 50))
    corriendo=True

    while corriendo:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    corriendo = False

            fondoPantalla = pygame.transform.scale(fondoImagen, (pantallaLargo, pantallaAncho))
            pantalla.blit(fondoPantalla, (0, 0))
            pantalla.blit(text, text_rect)

            if boton2jugadores.imprimirBotonInteractivo(negro):
                numeroJugadores=2
                return 2
            boton2jugadores.textoEnBoton(fuente, '2', blanco)

            if boton3jugadores.imprimirBotonInteractivo(negro):
                numeroJugadores=3
                return 3
            boton3jugadores.textoEnBoton(fuente, '3', blanco)

            if boton4jugadores.imprimirBotonInteractivo(negro):
                numeroJugadores=4
                return 4
            boton4jugadores.textoEnBoton(fuente, '4', blanco)

            if botonRegresarEstablecerJugadores.imprimirBotonInteractivo(negro):
                inicio()
            botonRegresarEstablecerJugadores.textoEnBoton(fuente,'Regresar',blanco)

            pygame.display.update()
    pygame.quit()

#obtiene los nombres de los jugadores
def get_player_names(num_players):
    player_names = []
    for i in range(num_players):
        name = get_player_name(i + 1)
        player_names.append(name)
    return player_names

#pantalla de obtener nombre de juggadores
def get_player_name(player_number):
    global fondoImagen

    pantallaLargo = 1100
    pantallaAncho = 600
    pantalla = pygame.display.set_mode((pantallaLargo, pantallaAncho))
    
    input_value = ""
    while True:
        fondoPantalla = pygame.transform.scale(fondoImagen, (pantallaLargo, pantallaAncho))
        pantalla.blit(fondoPantalla, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return input_value
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    return input_value
                elif event.key == pygame.K_BACKSPACE:
                    input_value = input_value[:-1]
                elif event.unicode.isalpha() or event.unicode.isspace():
                    input_value += event.unicode

        font = pygame.font.Font("Fuentes/NexaHeavy.ttf", 36)
        text = font.render(f"Ingrese el nombre del jugador {player_number}:", True, negro)
        text_rect = text.get_rect(center=(pantallaLargo // 2, pantallaAncho // 2 - 50))
        pantalla.blit(text, text_rect)
        pygame.draw.rect(pantalla, blanco, (pantallaLargo // 2 - 100, pantallaAncho // 2, 200, 50), 2)
        input_text = font.render(input_value, True, negro)
        input_text_rect = input_text.get_rect(center=(pantallaLargo // 2, pantallaAncho // 2 + 25))
        pantalla.blit(input_text, input_text_rect)
        pygame.display.flip()

#tira los dados
def roll_dice_inicio():
    global dice_value, shake_offset, shake_direction, rolling, last_dice_index, fondoImagen

    pantallaLargo = 1100
    pantallaAncho = 600
    pantalla = pygame.display.set_mode((pantallaLargo, pantallaAncho))

    rolling = True
    dice_value = None
    shake_offset = 0
    shake_direction = 1

    # Cambiar las imágenes de forma aleatoria durante un tiempo
    frames = 10  # Número de frames en la animación
    delay = 40  # Tiempo de espera entre frames en milisegundos
    dice_image = None

    for frame in range(frames):
        # Calcular la posición de agitación
        shake_offset += shake_direction * shake_amplitude
        if abs(shake_offset) >= shake_amplitude:
            shake_direction *= -1

        # Mostrar una imagen aleatoria del dado con agitación
        random_index = random.randint(0, 5)
        dice_image = dice_images[random_index]
        x = dice_rect_Inicio.x + shake_offset
        y = dice_rect_Inicio.y + shake_offset
        scaled_dice_image = pygame.transform.scale(dice_image, (dice_rect_Inicio.width, dice_rect_Inicio.height))

        fondoPantalla = pygame.transform.scale(fondoImagen, (pantallaLargo, pantallaAncho))
        pantalla.blit(fondoPantalla, (0, 0))

        pantalla.blit(scaled_dice_image, (x, y))
        pygame.display.flip()
        pygame.time.delay(delay)

    # Mostrar la imagen final del dado
    x = dice_rect_Inicio.x
    y = dice_rect_Inicio.y
    scaled_dice_image = pygame.transform.scale(dice_image, (dice_rect_Inicio.width, dice_rect_Inicio.height))
    fondoPantalla = pygame.transform.scale(fondoImagen, (pantallaLargo, pantallaAncho))
    pantalla.blit(fondoPantalla, (0, 0))
    pantalla.blit(scaled_dice_image, (x, y))
    pygame.display.flip()
    dice_value = random_index + 1
    last_dice_index = random_index  # Almacenar el índice del último dado lanzado
    rolling = False

    return dice_value

#dice el orden de los jugadores
def draw_player_order(player_names):
    global fondoImagen, numeroJugadores
    pantallaLargo = 1100
    pantallaAncho = 600
    pantalla = pygame.display.set_mode((pantallaLargo, pantallaAncho))

    fondoPantalla = pygame.transform.scale(fondoImagen, (pantallaLargo, pantallaAncho))
    pantalla.blit(fondoPantalla, (0, 0))

    font = pygame.font.Font("Fuentes/NexaHeavy.ttf", 36)
    text = font.render("Orden de juego:", True, negro)
    text_rect = text.get_rect(center=(pantallaLargo // 2, pantallaAncho // 2 - 100))
    pantalla.blit(text, text_rect)
    y = pantallaAncho // 2 - 50
    for i, name in enumerate(player_names):
        text = font.render(f"Jugador {i + 1}: {name}", True, negro)
        text_rect = text.get_rect(center=(pantallaLargo // 2, y))
        pantalla.blit(text, text_rect)
        y += 50
    if botonContinuarEstablecerJugadores.imprimirBotonInteractivo(negro):
        return numeroJugadores
    botonContinuarEstablecerJugadores.textoEnBoton(fuente,'Continuar',blanco)
    pygame.display.flip()

# Mostrar orden de juego
player_order = []

#pantalla de cantidad de jugadores
def cantidadJugadores():
    global dice_value, numeroJugadores, fondoImagen,player_order

    pantallaLargo = 1100
    pantallaAncho = 600
    pantalla = pygame.display.set_mode((pantallaLargo, pantallaAncho))

    # Mostrar pantalla previa para ingresar la cantidad de jugadores
    num_players = get_input()

    # Obtener nombres de jugadores
    player_names = get_player_names(num_players)

    # Mostrar el dado inicial antes de comenzar el juego
    fondoPantalla = pygame.transform.scale(fondoImagen, (pantallaLargo, pantallaAncho))
    pantalla.blit(fondoPantalla, (0, 0))
    initial_dice_image = pygame.transform.scale(dice_images[dice_value - 1], (dice_rect_Inicio.width, dice_rect_Inicio.height))
    pantalla.blit(initial_dice_image, (dice_rect_Inicio.x, dice_rect_Inicio.y))
    pygame.display.flip()

    while len(player_order) < len(player_names):
        name = player_names[len(player_order)]
        fondoPantalla = pygame.transform.scale(fondoImagen, (pantallaLargo, pantallaAncho))
        pantalla.blit(fondoPantalla, (0, 0))
        font = pygame.font.Font("Fuentes/NexaHeavy.ttf", 26)
        text = font.render(f"{name}, es su turno. Lance el dado para definir el orden.", True, negro)
        text_rect = text.get_rect(center=(pantallaLargo // 2, pantallaAncho // 2 - 50))
        pantalla.blit(text, text_rect)

        # Mostrar el dado actual
        dice_image = pygame.transform.scale(dice_images[dice_value - 1], (dice_rect_Inicio.width, dice_rect_Inicio.height))
        pantalla.blit(dice_image, (dice_rect_Inicio.x, dice_rect_Inicio.y))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONDOWN and not rolling:
                mouse_pos = pygame.mouse.get_pos()
                if dice_rect_Inicio.collidepoint(mouse_pos):
                    dice_value = roll_dice_inicio()
                    player_order.append((name, dice_value))

    player_order.sort(key=lambda x: x[1], reverse=True)  # Ordenar por valor del dado en orden descendente

    # Mostrar el último resultado del dado por unos segundos
    show_last_dice = True
    show_last_dice_frames_counter = show_last_dice_frames

    while show_last_dice:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                show_last_dice = False
                break

        if not show_last_dice:
            break

        fondoPantalla = pygame.transform.scale(fondoImagen, (pantallaLargo, pantallaAncho))
        pantalla.blit(fondoPantalla, (0, 0))
        last_dice_image = pygame.transform.scale(dice_images[last_dice_index], (dice_rect_Inicio.width, dice_rect_Inicio.height))
        
        pantalla.blit(last_dice_image, (dice_rect_Inicio.x, dice_rect_Inicio.y))
        pygame.display.flip()
        show_last_dice_frames_counter -= 1

        if show_last_dice_frames_counter <= 0:
            show_last_dice = False
    
    # Mostrar orden de juego final antes de cerrar la ventana
    draw_player_order([name for name, _ in player_order])
    
    # Mantener la ventana abierta hasta que se cierre manualmente
    running = True
    while running:
        if botonContinuarEstablecerJugadores.imprimirBotonInteractivo(negro):
            return numeroJugadores
        botonContinuarEstablecerJugadores.textoEnBoton(fuente,'Continuar',blanco)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
    pygame.quit()

# Función para lanzar el dado
def roll_dice(): #no debo hacer nada
    global dice_value, shake_offset, shake_direction, rolling, last_dice_image, colorPared
    rolling = True
    dice_value = None
    shake_offset = 0
    shake_direction = 1

    # Cambiar las imágenes de forma aleatoria durante un tiempo
    frames = 10  # Número de frames en la animación
    delay = 40  # Tiempo de espera entre frames en milisegundos
    dice_image = None

    for frame in range(frames):

        # Calcular la posición de agitación
        shake_offset += shake_direction * shake_amplitude
        if abs(shake_offset) >= shake_amplitude:
            shake_direction *= -1

        # Mostrar una imagen aleatoria del dado con agitación
        random_index = random.randint(0, 5)
        dice_image = dice_images[random_index]
        x = dice_rect.x + shake_offset
        y = dice_rect.y + shake_offset
        scaled_dice_image = pygame.transform.scale(dice_image, (dice_rect.width, dice_rect.height))
        pantalla.fill(colorPared)  # Limpiar la pantalla en cada frame
        dibujar_tablero()  # Dibujar la tablero en cada frame
        pantalla.blit(scaled_dice_image, (x, y))

        pygame.display.flip()
        pygame.time.delay(delay)

    # Mostrar la imagen final del dado
    x = dice_rect.x
    y = dice_rect.y
    scaled_dice_image = pygame.transform.scale(dice_image, (dice_rect.width, dice_rect.height))
    pantalla.fill(colorPared)  # Limpiar la pantalla antes de mostrar el dado final
    dibujar_tablero()  # Dibujar la tablero antes de mostrar el dado final
    dineroJugadores()
    granAcumulado()
    pantalla.blit(scaled_dice_image, (x, y))
    pygame.display.flip()
    dice_value = random_index + 1
    last_dice_image = scaled_dice_image  # Almacenar la imagen del último dado lanzado
    rolling = False

    return dice_value

#dibuja el dinero de cada jugador y el turno en la pantalla
def dineroJugadores():
    font = pygame.font.Font("Fuentes/NexaHeavy.ttf", 25)
    inicio = 100
    for jugador in jugadores:
        texto = font.render(jugador.nombre + ': ' + str(jugador.acumulado),True,blanco)
        inicio += 50
        pantalla.blit(texto,(930,inicio)) #Establece eje X de dinero de cada jugador
    text = font.render(f"Turno de: {jugadores[current_player_index].nombre}", True, (255, 255, 255))
    text_rect = text.get_rect(center=((pantallaLargo // 2)+300, pantallaAncho - 50))
    pantalla.blit(text, text_rect) 
        
#Función para comprar propiedad
def comprarPropiedad(jugador, propiedad):
    pantalla.fill(colorPared)
    dibujar_tablero()
    dineroJugadores()
    granAcumulado()
    if last_dice_image:
        x = dice_rect.x
        y = dice_rect.y
        pantalla.blit(last_dice_image, (x, y))
    botonSi = Boton(360, 270, 50, 50, colorBotones)
    botonNo = Boton(420, 270, 50, 50, colorBotones)
    font = pygame.font.Font("Fuentes/NexaHeavy.ttf", 20)
    texto = font.render("¿Desea comprar " + str(propiedad.desc) + '?', True, negro)
    texto2 = font.render(f"Valor: {propiedad.valor}", True, negro)
    texto2Rect = texto2.get_rect(center=(350, 240))

    fondo_tarjeta_rect = pygame.Rect(290, 190, 360, 150)
    pygame.draw.rect(pantalla, crema, fondo_tarjeta_rect)
    contorno_tarjeta_rect = pygame.Rect(290, 190, 360, 150)
    pygame.draw.rect(pantalla, (255, 255, 255), contorno_tarjeta_rect, 2)

    pantalla.blit(texto, (300, 200))
    pantalla.blit(texto2, texto2Rect)

    corriendo = True
    while corriendo:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
        if botonSi.imprimirBotonInteractivo(negro):
            jugador.realizaCompra(propiedad,banco) #compra un propiedad (el dinero se va al banco)
            return
        botonSi.textoEnBoton(font,'Sí',blanco)
        if botonNo.imprimirBotonInteractivo(negro):
            return 
        botonNo.textoEnBoton(font,'No',blanco)
        pygame.display.update()

#dibuja el gran acumulado
def granAcumulado():
    font = pygame.font.Font("Fuentes/NexaHeavy.ttf", 25)
    texto1 = font.render('Gran acumulado:',True,blanco)
    texto2 = font.render(str(banco.granAcum),True,blanco)
    texto2rect = texto2.get_rect(center=(1050,450))
    pantalla.blit(texto1,(932,400))
    pantalla.blit(texto2,texto2rect)
    
#texto de accion
def accion(string):
    pantalla.fill(colorPared)
    dibujar_tablero()
    dineroJugadores()
    granAcumulado()
    if last_dice_image:
            x = dice_rect.x
            y = dice_rect.y
            pantalla.blit(last_dice_image, (x, y))

    fondo_tarjeta_rect = pygame.Rect(290, 190, 360, 150)
    pygame.draw.rect(pantalla, crema, fondo_tarjeta_rect)
    contorno_tarjeta_rect = pygame.Rect(290, 190, 360, 150)
    pygame.draw.rect(pantalla, (255, 255, 255), contorno_tarjeta_rect, 2)

    botonContinuar = Boton(420,270,100,50,colorBotones)
    texto = fuente.render(string, True, negro)
    pantalla.blit(texto, (300,200))
    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
        if botonContinuar.imprimirBotonInteractivo(negro):
            return 
        botonContinuar.textoEnBoton(fuente,'Continuar',blanco)
        pygame.display.update()

#Funcion para el texto de accion de derecho de paso 
def accionPaso(jug,duenno,propiedad):
    pantalla.fill(colorPared)
    dibujar_tablero()
    dineroJugadores()
    granAcumulado()
    if last_dice_image:
            x = dice_rect.x
            y = dice_rect.y
            pantalla.blit(last_dice_image, (x, y))
    font = pygame.font.Font("Fuentes/NexaHeavy.ttf", 20)
    botonContinuar = Boton(420,300,100,50,colorBotones)
    texto = font.render(f'{jug.nombre} paga a {duenno.nombre}', True, negro)
    texto2 = font.render(f'{propiedad.paso} por derecho de paso a', True, negro)
    texto3 = font.render(f'{propiedad.desc}', True, negro)

    fondo_tarjeta_rect = pygame.Rect(290, 190, 360, 200)
    pygame.draw.rect(pantalla, crema, fondo_tarjeta_rect)
    contorno_tarjeta_rect = pygame.Rect(290, 190, 360, 200)
    pygame.draw.rect(pantalla, (255, 255, 255), contorno_tarjeta_rect, 2)

    pantalla.blit(texto, (300,200))
    pantalla.blit(texto2,(300,225))
    pantalla.blit(texto3,(300,250))

    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
        if botonContinuar.imprimirBotonInteractivo(negro):
            return 
        font = pygame.font.Font("Fuentes/NexaHeavy.ttf",20)
        botonContinuar.textoEnBoton(font,'Continuar',blanco)
        pygame.display.update()

#Funcion que realiza el cobro de multa o tirar dados
def accionCarcel(jugador):
    global current_player_index
    pantalla.fill(colorPared)
    dibujar_tablero()
    dineroJugadores()
    granAcumulado()
    if last_dice_image:
            x = dice_rect.x
            y = dice_rect.y
            pantalla.blit(last_dice_image, (x, y))
    font = pygame.font.Font("Fuentes/NexaHeavy.ttf", 20)
    botonPagar = Boton(360, 270,100,50,colorBotones)
    botonDado = Boton(500, 270,100,50,colorBotones)
    texto = font.render(f'¿Desea pagar la multa o tirar los dados?', True, negro)

    fondo_tarjeta_rect = pygame.Rect(290, 190, 360, 200)
    pygame.draw.rect(pantalla, crema, fondo_tarjeta_rect)
    contorno_tarjeta_rect = pygame.Rect(290, 190, 360, 200)
    pygame.draw.rect(pantalla, (255, 255, 255), contorno_tarjeta_rect, 2)


    pantalla.blit(texto, (300,200))
    while True:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
        if botonPagar.imprimirBotonInteractivo(negro):
            banco.cobraGranAcumulado(conf[3],jugador)
            jugador.carcel = False
            return 
        botonPagar.textoEnBoton(font,'Pagar',blanco)
        if botonDado.imprimirBotonInteractivo(negro):
            dado1 = roll_dice()
            dado2 = roll_dice()
            if dado1 == dado2:
                return 
            else:
                accion('Dados no obtuvieron el mismo valor, seguirá en la carcel')
                current_player_index = (current_player_index + 1) % len(jugadores)
                return 
        botonDado.textoEnBoton(font,'Dado',blanco)
        pygame.display.update()



#Funcion de juego principal
def juego():
    global current_player_index, numeroJugadores
    # Bucle principal del juego
    running = True

    # Mostrar pantalla previa para ingresar la cantidad de jugadores
    num_jugadores = cantidadJugadores()
    num_jugadores = numeroJugadores

    # Crear jugadores
    crear_jugadores(num_jugadores)
    # Crear propiedades
    crearPropiedades(propiedadesAmbiente)
    #nombrar jugadores
    for i in range(len(jugadores)):
        jugadores[i].nombre = player_order[i][0]
    #pago inicial
    for jugador in jugadores:
        banco.realizaPago(conf[1],jugador)

    pantallaLargo = 1510
    pantallaAncho = 900
    pantalla = pygame.display.set_mode((pantallaLargo, pantallaAncho))

    current_player_index = 0  # Índice del jugador actual
    while running:
        #dibuja en pantalla todos los graficos 
        pantalla.fill(colorPared)
        dibujar_tablero()
        dineroJugadores()
        granAcumulado()
        # Dibujar imagen del último dado lanzado, si existe
        if last_dice_image:
            x = dice_rect.x
            y = dice_rect.y
            pantalla.blit(last_dice_image, (x, y))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            elif event.type == pygame.MOUSEBUTTONDOWN and not rolling:
                mouse_pos = pygame.mouse.get_pos()
                if dice_rect.collidepoint(mouse_pos):
                    dice_value = roll_dice()
                    #Si el jugador esta en la carcel 
                    if jugadores[current_player_index].posicion == 7 and jugadores[current_player_index].carcel:
                        if jugadores[current_player_index].turnosCarcel > 0:
                            jugadores[current_player_index].turnosCarcel -= 1
                            accion(f'El {jugadores[current_player_index].nombre} sigue en la carcel')
                            current_player_index = (current_player_index + 1) % len(jugadores)
                            continue
                        else:
                            #pagar multa de salida 
                            accion(f'{jugadores[current_player_index].nombre} debe pagar {conf[3]} por multa')
                            accionCarcel(jugadores[current_player_index])
                            break 

                    #si se pasa por la casilla de inicio 
                    if jugadores[current_player_index].posicion != 1 and jugadores[current_player_index].posicion + dice_value > 24: 
                        banco.realizaPago(conf[2],jugadores[current_player_index]) #el banco paga al jugador 
                        accion(f'Se le paga al {jugadores[current_player_index].nombre} el monto de inicio')
                    
                    #jugador se mueve
                    jugadores[current_player_index].move(dice_value)

                    #sacar carta de suerte en la casilla de suerte
                    if jugadores[current_player_index].posicion == 19:
                        carta = banco.sacarCarta(jugadores[current_player_index])
                        accion(carta[0])

                    #si el jugador cae en la carcel
                    if jugadores[current_player_index].posicion == 7 and jugadores[current_player_index].carcel == False:
                        jugadores[current_player_index].carcel = True
                        jugadores[current_player_index].turnosCarcel = 1
                        accion(f'{jugadores[current_player_index].nombre} entra a la carcel')

                    #paga el gran acumulado en la casilla de parada libre
                    if jugadores[current_player_index].posicion == 13 and banco.granAcum>0:
                        banco.pagaGranAcumulado(jugadores[current_player_index])
                        accion(f'El {jugadores[current_player_index].nombre} se lleva el Gran Acumulado')

                    for i in propiedades:
                        #Revisa si la propiedad se puede comprar o si se tiene la cantidad de dinero suficiente
                        if jugadores[current_player_index].posicion == i.pos and i.valor != 0 and jugadores[current_player_index].acumulado >= i.valor and i.estado == False: 
                            #compra la propiedad 
                            comprarPropiedad(jugadores[current_player_index],i)
                        #paga el derecho de paso
                        elif jugadores[current_player_index].posicion == i.pos and i.valor != 0 and i.estado == True:
                            for duenno in jugadores:
                                if i in duenno.propiedades:
                                    jugadores[current_player_index].pagaPaso(i,duenno)
                                    accionPaso(jugadores[current_player_index],duenno,i)    
                    
                    current_player_index = (current_player_index + 1) % len(jugadores)

        pygame.display.flip()

#Funcion inicial 
def inicio():
    global fondoImagen

    # Reproducir música de inicio
    if fondoImagen == playaGolfito:
        pygame.mixer.music.load('Canciones/inicio.mp3')
    elif fondoImagen == parqueIrazu:
        pygame.mixer.music.load('Canciones/inicio.mp3')
    pygame.mixer.music.play(-1)

    pantallaLargo = 1100
    pantallaAncho = 600
    pantalla = pygame.display.set_mode((pantallaLargo, pantallaAncho))
    corriendo = True
    textoAumenta = True
    textoEscalaAumento = 0
    clock = pygame.time.Clock()
    fondoPantalla = pygame.transform.scale(fondoImagen, (pantallaLargo, pantallaAncho))

    #Inicializa gif forzado
    imagenesRichUncleJuntas = []
    for fotos in imagenesRichUncle:
        foto = pygame.image.load(fotos)
        imagenesRichUncleJuntas.append(foto)

    #Reloj para el gif forzado
    clock = pygame.time.Clock()

    #Primera imagen gif forzado
    imagenesRichUncleActual = random.choice(imagenesRichUncleJuntas)
    imagenesRichUnclerect = imagenesRichUncleActual.get_rect(center=(pantallaLargo // 4.5, pantallaAncho // 1.7))

    #Timer gif forzado
    imagenesRichUncleTimer = pygame.time.get_ticks()
    imagenesRichUncleIntervalo = 500  #1000 millisegundos equivalen a 1 segundo

    while corriendo:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                corriendo = False

        # Aumentar y disminuir el tamaño del texto
        if textoAumenta:
            textoEscalaAumento += 0.1
            if textoEscalaAumento >= 1.1:
                textoAumenta = False
        else:
            textoEscalaAumento -= 0.001
            if textoEscalaAumento <= 1.9:
                textoAumenta = True

        imagenInicioEscalada = pygame.transform.scale(imagenInicio, (imagenInicioLargo, imagenInicioAncho))
        imagenInicioRectEscalada = imagenInicioEscalada.get_rect()
        imagenInicioRectEscalada.center = ((pantalla.get_width() // 2) + 4, (pantalla.get_height() // 2) + 4)

        #Revisión de gif forzado (momento para cambiar frame)
        momentoActual = pygame.time.get_ticks()
        if momentoActual - imagenesRichUncleTimer >= imagenesRichUncleIntervalo:
            imagenesRichUncleActual = random.choice(imagenesRichUncleJuntas)
            imagenesRichUnclerect = imagenesRichUncleActual.get_rect(center=(pantallaLargo // 4.5, pantallaAncho // 1.7))
            imagenesRichUncleTimer = momentoActual

        textoEscala = pygame.transform.rotozoom(texto, 0, textoEscalaAumento)
        textoEscalaRect = textoEscala.get_rect()
        textoEscalaRect.center = (pantalla.get_width() // 2, pantalla.get_height() // 2)

        textoEscalaSombra = pygame.transform.rotozoom(textoSombra, 0, textoEscalaAumento)
        textoEscalaRectSombra = textoEscalaSombra.get_rect()
        textoEscalaRectSombra.center = ((pantalla.get_width() // 2) + 4, (pantalla.get_height() // 2) + 4)

        pantalla.blit(fondoPantalla, (0, 0))
        
        pantalla.blit(imagenesRichUncleActual,imagenesRichUnclerect)

        pantalla.blit(imagenInicioEscalada, imagenInicioRectEscalada)
        pantalla.blit(textoEscalaSombra, textoEscalaRectSombra)
        pantalla.blit(textoEscala, textoEscalaRect)

        dibujar_botones_inicio()

        pygame.display.update()
        clock.tick(60)
        
    pygame.quit()

inicio()