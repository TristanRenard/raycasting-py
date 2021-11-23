import pygame
class Material:
    """
    class pour géréer les matériaux du labyrinthe et leur couleur
    """
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
    """
    gère les collectibles du labyrinthe
    """
    def __init__(self,char,color):
        super().__init__(char,color)
        self.type="collectible"
        self.c=['0','1','2','3','4','5','6','7','8','9']
        self.collected=0

    def collect(self,x):
        self.collected+=1
        self.c.remove(x)