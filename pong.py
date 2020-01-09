import pygame
import time
pygame.init()

height,width = 400, 600
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)
radius = 10
game_over = False
window = pygame.display.set_mode((width,height))
pygame.display.set_caption("Ping Pong")
score = 0
score_font = pygame.font.SysFont("comicsansms", 35)
over_font = pygame.font.SysFont("comicsansms", 40)
difficulty=15
x1,y1 = 0,height-50
x_change=0
x2,y2 = 300,100
paddle_width, paddle_height = 150, 30
x2_change, y2_change = -5, -5
ball_size=10
clock = pygame.time.Clock()
while not game_over:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            game_over=True
        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_LEFT:
                x_change=-10
            if event.key==pygame.K_RIGHT:
                x_change=10
    x1+=x_change
    x2+=x2_change
    y2+=y2_change
    if x1<10 or x1>width-10-paddle_width:
        x_change=-x_change

    if x2>width-15 or x2<15:
        x2_change = -x2_change
    if  y2<ball_size:
        y2_change=-y2_change
    if y2>y1-ball_size:
        if x2<x1 or x2>x1+paddle_width:
            game_over=True
        elif x2>x1 and x2<x1+width:
            y2_change = -y2_change
            score+=1
            if x_change>0:
                x2_change+=7
                if x_change>10:
                    x_change=10
            else:
                x2_change-=7
                if x2_change<-10:
                    x2_change=-1
    
    window.fill(blue)
    pygame.draw.circle(window, green, [x2,y2], radius)
    pygame.draw.rect(window, red, [x1,y1,paddle_width,paddle_height])
    value = score_font.render("Your Score: " + str(score), True, yellow)
    window.blit(value, [0, 0])   
    pygame.display.update()
    clock.tick(difficulty)
game_over_msg = over_font.render("Game over",True,red)   
window.blit(game_over_msg,[width/2-200,height/2-40])  
pygame.display.update()
time.sleep(5)
pygame.quit()
quit()
