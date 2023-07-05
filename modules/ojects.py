import pygame
from modules.level_map import screen


class Object:
    def __init__(self, x, y, width, height, image):
        self.hitbox = pygame.Rect(x, y, width, height)
        self.image = image
    
    def draw(self):
        #pygame.draw.rect(screen, (0,0,0),self.hitbox)
        screen.blit(self.image, (self.hitbox.x, self.hitbox.y))