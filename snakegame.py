import pygame
import time                    #needed to slow down the snake
from pygame.locals import *
from random import randint      #need to be cited for movement
import winsound                 #needed for inputting sound


#creating a class for the display of apples that is going to appear on screen
class Apple:
    x = 0                          
    y = 0
    step = 33               #determines the length in between the blocks
 
    def __init__(snake,x,y):
        snake.x = x * snake.step
        snake.y = y * snake.step
 
    def draw(snake, surface, image):
        surface.blit(image,(snake.x, snake.y)) 
 
#creating a class to input 
class Player:
    x = [0]
    y = [0]
    step = 33         #determines the length in between the blocks
    direction = 0    #determines the starting direction of snake, 0 here means it start from he left to right
    length =0       #determines the starting length of the snake
 
    MaxCount = 2      #determines the maximum update count, the more the value the faster it updates and the faster the snake moves
    Count = 0
 
    def __init__(snake, length):
       snake.length = length
       for i in range(0,500):
           snake.x.append(-50)   
           snake.y.append(-50)
 
       snake.x[1] = 1*20
       snake.x[2] = 2*20
 
    def update(snake):
 
        snake.Count = snake.Count + 1                   #1 represents the update count, the more the value the faster it updates and the faster the snake moves
        if snake.Count > snake.MaxCount:
 
                                                       #this is to update the previous position of the snake
            for i in range(snake.length-1,0,-1):
                snake.x[i] = snake.x[i-1]
                snake.y[i] = snake.y[i-1]
 
                                                         #this is to update the position of the head of the snake
            if snake.direction == 0:
                snake.x[0] = snake.x[0] + snake.step
            if snake.direction == 1:
                snake.x[0] = snake.x[0] - snake.step
            if snake.direction == 2:
                snake.y[0] = snake.y[0] - snake.step
            if snake.direction == 3:
                snake.y[0] = snake.y[0] + snake.step
 
            snake.Count = 0
 
 
    def moveRight(snake):               #shows the direction of the snake with the keys pressed
        snake.direction = 0
 
    def moveLeft(snake):
        snake.direction = 1
 
    def moveUp(snake):
        snake.direction = 2
 
    def moveDown(snake):
        snake.direction = 3 
 
    def draw(snake, surface, image):
        for i in range(0,snake.length):         #shows the initial length of snake 
            surface.blit(image,(snake.x[i],snake.y[i])) 
 
class Game:                                             #the logic used to determine the if the head of the snake collides with the body
    def isCollision(snake,x1,y1,x2,y2,bsize):           #the way it works is that it sees if coordinates (x1,y1) intersects with (x2,y2), it is a collision
        if x1 >= x2 and x1 <= x2 + bsize:               #bsize is the blocksize
            if y1 >= y2 and y1 <= y2 + bsize:
                return True
        return False
 
class App:
    windowWidth = 1000               #this controls the windows size when playing the game
    windowHeight = 800
    snake = 0
    apple = 0
 
    def __init__(snake):                        #this part keeps the snake running constantly
        snake._running = True
        snake._display_surf = None
        snake._image_surf = None
        snake._apple_surf = None
        snake.game = Game()
        snake.player = Player(3) 
        snake.apple = Apple(5,5)
 
    def on_init(snake):
        pygame.init()
        snake._display_surf = pygame.display.set_mode((snake.windowWidth,snake.windowHeight), pygame.HWSURFACE)
        pygame.display.set_caption('Snake Game')                   #title of game displayed when windows is opened
        snake._running = True
        snake._image_surf = pygame.image.load("whiteblock.jpg").convert()           #the image of both the apple and snake that is loaded from external image
        snake._apple_surf = pygame.image.load("whiteblock.jpg").convert()
 

 #logic of the game
        
    def on_loop(snake):                          
        snake.player.update()         
 
        
        for i in range(0,snake.player.length):                 #this part loops both if the snake eats the apple it increases the length and creates a new apple location
            if snake.game.isCollision(snake.apple.x,snake.apple.y,snake.player.x[i], snake.player.y[i],30):
                snake.apple.x = randint(2,9) * 33
                snake.apple.y = randint(2,9) * 33
                snake.player.length = snake.player.length + 1           #+1 is the addition of block size on the snake once it eats an apple
                winsound.PlaySound('bite.wav', winsound.SND_FILENAME)
                                                             #logic needed to see if the snake collides with itself, once collided it prints a phrase
        for i in range(2,snake.player.length):
            if snake.game.isCollision(snake.player.x[0],snake.player.y[0],snake.player.x[i], snake.player.y[i],30):
                print("You lose!")
                exit(0)                                                
        pass
 
    def on_render(snake):                                       #compulsory to render the image of apple and snake
        snake._display_surf.fill((0,0,0))
        snake.player.draw(snake._display_surf, snake._image_surf)
        snake.apple.draw(snake._display_surf, snake._apple_surf)
        pygame.display.flip()
 
 
    def on_execute(snake):
        if snake.on_init() == False:
            snake._running = False
 
        while( snake._running ):                     # this part is needed to allow the keys to be pressed to steer the snake
            pygame.event.pump()  
            keys = pygame.key.get_pressed() 
 
            if (keys[K_RIGHT]):
                snake.player.moveRight()
 
            if (keys[K_LEFT]):
                snake.player.moveLeft()
 
            if (keys[K_UP]):
                snake.player.moveUp()
 
            if (keys[K_DOWN]):
                snake.player.moveDown()
 
            snake.on_loop()
            snake.on_render()
 
            time.sleep (50.0 / 1000.0);  #slows down the snake

#compulsory to execute the game
if __name__ == "__main__" :
    theApp = App()
    theApp.on_execute()
