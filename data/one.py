# 4월 9일자 
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

# 게임 반복 구간
done = False
while not done: # While True
    # Event 반복 구간
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        
    # 게임 로직 구간

    # 화면 삭제 구간

    # 스크린 채우기 
    screen.fill(White)

    # 화면 그리기
    pygame.draw.line(screen, Red, [50, 50], [500, 50], 4) #선
    
    pygame.draw.rect(screen, Blue, [50, 200, 150, 150], 4) #사각형

    pygame.draw.polygon(screen, Green, [[350, 200], [350, 250], [450, 350]], 4) #다각형

    pygame.draw.circle(screen, Black, [150, 450], 60, 4) #원

    pygame.draw.ellipse(screen, Pink, [250, 400, 200, 100], 4) #타원

    # 폰트 선택 (폰트, 크기, 두껍게, 이탤릭)
    font = pygame.font.SysFont('FixeSys', 20, False, False)

    text = font.render('Made By Kim Seong Ju', True, Black)
    screen.blit(text, [500, 400])

    # 화면 업데이트
    pygame.display.flip()

    # 초당 업데이트 횟수
    clock.tick(60)

# 게임 종료
pygame.quit()
