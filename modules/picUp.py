import pygame
from modules.hero import Hero

class Pickup():
    def __init__(self, x, y, width, height, color, id):
        self.hitbox = pygame.Rect(x, y, width, height)
        self.color = color
        self.id = id

    def draw(self, window):
        pygame.draw.rect(window, self.color, self.hitbox)
    
    def collide(self, player, drop_list, drop):
        if player.hitbox.colliderect(self.hitbox):
            drop_list.remove(drop)
            if self.id == 1:
                player.gift_count += 1
        

    def update(self, x_shift, y_shift):
        self.hitbox.x += x_shift
        self.hitbox.y += y_shift

    def next_lvl(self, player, dialog2):
        if player.gift_count == 3:
            dialog2()