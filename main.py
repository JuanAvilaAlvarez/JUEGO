import pygame
import sys
import random

pygame.init()

size = width, height = 600, 600
screen = pygame.display.set_mode(size)
background = (255, 255, 255)

# Lista para el orden de las fichas (números del 1 al 8)
orden = [i for i in range(1, 9)] + [0]  # Orden inicial del rompecabezas (0 representa el espacio vacío)

# Mezclar el orden de las fichas
random.shuffle(orden)

# Tamaño de cada cuadro de ficha
ficha = width // 3

# Función para dibujar el tablero
def tablero():
    font = pygame.font.Font(None, 36)
    for i in range(9):
        fila = i // 3
        col = i % 3
        x = col * ficha
        y = fila * ficha
        if orden[i] != 0:
            number_text = font.render(str(orden[i]), True, (0, 0, 0))
            text_rect = number_text.get_rect(center=(x + ficha // 2, y + ficha // 2))
            screen.blit(number_text, text_rect)
        elif esta_resuelto():  # Verificar si el rompecabezas está resuelto
            # Dibujar el número "9" en el espacio vacío (esquina inferior derecha)
            number_text = font.render("9", True, (0, 0, 0))
            text_rect = number_text.get_rect(center=(x + ficha // 2, y + ficha // 2))
            screen.blit(number_text, text_rect)


# Función para intercambiar las fichas
def mover_ficha(index1, index2):
    orden[index1], orden[index2] = orden[index2], orden[index1]

# Función para verificar si el rompecabezas está resuelto
def esta_resuelto():
    return orden == [i for i in range(1, 9)] + [0]

def main():
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                empty_index = orden.index(0)
                if event.key == pygame.K_UP and empty_index + 3 < 9:
                    mover_ficha(empty_index, empty_index + 3)
                elif event.key == pygame.K_DOWN and empty_index - 3 >= 0:
                    mover_ficha(empty_index, empty_index - 3)
                elif event.key == pygame.K_LEFT and empty_index % 3 != 2:
                    mover_ficha(empty_index, empty_index + 1)
                elif event.key == pygame.K_RIGHT and empty_index % 3 != 0:
                    mover_ficha(empty_index, empty_index - 1)

        screen.fill(background)
        tablero()
        pygame.display.flip()

if __name__ == "__main__":
    main()
