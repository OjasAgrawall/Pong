import pygame

pygame.init()

TEMP_SCREEN_WIDTH = 800
TEMP_SCREEN_HEIGHT = 600
NAME = "Pong"

screen = pygame.display.set_mode((TEMP_SCREEN_WIDTH, TEMP_SCREEN_HEIGHT), flags = pygame.RESIZABLE)
pygame.display.set_caption(NAME)


#Colours
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

#Paddles
PADDLE_WIDTH = 50
PADDLE_HEIGHT = 100


player1Y = 0

    
player2X = screen.get_width() - 100
player2Y = 0

def paddleMovement():
    global player1Y, player2Y
    key = pygame.key.get_pressed()
    if key[pygame.K_w] == True:
        player1Y -= PADDLE_MOVE_SPEED
        
    if key[pygame.K_s] == True:
        player1Y += PADDLE_MOVE_SPEED
        
    if key[pygame.K_o] == True:
        player2Y -= PADDLE_MOVE_SPEED
        
    if key[pygame.K_l] == True:
        player2Y += PADDLE_MOVE_SPEED
        
    if player1Y < 0:
            player1Y = 0
    if player1Y > SCREEN_BOTTOM:
            player1Y = SCREEN_BOTTOM
    
    if player2Y < 0:
            player2Y = 0
    if player2Y > SCREEN_BOTTOM:
            player2Y = SCREEN_BOTTOM

def drawPaddles():
    player1 = pygame.Rect((50, player1Y, PADDLE_WIDTH, PADDLE_HEIGHT))

    player2X = screen.get_width() - 100
    player2 = pygame.Rect((player2X, player2Y, PADDLE_WIDTH, PADDLE_HEIGHT))

    pygame.draw.rect(screen, WHITE, player1)
    pygame.draw.rect(screen, WHITE, player2)

def drawCentreLine():
    SCREEN_MID = screen.get_width() / 2
    SCREEN_HEIGHT = screen.get_height()
    for y in range(0, SCREEN_HEIGHT, SCREEN_HEIGHT // 10):
        pygame.draw.rect(screen, WHITE, (SCREEN_MID - 2, y + 20, 4, (SCREEN_HEIGHT//20)))


TPS = 100
delay = int(1000 / TPS)

run = True
while run:
    
    pygame.time.delay(delay)
    
    #reset screen 
    screen.fill((0, 0, 0))

    # Get the bottom of the screen using the changing screen height
    SCREEN_BOTTOM = screen.get_height() - 100
    PADDLE_MOVE_SPEED = (screen.get_height()) / 200

    # The two player paddle movements
    paddleMovement()

    #actually draw the paddles onto the screen
    drawPaddles()

    drawCentreLine()

    #if you want to leave you can
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    pygame.display.update()

pygame.quit()