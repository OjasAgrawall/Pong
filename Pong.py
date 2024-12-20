import pygame

pygame.init()

TEMP_SCREEN_WIDTH = 800
TEMP_SCREEN_HEIGHT = 600
NAME = "Pong"
bg = pygame.image.load("PongBackground.jpg")

screen = pygame.display.set_mode((TEMP_SCREEN_WIDTH, TEMP_SCREEN_HEIGHT), flags = pygame.RESIZABLE)
pygame.display.set_caption(NAME)

NUMBERFONT = pygame.font.Font("ataris-pong-score.otf", 40)
TEXTFONT = pygame.font.SysFont("Georgia", 40)

#Colours
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

#Paddles
PADDLE_WIDTH = 35
PADDLE_HEIGHT = 100


player1Y = 0
player1Score = 0
player1 = pygame.Rect((50, player1Y, PADDLE_WIDTH, PADDLE_HEIGHT))

player2X = screen.get_width() - 100
player2Y = 0
player2Score = 0
player2 = pygame.Rect((player2X, player2Y, PADDLE_WIDTH, PADDLE_HEIGHT))


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
    global player1, player2
    player1 = pygame.Rect((50, player1Y, PADDLE_WIDTH, PADDLE_HEIGHT))

    player2X = screen.get_width() - 100
    player2 = pygame.Rect((player2X, player2Y, PADDLE_WIDTH, PADDLE_HEIGHT))
    pygame.draw.rect(screen, WHITE, player1)
    pygame.draw.rect(screen, WHITE, player2)

#ball
BALL_RADIUS = 10
ball = pygame.Rect(screen.get_width()//2 - BALL_RADIUS, screen.get_height()//2 - BALL_RADIUS, BALL_RADIUS*2, BALL_RADIUS*2)
ball_x_speed = 4
ball_y_speed = 4

def ballMovement():
    global ball_x_speed, ball_y_speed, player2Score, player1Score
    ball.x += ball_x_speed
    ball.y += ball_y_speed

    if (ball.y + 2*BALL_RADIUS) >= screen.get_height() or ball.y <= 0:
        ball_y_speed *= -1

    if (ball.x + 2*BALL_RADIUS) >= screen.get_width():
        player1Score += 1
        ball.center = screen.get_width()//2, screen.get_height()//2
        ball_x_speed *= -1
        ball_y_speed *= -1

    if ball.x <= 0:
        player2Score += 1
        ball.center = screen.get_width()//2, screen.get_height()//2
        ball_x_speed *= -1
        ball_y_speed *= -1

def relativeBallSpeed():
    global ball_x_speed, ball_y_speed
    ball_speed_scale = 175
    if ball_x_speed < 0:
        ball_x_speed = -(screen.get_width() / ball_speed_scale)

    if ball_x_speed > 0:
        ball_x_speed = screen.get_width() / ball_speed_scale 

    if ball_y_speed < 0:
        ball_y_speed = -(screen.get_height() / ball_speed_scale) * 1.5

    if ball_y_speed > 0:
        ball_y_speed = screen.get_height() / ball_speed_scale * 1.5

def ballCollision():
    global ball_x_speed
    if ball.colliderect(player1):
        ball_x_speed *= -1
        #distance = (ball.left - player1.right)
        ball.x += 5

    if ball.colliderect(player2):
        ball_x_speed *= -1
        distance = (ball.right - player2.left)
        ball.x -= distance
        
def drawBall():
    pygame.draw.circle(screen, WHITE, ball.center, BALL_RADIUS) 

def drawCentreLine():
    SCREEN_MID = screen.get_width() / 2
    SCREEN_HEIGHT = screen.get_height()
    for y in range(0, SCREEN_HEIGHT, SCREEN_HEIGHT // 10):
        pygame.draw.rect(screen, WHITE, (SCREEN_MID - 2, y + 20, 4, (SCREEN_HEIGHT//20)))

def displayScore():
    player1_score_text = NUMBERFONT.render(str(player1Score), True, WHITE)
    player2_score_text = NUMBERFONT.render(str(player2Score), True, WHITE)

    screen.blit(player1_score_text, (screen.get_width()/2 - (screen.get_width()//20) - 10, 50))
    screen.blit(player2_score_text, (screen.get_width()/2 + (screen.get_width()//20) - 10, 50))
run = True
class Button():
    def __init__(self, text, x, y, width, height):
        self.text = text
        self.x = x
        self.y = y
        self.textX = x
        self.textY = y
        self.width = width
        self.height = height
        self.color = WHITE
        self.rounding = 0
        self.text_color = BLACK

        button_text = TEXTFONT.render(self.text, True, self.text_color)
        self.button_text = button_text
        button_rect = pygame.Rect(self.x, self.y, self.width, self.height)
        self.button_rect = button_rect
    
    def setColor(self, r, g, b):
        self.color = (r, g, b)
    
    def setTextColor(self, r, g, b):
        self.text_color = (r, g, b)
    
    def setRounding(self, n):
        self.rounding = n

    def draw(self):
        pygame.draw.rect(screen, self.color, self.button_rect, 0, self.rounding)
        pygame.draw.rect(screen, BLACK, self.button_rect, 2, self.rounding)

        screen.blit(self.button_text, (self.textX, self.textY))
        
def mainMenu():
    run = True
    global playButtonPressed, bg
    playButtonPressed = False
    while run:

        screen.fill(WHITE)

        bg = pygame.transform.scale(bg, (screen.get_width(), screen.get_height()))
        screen.blit(bg, (0,0))

        play_button = Button("Play", (screen.get_width()/2) - 100, (screen.get_height() - 300), 200, 80)
        play_button.textX = play_button.x + 58
        play_button.textY = play_button.y + 15

        play_button.setRounding(20)
        play_button.setColor(211,211,211)
        play_button.draw()

        exit_button = Button("Exit", (screen.get_width()/2) - 100, (screen.get_height() - 100), 200, 80)
        exit_button.textX = exit_button.x + 58
        exit_button.textY = exit_button.y + 15

        exit_button.setRounding(20)
        exit_button.setColor(211,211,211)
        exit_button.draw()

        mouse_pos = pygame.mouse.get_pos()

        if pygame.mouse.get_pressed()[0]:
            if play_button.button_rect.collidepoint(mouse_pos):
                playButtonPressed = True

            if exit_button.button_rect.collidepoint(mouse_pos):
                run = False

        if playButtonPressed:
            run = False
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        pygame.display.update()
    
    


def playButton():
    global SCREEN_BOTTOM, PADDLE_MOVE_SPEED
    TPS = 100
    delay = int(1000 / TPS)

    run = True
    while run:
        
        pygame.time.delay(delay)
        
        #reset screen 
        screen.fill(BLACK)

        # Get the bottom of the screen using the changing screen height
        SCREEN_BOTTOM = screen.get_height() - 100
        PADDLE_MOVE_SPEED = screen.get_height() / 150

        relativeBallSpeed()
        

        # movements
        paddleMovement()
        ballMovement()
        
        #collisions checks
        ballCollision()


        #actually draw onto the screen
        drawPaddles()
        drawBall()
        drawCentreLine()

        #Score
        displayScore()

        #if you want to leave you can
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        pygame.display.update()

mainMenu()
if playButtonPressed:
    playButton()

pygame.quit()