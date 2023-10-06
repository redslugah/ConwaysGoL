import pygame
import os.path
import random
import time

class  Cell:
    def __init__(self):
        self.type = DEAD
        self.checked = False


GRID_SIZE = 30
CELL_SIZE = 20
WIDTH, HEIGHT = GRID_SIZE*CELL_SIZE+1,GRID_SIZE*CELL_SIZE+1
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
FILL = (50,50,50)
FPS = 60
global refresh
refresh = 0.2
global simu
simu = False
cell_color = (255,255,255)
DEADD = pygame.image.load(os.path.join('assets', 'dead.png'))
novo_tamanho = (CELL_SIZE-0.2, CELL_SIZE-0.2)
DEAD = pygame.transform.scale(DEADD, novo_tamanho)
ALIVEE = pygame.image.load(os.path.join('assets', 'alive.png'))
novo_tamanho = (CELL_SIZE-0.2, CELL_SIZE-0.2)
ALIVE = pygame.transform.scale(ALIVEE, novo_tamanho)
global board
board = [[Cell() for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]

def display():
    WIN.fill(FILL)
    for iy, rowOfCells in enumerate(board):
        for ix, cell in enumerate(rowOfCells):
                if cell.type:
                    #WIN.blit(cell.type, (iy*CELL_SIZE+1, ix*CELL_SIZE+1, CELL_SIZE-2, CELL_SIZE-2))
                    WIN.blit(cell.type, (iy*CELL_SIZE+1, ix*CELL_SIZE+1))
                
    pygame.display.update()
    
def find_izinhos(y, x):
    deads = 0
    alives = 0
    try:
        if (board[y-1 if y != 0 else (GRID_SIZE-1)][x-1 if x != 0 else (GRID_SIZE-1)].type == DEAD):
            deads +=1
        else:
            alives +=1
    except IndexError:
        pass
    try:
        if (board[y-1 if y != 0 else (GRID_SIZE-1)][x].type == DEAD):
            deads +=1
        else:
            alives +=1
    except IndexError:
        pass
    try:
        if (board[y-1 if y !=0 else (GRID_SIZE-1)][x+1 if x != (GRID_SIZE-1) else 0].type == DEAD):
            deads +=1
        else:
            alives +=1
    except IndexError:
        pass
    try:
        if (board[y][x-1 if x != 0 else (GRID_SIZE-1)].type == DEAD):
            deads +=1
        else:
            alives +=1
    except IndexError:
        pass
    try:
        if (board[y][x+1 if x != (GRID_SIZE-1) else 0].type == DEAD):
            deads +=1
        else:
            alives +=1
    except IndexError:
        pass
    try:
        if (board[y+1 if y != (GRID_SIZE-1) else 0][x-1 if x !=0 else (GRID_SIZE-1)].type == DEAD):
            deads +=1
        else:
            alives +=1
    except IndexError:
        pass
    try:
        if (board[y+1 if y != (GRID_SIZE-1) else 0][x].type == DEAD):
            deads +=1
        else:
            alives +=1
    except IndexError:
        pass
    try:
        if (board[y+1 if y != (GRID_SIZE-1) else 0][x+1 if x != (GRID_SIZE-1) else 0].type == DEAD):
            deads +=1
        else:
            alives +=1
    except IndexError:
        pass
    #print(deads,alives)
    #print(y,x)
    return alives, deads

def changeCell(l, d, cell):
    #print(l)
    if cell.type == ALIVE:
        if l == 2 or l == 3:
            return ALIVE
        else: return DEAD
    else:
        if l == 3:
            return ALIVE
        else: return DEAD
        

def start_simmulation():
    lizinhos = 0
    dizinhos = 0
    global board
    global refresh
    tboard = [[Cell() for _ in range(GRID_SIZE)] for _ in range(GRID_SIZE)]   
    for iy, rowOfCells in enumerate(board):
        for ix, cell in enumerate(rowOfCells):
            if cell.checked is not True:
                lizinhos, dizinhos = find_izinhos(iy, ix)
                tboard[iy][ix].type = changeCell(lizinhos, dizinhos, cell)
                cell.checked = True

    for iy, rowOfCells in enumerate(board):
        for ix, cell in enumerate(rowOfCells):
            cell.checked = False
    board = tboard
    time.sleep(refresh)
            
            


def fill_random(pos):
    x = pos[0]//CELL_SIZE
    y = pos[1]//CELL_SIZE
    try:
        if board[x][y].type == DEAD:
            board[x][y].type = ALIVE
        else:
            board[x][y].type = DEAD
            #pass
    except IndexError:
        pass
    #print(x,y)
    #start_simmulation()


def click_action(event):
    #print(event)
    global simu
    if event.button == 1:
        if simu:
            pass
        else: 
            #for i in range(15000):
                #fill_random((random.randint(0,WIDTH-1),random.randint(0,HEIGHT-1)))
            fill_random(event.pos)
    elif event.button == 3:
        if not simu:
            simu = True
        else:
            simu = False

    #fill_random((random.randint(0,GRID_SIZE-1),random.randint(0,GRID_SIZE-1)))

def main():
    global gamerunning
    gamerunning = True
    start_tick = pygame.time.get_ticks()
    pygame.init()
    clock = pygame.time.Clock()
    run = True
    clock.tick(FPS)
    while run:
        if gamerunning:

            display()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.pos[1] // 1 >= 0:
                        click_action(event)
            if simu: start_simmulation()


if __name__ == '__main__':
    main() 