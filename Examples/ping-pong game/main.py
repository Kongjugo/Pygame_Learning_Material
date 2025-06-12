import pygame
import os
import random

# 게임 화면 설정
SCREEN_WIDTH = 800
SCREEN_HEGIHT = 600

# 색상 지정
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255, 0, 0)
ORANGE = (250, 170, 70)

# FPS 설정 (프레임 설정)
FPS = 60

# 초기화 
pygame.init()
pygame.font.init()
pygame.mixer.init()

# 파일 경로 설정
current_path = os.path.dirname(__file__)
assets_path = os.path.join(current_path, 'assets')

pygame.mixer.music.load(os.path.join(assets_path, 'bgm.mp3'))
pygame.mixer.music.play(-1)  # 무한 반복 재생

ping_sound = pygame.mixer.Sound(os.path.join(assets_path, 'ping.mp3'))
pong_sound = pygame.mixer.Sound(os.path.join(assets_path, 'pong.mp3'))

font = pygame.font.Font(os.path.join(assets_path, 'Pretendard-Medium.otf'))

# 화면 설정
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEGIHT))
pygame.display.set_caption("ping pong game")
pygame.display.set_icon()
clock = pygame.time.Clock()

# 기타 변수 설정
ball = pygame.Rect(SCREEN_WIDTH // 2, SCREEN_HEGIHT // 2, 12, 12)
ball_dx = random.choice([-3, 3])
ball_dy = 5

player = pygame.Rect(SCREEN_WIDTH // 2, SCREEN_HEGIHT - 40, 50, 15)
player_dx = 0

computer = pygame.Rect(SCREEN_WIDTH // 2,  40, 50, 15)

player_score = 0
computer_score = 0

# 공 리셋 함수
def reset_ball(center_x, center_y):
    global ball, ball_dx, ball_dy
    ball.x = center_x
    ball.y = center_y
    ball_dx = random.choice([-3, -2, -1, 1, 2, 3])
    ball_dy = 5

# 게임 리셋 함수
def reset_score():
    global player_score, computer_score
    player_score = 0
    computer_score = 0

# 이벤트 함수
def event():
    global player_dx

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                player_dx = -5
            elif event.key == pygame.K_RIGHT:
                player_dx = 5
        if event.type == pygame.KEYUP:
            if event.key in [pygame.K_LEFT, pygame.K_RIGHT]:
                player_dx = 0
    return False

# 게임 업데이트 함수
def update_game():
    global ball, ball_dx, ball_dy, player, player_dx, player_score, computer_score, computer

    # 공 이동
    ball.x = ball_dx + ball.x
    ball.y = ball_dy + ball.y

    # 공이 충돌한 경우
    if ball.left < 0 or ball.right > SCREEN_WIDTH:
        ball_dx = ball_dx * (-1)

    # 플레이어 이동 
    player.x = player.x + player_dx

    # 플레이어가 화면 밖으로 이동한 경우
    if player.left < 0:
        player.left = 0 # player_dx = 0
    if player.right > SCREEN_WIDTH:
        player.right = SCREEN_WIDTH # player_dx = 0
    
    # 컴퓨터(적) 이동
    if computer.centerx > ball.centerx:
        computer.x = computer.x - 3
    if computer.centerx < ball.centerx:
        computer.x = computer.x + 3
    
    # 공이 플레이어/컴퓨터에 부딪혔을 때
    if ball.colliderect(player):
        ball_dy = ball_dy * (-1)
        ball_dx = random.randint(-5, 5)
        ball.bottom = player.top
        ping_sound.play()

    if ball.colliderect(computer):
        ball_dy = ball_dy * (-1)
        ball.top = computer.bottom
        pong_sound.play()

    if ball.top < 0 :
        player_score = player_score + 1
        reset_ball(player.centerx, player.centery) 

    elif ball.bottom > SCREEN_HEGIHT :
        computer_score += 1
        reset_ball(computer.centerx, computer.centery)


#게임 메세지 출력 함수     
def show_message(text, color) :
    label = font.render(text, True, color)
    screen.blit(label, ((SCREEN_WIDTH - label.get_width()) // 2, (SCREEN_HEGIHT - label.get_height()) // 2))
    pygame.display.update()

#게임 그리기 함수
def draw() :
    #스크린 지정
    screen.fill(BLUE)

    #플레이어가 이겼을 경우
    if player_score == 5:
       show_message("승리", WHITE)
       reset_score()
       pygame.time.wait(2000)

    #적이 이겼을 경우
    elif computer_score == 5:
        show_message("패배", WHITE)
        reset_score()
        pygame.time.wait(2000)

    #아무 상황도 아닌경우 = 게임이 진행되고 있을때때
    else :
        pygame.draw.rect(screen, ORANGE, ball)
        pygame.draw.rect(screen, RED, player)
        pygame.draw.rect(screen, BLACK, enemy)

        #점선
        for x in range(0, SCREEN_WIDTH, 24) :
            pygame.draw.rect(screen, WHITE, [x, SCREEN_HEGIHT//2, 10, 10])

        #점수출력
        enemy_label = font.render(str(enemy_score), True, WHITE)
        screen.blit(enemy_label, (10, 220))

        player_label = font.render(str(player_score), True, WHITE)
        screen.blit(player_label, (10, 340))

    #게임 화면 업데이트
    pygame.display.flip()

#메인 함수
def main() :
    done = False 
    while not done :
        done = event()
        update_game()
        draw()
        clock.tick(FPS)
        
    pygame.quit()

#시작점을 알려주는 조건문
if __name__ == '__main__' :
    main()
