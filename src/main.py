import random
import pygame
import sys
import math
from classes import laby, materials
from classes.musicmanager import MusicManager

pausemusic = MusicManager("musics/pause.mp3")


music = MusicManager("musics/music.mp3")

gmusic = MusicManager("musics/wing.mp3")

startmusic = MusicManager("musics/win.mp3")

fullscreen = False
options = [10,10]

def pausemenu(win,fullscreen):
    """
    Menu pause (quand la touche échap est pressée pendant le jeu)
    """
    pausemusic.play_music()
    while True:
        pygame.mouse.set_visible(True)
        win.fill((0, 0, 0))
        win.blit(pygame.transform.scale(pygame.image.load("images/background.png"), (win.get_width(), win.get_height())), (0, 0))

        banner = pygame.image.load("images/banner.png")
        banner = pygame.transform.scale(banner, (banner.get_width(), banner.get_height()))
        win.blit(banner, (int((win.get_width() - banner.get_width()) / 2), int((win.get_height() - banner.get_height()) / 2)-145))

        resumebtn = pygame.image.load("images/resumebtn.png")
        resumebtn = pygame.transform.scale(resumebtn, (221, 49))
        win.blit(resumebtn, (int((win.get_width()-221)/2) , int(int((win.get_height())-49)/2)+60))
        resumebtn_rect = resumebtn.get_rect()
        resumebtn_rect.x = int((win.get_width()-221)/2)
        resumebtn_rect.y = int(int((win.get_height())-49)/2)+60

        playbtn = pygame.image.load("images/restart.png")
        playbtn = pygame.transform.scale(playbtn, (221, 49))
        win.blit(playbtn, (int((win.get_width()-221)/2) , int(int((win.get_height())-49)/2)+130))
        playbtn_rect = playbtn.get_rect()
        playbtn_rect.x = int((win.get_width()-221)/2)
        playbtn_rect.y = int(int((win.get_height())-49)/2)+130


        homebtn = pygame.image.load("images/homebtn.png")
        homebtn = pygame.transform.scale(homebtn, (221, 49))
        win.blit(homebtn, (int((win.get_width()-221)/2) , int(int((win.get_height())-49)/2)+200))
        homebtn_rect = homebtn.get_rect()
        homebtn_rect.x = int((win.get_width()-221)/2)
        homebtn_rect.y = int(int((win.get_height())-49)/2)+200


        quitbtn = pygame.image.load("images/quitbtn.png")
        quitbtn = pygame.transform.scale(quitbtn, (221, 49))
        win.blit(quitbtn, (int((win.get_width()-221)/2) , int(int((win.get_height())-49)/2)+270))
        quitbtn_rect = quitbtn.get_rect()
        quitbtn_rect.x = int((win.get_width()-221)/2)
        quitbtn_rect.y = int(int((win.get_height())-49)/2)+270

        if fullscreen == False:
            fullscreenbtn = pygame.image.load("images/fullscreen.png")
            fullscreenbtn = pygame.transform.scale(fullscreenbtn, (45, 45))
            win.blit(fullscreenbtn, (int((win.get_width()-65)) , int(win.get_height())-65))
            fullscreenbtn_rect = fullscreenbtn.get_rect()
            fullscreenbtn_rect.x = int(int(win.get_width())-65)
            fullscreenbtn_rect.y = int(int(win.get_height())-65)

        pygame.display.flip()

        keys = pygame.key.get_pressed()

        # vérifie les boutons pressés
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if playbtn_rect.collidepoint(pygame.mouse.get_pos(event.pos)):
                    mainloop(win, screenwidth, screenheight,fullscreen)
                    break
                if homebtn_rect.collidepoint(pygame.mouse.get_pos(event.pos)):
                    pausemusic.stop_music()
                    startmenu(win, win.get_width(), win.get_height(),fullscreen)
                if quitbtn_rect.collidepoint(pygame.mouse.get_pos(event.pos)):
                    pygame.quit()
                    sys.exit(0)
                if resumebtn_rect.collidepoint(pygame.mouse.get_pos(event.pos)):
                    pausemusic.stop_music()
                    return
                if fullscreenbtn_rect.collidepoint(pygame.mouse.get_pos(event.pos)):
                    if fullscreen == False:
                        fullscreen = True
                        win = pygame.display.set_mode((screenwidth, screenheight), pygame.FULLSCREEN)


def mainloop(win,screenheight,screenwidth,fullscreen):
    """
    Boucle principale du jeu
    :param win:
    :param screenheight:
    :param screenwidth:
    :param fullscreen:
    :return: game
    """
    #joue la musique du jeu
    music.play_music()
    #génère le niveau
    finalmaze = laby.Maze(options[0])
    finalmaze.genrandomly()
    finalmaze.sortie()
    finalmaze.collectibles()
    finalmaze.convert_str()
    #créer les materiaux
    wallsmaze = materials.Material("#", (210, 118, 31))
    endmaze = materials.Material("$", (183, 109, 40))
    collectible = materials.Collectibles("*", (255, 255, 255))
    #les constantes du jeu
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
    chrono = [0,0,0,0]
    def cast_rays():
        #fonction pour calculer les rayons et faire le rendu
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
                        #set color from wall
                        colorR = wallhit.color[0] / (1 + depth * depth * 0.0001)
                        colorG = wallhit.color[1] / (1 + depth * depth * 0.0001)
                        colorB = wallhit.color[2] / (1 + depth * depth * 0.0001)
                        depth *= math.cos(player_angle - start_angle)
                        wall_height = 21000 / (depth + 0.0001)
                        if wall_height > screenheight: wall_height = screenheight
                        #display wall
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
                        pygame.draw.rect(win,(colorR, colorG, colorB), (1 + ray * scale,(screenheight / 2) - wall_height / 2,scale, wall_height))
                        break
            start_angle += difangle
    forward = True
    while True:
        #check music statut
        if music.is_playing() == False:
            try:
                music.resume_music()
            except Exception:
                print(Exception)
            try:
                music.resume_music()
            except Exception:
                print(Exception)
        #gestion du chrono
        if ((chrono[3]+5)  > 100):
            chrono[3] = 0
            if chrono[2] > 59:
                chrono[2] = 0
                if chrono[1] > 59:
                    chrono[1] = 0
                    chrono[0] = chrono[0] + 1
                else:chrono[1] = chrono[1] + 1
            else:chrono[2]+=1
        else:chrono[3] = chrono[3] + 5
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
        #gère les events pygame
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)
        col = int(player_x / csize)
        row = int(player_y / csize)
        square = row * msize + col
        #gère les colisions
        if (MAP[square] == wallsmaze):
            if forward:
                player_x -= -math.sin(player_angle) * 7
                player_y -= math.cos(player_angle) * 7
            else:
                player_x += -math.sin(player_angle) * 7
                player_y += math.cos(player_angle) * 7
        if MAP[square] == endmaze:
            if collectible.collected == 10:
                print("win !")
                music.stop_music()
                gamewin(win, screenwidth, screenheight, (chrono[0], chrono[1], chrono[2], chrono[3]),fullscreen)
                endmaze.end(pygame, win,screenwidth,screenheight)
                break
            else:
                if forward:
                    player_x -= -math.sin(player_angle) * 7
                    player_y -= math.cos(player_angle) * 7
                else:
                    player_x += -math.sin(player_angle) * 7
                    player_y += math.cos(player_angle) * 7
        #gère les collectibles
        if MAP[square] in collectible.c:
            collectible.collect(MAP[square])
        pygame.draw.rect(win, (0, 0, 0), (0, 0, screenwidth, screenheight))
        pygame.draw.rect(win, (0, 200, 0), (0, screenheight / 2, screenwidth, screenheight))
        pygame.draw.rect(win, (0, 255, 201), (0, -screenheight / 2, screenwidth, screenheight))
        cast_rays()

        #gère les déplacements et les touches
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]or keys[pygame.K_q]: player_angle -= 0.15
        if keys[pygame.K_RIGHT] or keys[pygame.K_d] : player_angle += 0.15
        if (keys[pygame.K_UP]or keys[pygame.K_z]) and not keys[pygame.K_LSHIFT]:
            forward = True
            player_x += -math.sin(player_angle) * 4
            player_y += math.cos(player_angle) * 4
        if (keys[pygame.K_UP] or keys[pygame.K_z]) and keys[pygame.K_LSHIFT]:
            forward = True
            player_x += -math.sin(player_angle) * 7
            player_y += math.cos(player_angle) * 7
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            forward = False
            player_y -= math.cos(player_angle) * 4
            player_x -= -math.sin(player_angle) * 4
        if keys[pygame.K_t]:
            displayinfo=True
        if keys[pygame.K_t] and keys[pygame.K_LCTRL]:
            displayinfo=False
        if keys[pygame.K_ESCAPE]:
            music.pause_music()
            pausemenu(win,fullscreen)
            music.play_music()



        #nb de tick par secondes
        clock.tick(20)
        font = pygame.font.SysFont('Monospace Regular', 30)

        h=int(chrono[0])
        m=int(chrono[1])
        s=int(chrono[2])
        ms=int(chrono[3])
        if h<10:
            h="0"+str(h)
        else:
            h=str(h)
        if m<10:
            m="0"+str(m)
        else:
            m=str(m)
        if s<10:
            s="0"+str(s)
        else:
            s=str(s)
        if ms<10:
            ms="0"+str(ms)
        else:
            ms=str(ms)
        #affichages des informations
        if displayinfo:
            pchonom = m + " : "+ s + " : "+ ms
            pchonom_surface = font.render(pchonom, False, (255, 255, 255))
            win.blit(pchonom_surface, (10, 70))
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
            pchonom = m + " : " + s + " : " + ms
            pchonom_surface = font.render(pchonom, False, (255, 255, 255))
            win.blit(pchonom_surface, (10, 30))
        pygame.display.flip()

#menu de démarage
def startmenu(win,screenwidth,screenheight,fullscreen):
    startmusic.play_music()
    while True:
        pygame.mouse.set_visible(True)
        win.blit(pygame.transform.scale(pygame.image.load("images/background.png"), (win.get_width(), win.get_height())), (0, 0))

        banner = pygame.image.load("images/banner.png")
        banner = pygame.transform.scale(banner, (banner.get_width(), banner.get_height()))
        win.blit(banner, (int((win.get_width() - banner.get_width()) / 2), int((win.get_height() - banner.get_height()) / 2)-125))

        playbtn = pygame.image.load("images/playbtn.png")
        playbtn = pygame.transform.scale(playbtn, (221, 49))
        win.blit(playbtn, (int((win.get_width()-221)/2) , int(int((win.get_height())-49)/2)+130))
        playbtn_rect = playbtn.get_rect()
        playbtn_rect.x = int((win.get_width()-221)/2)
        playbtn_rect.y = int(int((win.get_height())-49)/2)+130


        quitbtn = pygame.image.load("images/quitbtn.png")
        quitbtn = pygame.transform.scale(quitbtn, (221, 49))
        win.blit(quitbtn, (int((win.get_width()-221)/2) , int(int((win.get_height())-49)/2)+200))
        quitbtn_rect = quitbtn.get_rect()
        quitbtn_rect.x = int((win.get_width()-221)/2)
        quitbtn_rect.y = int(int((win.get_height())-49)/2)+200


        if fullscreen == False:
            fullscreenbtn = pygame.image.load("images/fullscreen.png")
            fullscreenbtn = pygame.transform.scale(fullscreenbtn, (45, 45))
            win.blit(fullscreenbtn, (int((win.get_width()-65)) , int(win.get_height())-65))
            fullscreenbtn_rect = fullscreenbtn.get_rect()
            fullscreenbtn_rect.x = int(int(win.get_width())-65)
            fullscreenbtn_rect.y = int(int(win.get_height())-65)


        pygame.display.flip()

        keys = pygame.key.get_pressed()


        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if playbtn_rect.collidepoint(pygame.mouse.get_pos(event.pos)):
                    startmusic.stop_music()
                    mainloop(win, screenwidth, screenheight,fullscreen)
                    break
                if quitbtn_rect.collidepoint(pygame.mouse.get_pos(event.pos)):
                    pygame.quit()
                    sys.exit(0)
                if fullscreenbtn_rect.collidepoint(pygame.mouse.get_pos(event.pos)):
                    if fullscreen == False:
                        fullscreen = True
                        win = pygame.display.set_mode((screenwidth, screenheight), pygame.FULLSCREEN)

#menu de partie gagnée
def gamewin(win,screenwidth,screenheight, chrono,fullscreen):

    gmusic.play_music()
    while True:
        win.fill((0, 0, 0))
        win.blit(pygame.transform.scale(pygame.image.load("images/background.png"), (win.get_width(), win.get_height())), (0, 0))

        winbanner = pygame.image.load("images/winbanniere.png")
        winbanner = pygame.transform.scale(winbanner, ( winbanner.get_width(), winbanner.get_height()))
        win.blit(winbanner, (int((win.get_width()-winbanner.get_width())/2), int((win.get_height() - winbanner.get_height())/2)))

        font_chrono = pygame.font.SysFont('Monospace Regular', 55)
        chrnon_str = str(chrono[0]) + " : " + str(chrono[1]) + " : " + str(chrono[2])+"."+str(chrono[3])
        chrono_surface = font_chrono.render(chrnon_str, False, (255, 255, 255))
        win.blit(chrono_surface, (int((win.get_width()-winbanner.get_width())/2)+300, int((win.get_height() - winbanner.get_height())/2)+187))

        homebtn = pygame.image.load("images/homebtn.png")
        homebtn = pygame.transform.scale(homebtn, (221, 49))
        win.blit(homebtn, (int((win.get_width()-221)/2) , int(int((win.get_height())-49)/2)+130))
        homebtn_rect = homebtn.get_rect()
        homebtn_rect.x = int((win.get_width()-127)/2)
        homebtn_rect.y = int(int((win.get_height())-67)/2)+130

        restartbtn = pygame.image.load("images/pagainbtn.png")
        restartbtn = pygame.transform.scale(restartbtn, (221, 49))
        win.blit(restartbtn, (int((win.get_width()-221)/2) , int(int((win.get_height())-49)/2)+200))
        restartbtn_rect = restartbtn.get_rect()
        restartbtn_rect.x = int((win.get_width()-221)/2)
        restartbtn_rect.y = int(int((win.get_height())-67)/2)+200

        exitbtn = pygame.image.load("images/quitbtn.png")
        exitbtn = pygame.transform.scale(exitbtn, (221, 49))
        win.blit(exitbtn, (int((win.get_width()-221)/2) , int(int((win.get_height())-49)/2)+270))
        exitbtn_rect = exitbtn.get_rect()
        exitbtn_rect.x = int((win.get_width()-221)/2)
        exitbtn_rect.y = int(int((win.get_height())-67)/2)+270


        if fullscreen == False:
            fullscreenbtn = pygame.image.load("images/fullscreen.png")
            fullscreenbtn = pygame.transform.scale(fullscreenbtn, (45, 45))
            win.blit(fullscreenbtn, (int((win.get_width()-65)) , int(win.get_height())-65))
            fullscreenbtn_rect = fullscreenbtn.get_rect()
            fullscreenbtn_rect.x = int(int(win.get_width())-65)
            fullscreenbtn_rect.y = int(int(win.get_height())-65)


        pygame.mouse.set_visible(True)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if homebtn_rect.collidepoint(pygame.mouse.get_pos(event.pos)):
                    startmenu(win,screenwidth,screenheight,fullscreen)
                    break
                if restartbtn_rect.collidepoint(pygame.mouse.get_pos(event.pos)):
                    mainloop(win,screenwidth,screenheight,fullscreen)
                    break
                if exitbtn_rect.collidepoint(pygame.mouse.get_pos(event.pos)):
                    pygame.quit()
                    sys.exit(0)
                if fullscreenbtn_rect.collidepoint(pygame.mouse.get_pos(event.pos)):
                    if fullscreen == False:
                        fullscreen = True
                        win = pygame.display.set_mode((screenwidth, screenheight), pygame.FULLSCREEN)


        pygame.display.flip()

#initialisation du jeu
pygame.init()
screenheight = 648
screenwidth = screenheight * 2
win = pygame.display.set_mode((screenwidth, screenheight), pygame.NOFRAME)
#démarage du jeu
startmenu(win,screenwidth,screenheight,fullscreen)

