import pygame 

# 게임 스크린 크기 
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# RGB 값 색상 지정
Black = (0, 0, 0)
White = (255, 255, 255)
Red = (255, 0, 0)
Green = (0, 255, 0)
Blue = (0, 0, 255)
Pink = (255, 192, 203)

# 초기화 
pygame.init()

# Window Name 설정
pygame.display.set_caption("My Game")

# Window 크기 정의
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# Screen Update
clock = pygame.time.Clock()

# ball
ball_x = int(SCREEN_WIDTH/2)
ball_y = int(SCREEN_HEIGHT/2)
ball_dx = 4
ball_dy = 4
ball_size = 40 

# 게임 반복 구간
done = False
while not done: # While True
    # Event 반복 구간
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        
    # 게임 로직 구간
    ball_x += ball_dx
    ball_y += ball_dy
    
    # 공이 스크린을 벗어난 경우
    if (ball_x + ball_size) > SCREEN_WIDTH or (ball_x - ball_size) <  0:
        ball_dx = ball_dx * (-1)
    if (ball_y + ball_size) > SCREEN_HEIGHT or (ball_y - ball_size) <  0:
        ball_dy = ball_dy * (-1)


    # 화면 삭제 구간

    # 스크린 채우기 
    screen.fill(White)

    # 화면 그리기
    pygame.draw.circle(screen, Black, [ball_x, ball_y], ball_size, 4)

    # 화면 업데이트
    pygame.display.flip()

    # 초당 업데이트 횟수
    clock.tick(60)

# 게임 종료
pygame.quit()
