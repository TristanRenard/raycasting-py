import random
import pygame
import sys
import math
import materials
import laby

finalmaze = laby.Maze()
finalmaze.genWithGrid()
finalmaze.sortie()
finalmaze.collectibles()
finalmaze.convert_str()
screenheight = 648
screenwidth = screenheight * 2
msize = 10
csize = int((screenwidth / 2) / msize)
mdeth = int(msize * csize)
fov = math.pi / 3
hfov = fov / 2
nbofrays = int(648/4)
difangle = fov / nbofrays
scale = (screenwidth) / nbofrays
wallsmaze = materials.Material("#", (210, 118, 31))
endmaze = materials.Material("$", (183, 109, 40))
collectible = materials.Collectibles("*", (255, 255, 255))
player_x = ((screenheight / 2) / 40)*((18*2)-1)
player_y = ((screenheight / 2) / 40)*((18*2)-1)
player_angle = math.pi
collected= False
MAP = finalmaze.finalmaze
pygame.init()
win = pygame.display.set_mode((screenwidth, screenheight))
pygame.display.set_caption('Raycasting')
clock = pygame.time.Clock()
chrono = pygame.time.Clock()
chrono.tick()

def cast_rays():
    start_angle = player_angle - hfov
    for ray in range(nbofrays):
        for depth in range(mdeth):
            target_x = player_x - math.sin(start_angle) * depth
            target_y = player_y + math.cos(start_angle) * depth
            col = int(target_x / csize)
            row = int(target_y / csize)
            square = row * msize + col
            if MAP[square] == wallsmaze or MAP[square] == endmaze or MAP[square] in collectible.c:
                if MAP[square] == wallsmaze:
                    wallhit = wallsmaze
                    colorR = wallhit.color[0] / (1 + depth * depth * 0.0001)
                    colorG = wallhit.color[1] / (1 + depth * depth * 0.0001)
                    colorB = wallhit.color[2] / (1 + depth * depth * 0.0001)
                    depth *= math.cos(player_angle - start_angle)
                    wall_height = 21000 / (depth + 0.0001)
                    if wall_height > screenheight: wall_height = screenheight
                    pygame.draw.rect(win, (colorR, colorG, colorB), (1 + ray * scale,(screenheight / 2) - wall_height / 2,scale, wall_height))
                    break
                elif MAP[square] == endmaze:
                    wallhit = endmaze
                    colorR = wallhit.color[0] / (1 + depth * depth * 0.0001)
                    colorG = wallhit.color[1] / (1 + depth * depth * 0.0001)
                    colorB = wallhit.color[2] / (1 + depth * depth * 0.0001)
                    depth *= math.cos(player_angle - start_angle)
                    wall_height = 21000 / (depth + 0.0001)
                    if wall_height > screenheight: wall_height = screenheight
                    pygame.draw.rect(win, (colorR, colorG, colorB), (1 + ray * scale,(screenheight / 2) - wall_height / 2,scale, wall_height))
                    break
                elif MAP[square] in collectible.c:
                    colorR = random.randint(0,255) / (1 + depth * depth * 0.0001)
                    colorG = random.randint(0,255) / (1 + depth * depth * 0.0001)
                    colorB = random.randint(0,255) / (1 + depth * depth * 0.0001)
                    depth *= math.cos(player_angle - start_angle)
                    wall_height = 21000 / (depth + 0.0001)
                    if wall_height > screenheight: wall_height = screenheight
                    pygame.draw.rect(win, (colorR, colorG, colorB), (1 + ray * scale,(screenheight / 2) - wall_height / 2,scale, wall_height))
                    break
                else:
                    colorR=255/(1+depth*depth*0.0001)
                    colorG=255/(1+depth*depth*0.0001)
                    colorB=255/(1+depth*depth*0.0001)
                    depth *= math.cos(player_angle - start_angle)
                    wall_height = 21000 / (depth + 0.0001)
                    if wall_height > screenheight: wall_height = screenheight
                    pygame.draw.rect(win, (colorR, colorG, colorB), (1 + ray * scale,(screenheight / 2) - wall_height / 2,scale, wall_height))
                    break
        start_angle += difangle
forward = True
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)
    col = int(player_x / csize)
    row = int(player_y / csize)
    square = row * msize + col
    if MAP[square] == wallsmaze:
        if forward:
            player_x -= -math.sin(player_angle) * 5
            player_y -= math.cos(player_angle) * 5
        else:
            player_x += -math.sin(player_angle) * 5
            player_y += math.cos(player_angle) * 5
    if MAP[square] == endmaze:
        if collectible.collected == 10:
            print("win !")
            endmaze.end(pygame, win,screenwidth,screenheight)
        else:
            if forward:
                player_x -= -math.sin(player_angle) * 5
                player_y -= math.cos(player_angle) * 5
            else:
                player_x += -math.sin(player_angle) * 5
                player_y += math.cos(player_angle) * 5
    if MAP[square] in collectible.c:
        collectible.collect(MAP[square])
    pygame.draw.rect(win, (0, 0, 0), (0, 0, screenwidth, screenheight))
    pygame.draw.rect(win, (0, 200, 0), (0, screenheight / 2, screenwidth, screenheight))
    pygame.draw.rect(win, (0, 255, 201), (0, -screenheight / 2, screenwidth, screenheight))
    cast_rays()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]: player_angle -= 0.1
    if keys[pygame.K_RIGHT]: player_angle += 0.1
    if keys[pygame.K_UP]:
        forward = True
        player_x += -math.sin(player_angle) * 5
        player_y += math.cos(player_angle) * 5
    if keys[pygame.K_UP] and keys[pygame.K_LCTRL]:
        forward = True
        player_x += -math.sin(player_angle) * 6
        player_y += math.cos(player_angle) * 6
    if keys[pygame.K_DOWN]:
        forward = False
        player_y -= math.cos(player_angle) * 5
        player_x -= -math.sin(player_angle) * 5
    if keys[pygame.K_j]:
        pygame.quit()
    clock.tick(40)
    fps = str(int(clock.get_fps()))
    font = pygame.font.SysFont('Monospace Regular', 30)
    fps_surface = font.render(fps, False, (255, 255, 255))
    win.blit(fps_surface, (10, 0))
    player_pos = str(int(player_x)) + "," + str(int(player_y))
    player_pos_surface = font.render(player_pos, False, (255, 255, 255))
    win.blit(player_pos_surface, (10, 30))
    collected = str(collectible.collected) + "/10"
    collected_surface = font.render(collected, False, (255, 255, 255))
    win.blit(collected_surface, (10, 60))
    pygame.display.flip()
