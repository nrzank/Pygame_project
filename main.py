import pygame

clock = pygame.time.Clock() # ВВодим время игры
pygame.init()    # вызываем экран (окошко)
screen = pygame.display.set_mode((618, 359))   # размер полотны в пиксельях
pygame.display.set_caption('Pygame Nur game')   #   игры
icon = pygame.image.load('image/squirtle_icon.png')  # иконка игры
pygame.display.set_icon(icon)  # ВВоение иконки в дисплей
bg = pygame.image.load('image/qwerty.png').convert_alpha() # фон
bgx = 0 # Кординаты х фона
ghost = pygame.image.load('image/q2.png').convert_alpha() # Vrag
ghost_x = 620


gameplay = True

#bgsound = pygame.mixer.Sound('sounds/Deformed pixel music - P.S. See under foot.mp3') #музыка
#bgsound.play() #проигрывание музыки
walk_left = [
    pygame.image.load('image/Player/1.png').convert_alpha(),
    pygame.image.load('image/Player/2.png').convert_alpha(),
    pygame.image.load('image/Player/3.png').convert_alpha(),
    pygame.image.load('image/Player/4.png').convert_alpha(),

]   #анимация персонажа, хождение в лево
walk_right = [ 
    pygame.image.load('image/Player/5.png').convert_alpha(),
    pygame.image.load('image/Player/6.png').convert_alpha(),
    pygame.image.load('image/Player/7.png').convert_alpha(),
    pygame.image.load('image/Player/8.png').convert_alpha(),
]   #анимация персонажа, хождение в право

ghost_list_ingame = []

playrsped = 5   #скорость хождение персонажа в пиксельях
playerx = 150   #координаты персонажа по х
anim = 0   # анимация персонажа
playery = 250   #координаты персонажа у
isjump = False   #прыжок вверх начинается
jump_count = 8    #размер прыжка в пиксельях


ghost_timer = pygame.USEREVENT + 1
pygame.time.set_timer(ghost_timer, 2500)

label = pygame.font.Font('fonts/RubikBubbles-Regular.ttf', 40)
lose_label = label.render('You lose!', False, (187, 188, 189))
restart_label = label.render('Play again', False, (115, 132, 149))
restart_label_rect = restart_label.get_rect(topleft=(180, 200))

bullet = pygame.image.load('image/bullet.png').convert_alpha()
bullets = []
running = True    #хождение персонажа
while running:     #Основной цикл

    keys = pygame.key.get_pressed()
    screen.blit(bg, (bgx, 0))  #анимация заднего фона
    screen.blit(bg, (bgx + 618, 0))   #вводение заденго фона в экран

    if gameplay:
        player_rect = walk_left[0].get_rect(topleft=(playerx, playery))


        if ghost_list_ingame:
            for (i, el) in enumerate(ghost_list_ingame):
                screen.blit(ghost, el)
                el.x -= 10

                if el.x < 10:
                    ghost_list_ingame.pop(i)


                if player_rect.colliderect(el):
                    gameplay = False




        #цикл персонажа влево и вправо
        if keys[pygame.K_LEFT]:
            screen.blit(walk_left[anim], (playerx, playery))
        else:
            screen.blit(walk_right[anim], (playerx, playery))    #цикл персонажа начало и конец

        if keys[pygame.K_LEFT] and playerx > 50:  #назначение хождение в лево
            playerx -= playrsped
        elif keys[pygame.K_RIGHT] and playerx < 200:    #назначение хождение
            playerx += playrsped
        if anim == 3:
            anim = 0
        else:
            anim +=1

            bgx -= 2
            if bgx == -618:
                bgx = 0
                if keys[pygame.K_b]:
                    bullets.append(bullet.get_rect(topleft=(playerx + 30, playery + 10)))

                    if bullets:
                        for el in bullets:
                            screen.blit(bullet, (el.x, el.y))





        if not isjump:
            if keys[pygame.K_SPACE]:
                isjump = True
        else:
            if jump_count >= -8:
                if jump_count > 0:
                    playery -= (jump_count ** 2) / 2
                else:
                    playery += (jump_count ** 2) / 2


                jump_count -= 1
            else:
                isjump = False
                jump_count = 8
    else:
        screen.fill((87, 88, 89))
        screen.blit(lose_label, (180, 100))
        screen.blit(restart_label, restart_label_rect)

        mouse = pygame.mouse.get_pos()
        if restart_label_rect.collidepoint(mouse) and pygame.mouse.get_pressed()[0]:
            gameplay = True
            playerx = 150
            ghost_list_ingame.clear()

    #команда закрытия окна с игрой с нажатием крестика
    pygame.display.update()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        if event.type == ghost_timer:
            ghost_list_ingame.append(ghost.get_rect(topleft=(620, 250)))



    clock.tick(15) #  анимация персонажа в секундах