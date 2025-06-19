import pygame
import os
import random

#게임 설정
SCREEN_WIDTH = 900
SCREEN_HEIGHT= 700
FPS = 60

#색상 지정
WHITE = (255,255,255)
SEA = (80,180,220)
GROUND = (140,120,40)
DARK_GROUND = (70,60,20)

#경로 설정
current_path = os.path.dirname(__file__)
assets_path = os.path.join(current_path, 'assets')

#게임에 필요한 전역변수들
menu_on = True
score = 0
pipe_pos = 0 

#게임 초기화 함수
def init_game() :
    global fish_img, swim_sound, font, bgm_player
    fish_img = pygame.image.load(os.path.join(assets_path, "fish.png"))
    swim_sound = pygame.mixer.Sound(os.path.join(assets_path, "swim.wav"))
    font = pygame.font.Font(os.path.join(assets_path, "NanumGothicCoding-Bold.ttf"), 34)
    pygame.mixer.music.load(os.path.join(assets_path, "bgm.mp3"))
    bgm_player = False

#1. 물고기에 관련된 함수
#물고기 초기화 함수
def init_fish() :
    return [250, 250, 0] #물고기의 y값, 물고기의 dy값, 점수

#물고기 업데이트 함수
def update_fish(fish) :
    fish[1] = fish[1] + 0.5
    fish[0] = fish[0] + fish[1] #fish.y = fish.y + fish.dy

    #위 벽과 충돌했을때 멈추게 하는 코드
    if fish[0] <= 0: 
        fish[0] = 0

    #아래 벽과 충돌했을때 멈추게 하는 코드
    if fish[0] + fish_img.get_height() > SCREEN_HEIGHT :
        fish[0] = SCREEN_HEIGHT - fish_img.get_height() 
        fish[1] = 0 

    #dy값이 20이 넘어가면 고정:
        if fish[1] > 20:
            fish[1] = 20

#물고기 수영 함수
def swim(fish) :
    fish[1] = -10
    swim_sound.play()

#물고기 그림 그리는 함수
def draw_fish(screen, fish) :
    screen.blit(fish_img, (250, fish[0]))

# 파이프 생성
def create_pipe() :
    lpipe = pygame.image.load(os.path.join(assets_path, "pipe01.png"))
    spipe = pygame.image.load(os.path.join(assets_path, random.choice(["pipe02.png", "pipe03.png", "pipe04.png", "pipe05.png", "pipe06.png"])))

    if random.randint(0, 1) == 1:
        return [SCREEN_WIDTH, -2, lpipe, SCREEN_WIDTH, SCREEN_HEIGHT - spipe.get_height() - 50, spipe] 
        # [lpipe x좌표, lpipe y좌표, lpipe 이미지, spipe x좌표, spipe y좌표, spipe 이미지]  
    else:
        return [SCREEN_WIDTH, SCREEN_HEIGHT - lpipe.get_height() + 2, lpipe, SCREEN_WIDTH, -2, spipe] 
        # [lpipe x좌표, lpipe y좌표, lpipe 이미지, spipe x좌표, spipe y좌표, spipe 이미지]

# 파이프 업데이트
def update_pipe(pipes) :
    for i in range(len(pipes)):
        pipes[i][0] -= 4
        pipes[i][3] -= 4

# 파이프 그리기
def draw_pipe(screen, pipes) :
    for pipe in pipes:
        screen.blit(pipe[2], (pipe[0], pipe[1]))
        screen.blit(pipe[5], (pipe[3], pipe[4]))

# 파이프 충돌 체크
def check_crash(fish, pipes) :
    fx, fy = 250, fish[0]
    fw, fh = fish_img.get_width(), fish_img.get_height()
    for p in pipes:
        for px, py, pipe_img in [(p[0], p[1], p[2]), (p[3], p[4], p[5])]:
            pw, ph = pipe_img.get_width(), pipe_img.get_height()
            if (px + pw > fx) and (px < fx + fw) and (py < fy + fh) and (py + ph > fy):
                return True
    return False

# 이벤트 처리 함수
def process_events(fish, pipes) :
    global menu_on, score, bgm_player

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            return True 
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if menu_on:
                    score = 0 
                    pipes.clear() # 리스트에 아무것도 없도록 초기화
                    pipes.append(create_pipe()) # 파이프 리스트 생성
                    menu_on = False
                    fish[0], fish[1] = 250, 0 # 물고기 초기화
                    if not bgm_player:
                        pygame.mixer.music.play(-1)
                        bgm_player = True
                else:
                    swim(fish)
    return False

# 게임 로직
def update_logic(fish, pipes):
    global score, menu_on, pipe_pos
    update_fish(fish)
    update_pipe(pipes)  

    # 파이프가 왼쪽으로 이동하면서 벽에 부딪힌 경우 -> 파이프 제거
    if pipes[0][3] + fish_img.get_width() <= 0:
        pipes.pop(0)
        pipe_pos = random.randrange(200, 400, 4)
    
    # 파이프가 새로 생긴 경우
    if pipes[-1][3] <= pipe_pos:
        pipes.append(create_pipe())
        score += 1

    # 물고기와 파이프 충돌 체크
    if check_crash(fish, pipes):
        pygame.mixer.music.stop()
        menu_on = True

# 게임 화면 그리기
def draw_text(screen, text, x, y, color):
    text_obj = font.render(text, True, color)
    text_rect = text_obj.get_rect(center=(x, y))
    screen.blit(text_obj, text_rect)

def display_menu(screen):
    center_x, center_y = SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2
    rect = pygame.Rect(center_x - 220, center_y - 50, 440, 110)
    pygame.draw.rect(screen, GROUND, rect)
    draw_text(screen, "Press Space to Start", center_x, center_y, DARK_GROUND)

def display_frame(screen, fish, pipes):
    screen.fill(SEA)
    pygame.draw.rect(screen, GROUND, (0, SCREEN_HEIGHT-50, SCREEN_WIDTH, 50))
    draw_fish(screen, fish)
    draw_pipe(screen, pipes)
    draw_text(screen, f"Score: " + str(score), 100, 30, WHITE)

def main():
    global menu_on, score, pipe_pos
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Fish Game by School Class")
    clock = pygame.time.Clock()

    init_game()
    fish = init_fish()
    pipes = []

    done = False
    while not done:
        done = process_events(fish, pipes)
        if menu_on:
            display_menu(screen)
        else:
            update_logic(fish, pipes)
            display_frame(screen, fish, pipes)
        
        pygame.display.flip()
        clock.tick(FPS)

    pygame.quit()

if __name__ == "__main__":
    main()