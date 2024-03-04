#створи гру "Лабіринт"!
from pygame import *
import pygame
from pygame.sprite import _Group

x1 = (100)
x2 = (300)
y1 = (100)
y2 = (300)

window = display.set_mode((700, 500))
pygame.init()
display.set_caption("Доганялки ")

backround = transform.scale(image.load("background.jpg"), (700, 500))  #створи вікно гри

game = True

#mysik
mixer.init()
mixer
while game:
    window.blit(backround,(0, 0))  #задай фон сцени

    for e in event.get():
        if e.type == QUIT:
            game = False


run = True
clock = time.Clock()
FPS = 60

class GameSprite(sprite.Sprite)
    def __init__ (self, player_image, player_x, player_y, player_speed)
        super().__init__()
        self.image =  transform.scale(image.load(player_image), (65, 65))
        self.speed = player_speed
        self.rect = self.image.get_rect()
        self.rect.x = player_x
        self.rect.y = player_y
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
display.update()
clock.tick(FPS)