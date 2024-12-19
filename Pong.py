import pygame

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), flags = pygame.RESIZABLE)


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

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    pygame.display.update()

pygame.quit()