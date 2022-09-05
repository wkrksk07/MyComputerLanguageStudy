import pygame

pygame.init() #초기화

#화면 크기
screen_width = 1366
screen_height = 768
screen = pygame.display.set_mode((screen_width,screen_height))

#화면 타이틀
pygame.display.set_caption("코딩의 노예들")

# 배경 이미지 불러오기
background = pygame.image.load("C:/Users/VVIP/Documents/GitHub/MyComputerLanguageStudy/Python\Make the Game/PyGame_NadoCoding_2/Img/BackGround.png")

#Player 스프라이트 불러오기
Player = pygame.image.load("C:/Users/VVIP/Documents/GitHub/MyComputerLanguageStudy/Python\Make the Game/PyGame_NadoCoding_2/Img/Player.png")
Player_size = Player.get_rect().size #이미지 크기
Player_width = Player_size[0] #캐릭터 가로
Player_height = Player_size[1] #케릭터 세로
Player_x_pos = (screen_width / 2) - (Player_width/2) #화면 가로의 절반 크기에 해당하는 곳에 위치
Player_y_pos = screen_height - Player_height 

#이벤트 루프
running = True #게임이 진행중인가
while running:
    for event in pygame.event.get(): #어떤 이벤트가 발생했는가
        if event.type == pygame.QUIT: #창위 X = 닫기 눌렀을때
            running = False #게임 진행중 아님

    screen.blit(background,(0, 0)) #배경 그리기
    screen.blit(Player, (Player_x_pos,Player_y_pos))#캐릭터 그리기
    
    pygame.display.update()#게임화면호출

# 게임 종료
pygame.quit()