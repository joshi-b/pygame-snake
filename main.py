"""
main.py
game loop
"""

import pygame
import constants as c
import sprites 
import random

# functions
def text_to_screen(msg, color, size, x, y):
    # write text to screen
    font = pygame.font.Font(c.font_nm, size)
    text_surf = font.render(msg, True, color)
    text_rect = text_surf.get_rect()
    text_rect.center = (x, y)
    c.screen.blit(text_surf, text_rect)

def start_screen():
    while True:
        c.screen.fill(c.SAND)
        c.screen.blit(c.start_screen_img, [10, 70])
        text_to_screen("\u2192 Eat the apples to get bigger", c.BROWN, 27, c.WIDTH/2-10, 100)
        text_to_screen("\u2192 Don't run into anything", c.BROWN, 27, c.WIDTH/2-37, 140)
        text_to_screen("\u2192 Use arrow keys to move", c.BROWN, 27, c.WIDTH/2-27,180)
        text_to_screen("Press SPACE to play", c.BROWN, 32, c.WIDTH/2, c.HEIGHT/2+180) 
        pygame.display.update()
        
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    initGame()
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

def initGame():
    # initialize sprites 
    global all_sprites
    global snake 
    global enemies
    global foods

    all_sprites = pygame.sprite.Group()
    foods = pygame.sprite.Group()

    snake = sprites.Player()
    all_sprites.add(snake)

    food = sprites.Food()
    foods.add(food)
    all_sprites.add(food)

    gameLoop()

# game loop
def gameLoop():
    game = True
    gameOver = False
    while game:
        # fps
        c.clock.tick(c.FPS)
        
        # game over screen
        while gameOver == True:
            c.screen.fill(c.SAND)
            text_to_screen("Game Over!", c.BROWN, 60, c.WIDTH/2, (c.HEIGHT/2)-70)
            text_to_screen("\u2192 Press P to play again", c.GREEN, 25, (c.WIDTH/2)-2, c.HEIGHT/2)
            text_to_screen("\u2192 Press Q to QUIT", c.GREEN, 25, (c.WIDTH/2)-30, c.HEIGHT/2+40)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameOver = False
                        game = False
                    if event.key == pygame.K_p:
                        initGame()
                if event.type == pygame.QUIT:
                    gameOver = False
                    game = False

        # process input
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                game = False
        
        # if snake touches edges, game over!
        if snake.rect.right >= c.WIDTH or snake.rect.left < 0 or snake.rect.top < 0 or snake.rect.bottom >= c.HEIGHT:
            gameOver = True

        all_sprites.update()
        c.screen.fill(c.SAND)
        all_sprites.draw(c.screen)

        # snake length
        head = []
        head.append(snake.rect.x)
        head.append(snake.rect.y)
        snake.posList.append(head)

        if len(snake.posList) > snake.length:
            del snake.posList[0]

        # if snake runs over itself, game over!
        for i in snake.posList[:-1]:
                if i == head:
                        gameOver = True

        # draw snake length and tail
        for i in snake.posList[:-2]:
            pygame.draw.rect(c.screen, c.GREEN, [i[0], i[1],c.SIZE_OF_SBLOCK, c.SIZE_OF_SBLOCK])

        # check for collisions
        collision = pygame.sprite.spritecollide(snake, foods, True)
        if collision:
            snake.collision()
            food = sprites.Food()
            foods.add(food)
            all_sprites.add(food)

        # draw border
        for x in range(0, c.WIDTH+6, 5):
            pygame.draw.rect(c.screen, c.BROWN, [x, 0, 5, 5])
            pygame.draw.rect(c.screen, c.BROWN, [x, c.HEIGHT+5, 5, 5])
        for x in range(0, c.HEIGHT+5, 5):
            pygame.draw.rect(c.screen, c.BROWN, [0, x, 5, 5])
            pygame.draw.rect(c.screen, c.BROWN, [c.WIDTH+5, x, 5, 5])

        # update screen with score
        text_to_screen("Score: " + str(snake.score), c.BLACK, 24, 70, 40)

        pygame.display.update()

    pygame.quit()
    quit()

start_screen()
