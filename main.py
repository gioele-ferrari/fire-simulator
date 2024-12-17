import os
import time
import pygame
import sys
import random

SCREEN_WIDTH: int = 800
SCREEN_HEIGHT: int = 800
TILE_SIZE: int = 40

pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

MAP_WIDTH: int = SCREEN_WIDTH // TILE_SIZE
MAP_HEIGHT: int = SCREEN_HEIGHT // TILE_SIZE

FOREST_DENSITY: int = 0.2 # Densità del 20%
GROW_CHANCE = 0.0
FIRE_CHANCE = 0.3

COLOR_GREEN = (137, 234, 123)
TREE_IMG = pygame.image.load(os.path.join("images", "tree.png")).convert_alpha()
TREE_IMG = pygame.transform.scale(TREE_IMG, (TILE_SIZE, TILE_SIZE))

FIRE_IMG = pygame.image.load(os.path.join("images", "fire.png")).convert_alpha()
FIRE_IMG = pygame.transform.scale(FIRE_IMG, (TILE_SIZE, TILE_SIZE))

STEP_TIMER = 2
clock = pygame.time.Clock()


'''
    Funzione che gestisce il metodo principale di tutto il programma, quì si regolano
    le iterazioni e si gestiscono input come il reset o pulire la mappa.
'''
def main() -> None:
    forest = generate_forest()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key== pygame.K_r:
                    forest = generate_forest()

        screen.fill(COLOR_GREEN)
        display_forest(forest)
        forest = update_forest(forest)
        pygame.display.update()
        clock.tick(STEP_TIMER)


'''
    Funzionne per generare la forest casualmente, ci si basa su una densità
    di alberi da avere, nel caso il numero randomico sia inferiore allora mettiamo
    un albero.
'''
def generate_forest() -> list:
    forest_map = [[" " for _ in range(MAP_HEIGHT)] for _ in range(MAP_WIDTH)]
    for x_coord in range(MAP_WIDTH):
        for y_coord in range(MAP_HEIGHT):
            if random.random() <= FOREST_DENSITY:
                forest_map[x_coord][y_coord] = "T"
    return forest_map


'''
    Funzione per mostrare la foresta, in base al contenuto mostriamo lo sprite di
    un albero o di un fuoco, questa funzione serve solo per mostrare non è presente
    logica di simulazione. 
'''
def display_forest(forest) -> None:
    for x_coord in range(MAP_WIDTH):
        for y_coord in range(MAP_HEIGHT):
            if forest[x_coord][y_coord] == "T":
                screen.blit(TREE_IMG, (x_coord * TILE_SIZE, y_coord * TILE_SIZE))
            elif forest[x_coord][y_coord] == "F":
                screen.blit(FIRE_IMG, (x_coord * TILE_SIZE, y_coord * TILE_SIZE))


'''
    Serve per aggiornare a ogni iterazione la foresta, in questa funzione si calcola
    se far crescere un nuovo albero nella cella o se immettere un fuoco su un albero.
    In sequenza riconosciamo:
    - Se la nuova foresta è già stata impostata: saltiamo i controlli
    - Se nella vecchia foresta abbiamo uno spazio libero: chance di albero nuovo
    - Se nella vecchia foresta c'era un albero: chance di fuoco
    - Se nella vecchia foresta c'era un fuoco: lo dobbiamo dividere tra i vicini
    - Altrimenti rimane invariata
'''
def update_forest(old_forest) -> list:
    new_forest = [["O" for _ in range(MAP_HEIGHT)] for _ in range(MAP_WIDTH)]
    for x_coord in range(MAP_WIDTH):
        for y_coord in range(MAP_HEIGHT):
            if new_forest[x_coord][y_coord] != "O":
                continue

            if old_forest[x_coord][y_coord] == " " and random.random() <= GROW_CHANCE:
                new_forest[x_coord][y_coord] = "T"
            elif old_forest[x_coord][y_coord] == "T" and random.random() <= FIRE_CHANCE:
                new_forest[x_coord][y_coord] = "F"
            elif old_forest[x_coord][y_coord] == "F":
                for ix_coord in range(-1, 2):
                    for iy_coord in range(-1, 2):
                        if x_coord + ix_coord >= 0 and y_coord + iy_coord >= 0:
                            if x_coord + ix_coord <= (MAP_WIDTH - 1) and y_coord + iy_coord <= (MAP_HEIGHT - 1):
                                if old_forest[x_coord + ix_coord][y_coord + iy_coord] == "T":
                                    new_forest[x_coord + ix_coord][y_coord + iy_coord] = "F"
                new_forest[x_coord][y_coord] = " "
            else:
                new_forest[x_coord][y_coord] = old_forest[x_coord][y_coord]
    return new_forest


if __name__ == "__main__":
    main()