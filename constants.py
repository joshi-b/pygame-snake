"""
constants.py
defined constants + init pygame
"""
import pygame
from os import path

FPS = 30
SPEED = 5
SIZE_OF_SBLOCK = 15

# Colours
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (11, 140, 19)
RED = (255, 0, 0)
SAND = (245, 238, 223)
GREY = (128, 127, 131)

# Screen Dimensions
WIDTH = 800
HEIGHT = 600

img_dir = path.join(path.dirname(__file__), 'img')

# intialize pygame
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH+10, HEIGHT+10))
pygame.display.set_caption('SSSnake')
clock = pygame.time.Clock()
font_nm = pygame.font.match_font('times')

# load game graphics
apple_img = pygame.image.load(path.join(img_dir, "apple.png")).convert_alpha()
snake_head_img = pygame.image.load(path.join(img_dir, "snake_head.png")).convert_alpha()
icon_img = pygame.image.load(path.join(img_dir, "icon.jpg")).convert_alpha()


pygame.display.set_icon(icon_img)