import random
import pygame
import sys
import math

class Maze:
    def __init__(self):
        self.wall = '#'
        self.cell = ' '
        self.unvisited = 'u'
        self.height = 10
        self.width = 10
        self.maze = []
        self.c=['0','1','2','3','4','5','6','7','8','9']
        self.cc=[0,1,2,3,4,5,6,7,8,9]

    def genWithGrid(self):
        for i in range(0, self.height):
            line = []
            for j in range(0, self.width):
                line.append(self.unvisited)
            self.maze.append(line)

        starting_height = int(random.random() * self.height)
        starting_width = int(random.random() * self.width)
        if (starting_height == 0):
            starting_height += 1
        if (starting_height == self.height - 1):
            starting_height -= 1
        if (starting_width == 0):
            starting_width += 1
        if (starting_width == self.width - 1):
            starting_width -= 1

        self.maze[starting_height][starting_width] = self.cell
        walls = []
        walls.append([starting_height - 1, starting_width])
        walls.append([starting_height, starting_width - 1])
        walls.append([starting_height, starting_width + 1])
        walls.append([starting_height + 1, starting_width])

        self.maze[starting_height - 1][starting_width] = '#'
        self.maze[starting_height][starting_width - 1] = '#'
        self.maze[starting_height][starting_width + 1] = '#'
        self.maze[starting_height + 1][starting_width] = '#'

        while (walls):
            rand_wall = walls[int(random.random() * len(walls)) - 1]

            if (rand_wall[1] != 0):
                if (self.maze[rand_wall[0]][rand_wall[1] - 1] == 'u' and self.maze[rand_wall[0]][rand_wall[1] + 1] == ' '):
                    s_cells = self.surroundingCells(rand_wall)

                    if (s_cells < 2):
                        self.maze[rand_wall[0]][rand_wall[1]] = ' '

                        if (rand_wall[0] != 0):
                            if (self.maze[rand_wall[0] - 1][rand_wall[1]] != ' '):
                                self.maze[rand_wall[0] - 1][rand_wall[1]] = '#'
                            if ([rand_wall[0] - 1, rand_wall[1]] not in walls):
                                walls.append([rand_wall[0] - 1, rand_wall[1]])

                        if (rand_wall[0] != self.height - 1):
                            if (self.maze[rand_wall[0] + 1][rand_wall[1]] != ' '):
                                self.maze[rand_wall[0] + 1][rand_wall[1]] = '#'
                            if ([rand_wall[0] + 1, rand_wall[1]] not in walls):
                                walls.append([rand_wall[0] + 1, rand_wall[1]])

                        if (rand_wall[1] != 0):
                            if (self.maze[rand_wall[0]][rand_wall[1] - 1] != ' '):
                                self.maze[rand_wall[0]][rand_wall[1] - 1] = '#'
                            if ([rand_wall[0], rand_wall[1] - 1] not in walls):
                                walls.append([rand_wall[0], rand_wall[1] - 1])

                    for wall in walls:
                        if (wall[0] == rand_wall[0] and wall[1] == rand_wall[1]):
                            walls.remove(wall)

                    continue

            if (rand_wall[0] != 0):
                if (self.maze[rand_wall[0] - 1][rand_wall[1]] == 'u' and self.maze[rand_wall[0] + 1][rand_wall[1]] == ' '):

                    s_cells = self.surroundingCells(rand_wall)
                    if (s_cells < 2):
                        self.maze[rand_wall[0]][rand_wall[1]] = ' '

                        if (rand_wall[0] != 0):
                            if (self.maze[rand_wall[0] - 1][rand_wall[1]] != ' '):
                                self.maze[rand_wall[0] - 1][rand_wall[1]] = '#'
                            if ([rand_wall[0] - 1, rand_wall[1]] not in walls):
                                walls.append([rand_wall[0] - 1, rand_wall[1]])

                        if (rand_wall[1] != 0):
                            if (self.maze[rand_wall[0]][rand_wall[1] - 1] != ' '):
                                self.maze[rand_wall[0]][rand_wall[1] - 1] = '#'
                            if ([rand_wall[0], rand_wall[1] - 1] not in walls):
                                walls.append([rand_wall[0], rand_wall[1] - 1])

                        if (rand_wall[1] != self.width - 1):
                            if (self.maze[rand_wall[0]][rand_wall[1] + 1] != ' '):
                                self.maze[rand_wall[0]][rand_wall[1] + 1] = '#'
                            if ([rand_wall[0], rand_wall[1] + 1] not in walls):
                                walls.append([rand_wall[0], rand_wall[1] + 1])

                    for wall in walls:
                        if (wall[0] == rand_wall[0] and wall[1] == rand_wall[1]):
                            walls.remove(wall)

                    continue

            if (rand_wall[0] != self.height - 1):
                if (self.maze[rand_wall[0] + 1][rand_wall[1]] == 'u' and self.maze[rand_wall[0] - 1][rand_wall[1]] == ' '):

                    s_cells = self.surroundingCells(rand_wall)
                    if (s_cells < 2):
                        self.maze[rand_wall[0]][rand_wall[1]] = ' '

                        if (rand_wall[0] != self.height - 1):
                            if (self.maze[rand_wall[0] + 1][rand_wall[1]] != 'c'):
                                self.maze[rand_wall[0] + 1][rand_wall[1]] = '#'
                            if ([rand_wall[0] + 1, rand_wall[1]] not in walls):
                                walls.append([rand_wall[0] + 1, rand_wall[1]])
                        if (rand_wall[1] != 0):
                            if (self.maze[rand_wall[0]][rand_wall[1] - 1] != 'c'):
                                self.maze[rand_wall[0]][rand_wall[1] - 1] = '#'
                            if ([rand_wall[0], rand_wall[1] - 1] not in walls):
                                walls.append([rand_wall[0], rand_wall[1] - 1])
                        if (rand_wall[1] != self.width - 1):
                            if (self.maze[rand_wall[0]][rand_wall[1] + 1] != 'c'):
                                self.maze[rand_wall[0]][rand_wall[1] + 1] = '#'
                            if ([rand_wall[0], rand_wall[1] + 1] not in walls):
                                walls.append([rand_wall[0], rand_wall[1] + 1])

                    for wall in walls:
                        if (wall[0] == rand_wall[0] and wall[1] == rand_wall[1]):
                            walls.remove(wall)

                    continue

            if (rand_wall[1] != self.width - 1):
                if (self.maze[rand_wall[0]][rand_wall[1] + 1] == 'u' and self.maze[rand_wall[0]][rand_wall[1] - 1] == ' '):

                    s_cells = self.surroundingCells(rand_wall)
                    if (s_cells < 2):
                        self.maze[rand_wall[0]][rand_wall[1]] = ' '

                        if (rand_wall[1] != self.width - 1):
                            if (self.maze[rand_wall[0]][rand_wall[1] + 1] != ' '):
                                self.maze[rand_wall[0]][rand_wall[1] + 1] = '#'
                            if ([rand_wall[0], rand_wall[1] + 1] not in walls):
                                walls.append([rand_wall[0], rand_wall[1] + 1])
                        if (rand_wall[0] != self.height - 1):
                            if (self.maze[rand_wall[0] + 1][rand_wall[1]] != ' '):
                                self.maze[rand_wall[0] + 1][rand_wall[1]] = '#'
                            if ([rand_wall[0] + 1, rand_wall[1]] not in walls):
                                walls.append([rand_wall[0] + 1, rand_wall[1]])
                        if (rand_wall[0] != 0):
                            if (self.maze[rand_wall[0] - 1][rand_wall[1]] != ' '):
                                self.maze[rand_wall[0] - 1][rand_wall[1]] = '#'
                            if ([rand_wall[0] - 1, rand_wall[1]] not in walls):
                                walls.append([rand_wall[0] - 1, rand_wall[1]])

                    for wall in walls:
                        if (wall[0] == rand_wall[0] and wall[1] == rand_wall[1]):
                            walls.remove(wall)

                    continue

            for wall in walls:
                if (wall[0] == rand_wall[0] and wall[1] == rand_wall[1]):
                    walls.remove(wall)

        for i in range(0, self.height):
            for j in range(0, self.width):
                if (self.maze[i][j] == 'u'):
                    self.maze[i][j] = '#'


    def surroundingCells(self,rand_wall):
        s_cells = 0
        if (self.maze[rand_wall[0] - 1][rand_wall[1]] == ' '):
            s_cells += 1
        if (self.maze[rand_wall[0] + 1][rand_wall[1]] == ' '):
            s_cells += 1
        if (self.maze[rand_wall[0]][rand_wall[1] - 1] == ' '):
            s_cells += 1
        if (self.maze[rand_wall[0]][rand_wall[1] + 1] == ' '):
            s_cells += 1

        return s_cells

    def __repr__(self):
        return self.finalmaze


    def placen(self,n):
        while True:
            x=random.randint(0,self.width-1)
            y=random.randint(0,self.width-1)
            if self.maze[x][y] == ' ':
                self.maze[x][y] = n
                break


    def sortie(self):
        self.maze[-1][-1] = '$'
        self.maze[-1][-2] = '$'
        self.maze[-2][-1] = '$'
        self.maze[-2][-2] = ' '

    def convert_str(self):
        self.finalmaze = ""

        for i in self.maze:
            for j in i:
                self.finalmaze += str(j)

        for i in range(10):
            print(self.finalmaze[i * 10:(i + 1) * 10])


    def collectibles(self):
        for i in range(10):
            self.placen(str(i))


class SuperMaze:
    def __init__(self,size):
        self.size = size
        self.maze = []

    def generates(self):
        for j in range(self.size):
            mm= Maze()
            mm.genWithGrid()
            mm.sortie()
            mm.convert_str()
            self.maze.append(mm.finalmaze)
        return self.maze


class Material:
    def __init__(self,char,color):
        self.char = char
        self.color = color
        self.type="wall"

    def __str__(self):
        return self.char

    def __repr__(self):
        return self.char

    def __eq__(self, other):
        return self.char == other

    def get_color(self):
        return self.color

    def get_type(self):
        return self.type

    def set_end(self):
        self.type="end"

    def end(self, game : pygame.init(),win,w,h):
        font = pygame.font.SysFont('Monospace Regular', 120)
        wing = font.render("you win", False, (255, 255, 255))
        win.blit(wing, (round(h/2), round(w/2)))
        game.quit()

class Collectibles(Material):
    def __init__(self,char,color):
        super().__init__(char,color)
        self.type="collectible"
        self.c=['0','1','2','3','4','5','6','7','8','9']
        self.collected=0

    def collect(self,x):
        self.collected+=1
        self.c.remove(x)


def mainloop(win,screenheight,screenwidth):
    finalmaze = Maze()
    finalmaze.genWithGrid()
    finalmaze.sortie()
    finalmaze.collectibles()
    finalmaze.convert_str()
    wallsmaze = Material("#", (210, 118, 31))
    endmaze = Material("$", (183, 109, 40))
    collectible = Collectibles("*", (255, 255, 255))
    player_x = ((screenheight / 2) / 40)*((18*2)-1)
    player_y = ((screenwidth / 2) / 40)*((18*2)-1)
    player_angle = math.pi
    MAP = finalmaze.finalmaze
    screenheight = win.get_height()
    screenwidth = win.get_width()
    msize = 10
    csize = int((screenwidth / 2) / msize)
    mdeth = int(msize * csize)
    fov = math.pi / 3
    hfov = fov / 2
    nbofrays = int(648/4)
    difangle = fov / nbofrays
    scale = (screenwidth) / nbofrays
    pygame.display.set_caption('Raycasting')
    clock = pygame.time.Clock()
    pygame.mouse.set_visible(False)
    displayinfo = False
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
        screenheight = win.get_height()
        screenwidth = win.get_width()
        msize = 10
        csize = int((screenwidth / 2) / msize)
        mdeth = int(msize * csize)
        fov = math.pi / 3
        hfov = fov / 2
        nbofrays = int(screenwidth / 4)
        difangle = fov / nbofrays
        scale = (screenwidth) / nbofrays

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
                gamewin(win, screenwidth, screenheight)
                endmaze.end(pygame, win,screenwidth,screenheight)
                break
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
        if keys[pygame.K_LEFT]: player_angle -= 0.15
        if keys[pygame.K_RIGHT]: player_angle += 0.15
        if keys[pygame.K_UP]:
            forward = True
            player_x += -math.sin(player_angle) * 4
            player_y += math.cos(player_angle) * 4
        if keys[pygame.K_UP] and keys[pygame.K_LCTRL]:
            forward = True
            player_x += -math.sin(player_angle) * 5
            player_y += math.cos(player_angle) * 5
        if keys[pygame.K_DOWN]:
            forward = False
            player_y -= math.cos(player_angle) * 4
            player_x -= -math.sin(player_angle) * 4
        if keys[pygame.K_j]:
            break
        if keys[pygame.K_t]:
            displayinfo=True
        if keys[pygame.K_t] and keys[pygame.K_LCTRL]:
            displayinfo=False
        if keys[pygame.K_p]:
            win=pygame.display.set_mode((screenwidth,screenheight),pygame.FULLSCREEN)
            screenheight = win.get_height()
            screenwidth = win.get_width()
            msize = 10
            csize = int((screenwidth / 2) / msize)
            mdeth = int(msize * csize)
            fov = math.pi / 3
            hfov = fov / 2
            nbofrays = int(648 / 4)
            difangle = fov / nbofrays
            scale = (screenwidth) / nbofrays

        clock.tick(20)
        font = pygame.font.SysFont('Monospace Regular', 30)
        if displayinfo:
            fps = str(int(clock.get_fps()))
            fps_surface = font.render(fps, False, (255, 255, 255))
            win.blit(fps_surface, (10, 10))
            player_pos = str(int(player_x)) + "," + str(int(player_y))
            player_pos_surface = font.render(player_pos, False, (255, 255, 255))
            win.blit(player_pos_surface, (10, 30))
            collected = str(collectible.collected) + "/10"
            collected_surface = font.render(collected, False, (255, 255, 255))
            win.blit(collected_surface, (10, 50))
        else:
            collected = str(collectible.collected) + "/10"
            collected_surface = font.render(collected, False, (255, 255, 255))
            win.blit(collected_surface, (10, 10))
        pygame.display.flip()

def startmenu(win,screenwidth,screenheight):
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)
        win.fill((0, 0, 0))
        font = pygame.font.SysFont('Monospace Regular', 30)
        start_surface = font.render("Press Enter to start", False, (255, 255, 255))
        win.blit(start_surface, (10, 10))
        pygame.display.flip()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RETURN]:
            mainloop(win,screenwidth,screenheight)
            break
        if keys[pygame.K_p]:
            win=pygame.display.set_mode((screenwidth,screenheight),pygame.FULLSCREEN)
            screenheight = win.get_height()
            screenwidth = win.get_width()

def gamewin(win,screenwidth,screenheight):
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)
        win.fill((0, 0, 0))
        font = pygame.font.SysFont('Monospace Regular', 30)
        win_surface = font.render("You Win! For play again press enter", False, (255, 255, 255))
        win.blit(win_surface, (10, 10))
        pygame.display.flip()
        keys = pygame.key.get_pressed()
        if keys[pygame.K_RETURN]:
            mainloop(win,screenwidth,screenheight)
            break
        if keys[pygame.K_p]:
            win=pygame.display.set_mode((screenwidth,screenheight),pygame.FULLSCREEN)
            screenheight = win.get_height()
            screenwidth = win.get_width()


pygame.init()
screenheight = 648
screenwidth = screenheight * 2
win = pygame.display.set_mode((screenwidth, screenheight))

startmenu(win,screenwidth,screenheight)