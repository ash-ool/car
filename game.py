import random
from car import Car
from powerups import *
import sys

street_position = 0


def car_racing():
    from interface import interface
    pygame.init()

    background_image = pygame.image.load("Images/BG.jpg")
    gameover_image = pygame.image.load("Images/crash.png")

    GREEN, BLACK, GREY, WHITE, RED, PURPLE, YELLOW, CYAN, BLUE = (20, 255, 140), (0, 0, 0), (210, 210, 210), (
        255, 255, 255), (255, 0, 0), (255, 0, 255), (255, 255, 0), (0, 255, 255), (100, 100, 255)
    colorList = (RED, GREEN, PURPLE, YELLOW, CYAN, BLUE, BLACK)

    SCREENWIDTH, SCREENHEIGHT = 1000, 700
    size = (SCREENWIDTH, SCREENHEIGHT)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Car Racing")

    clock = pygame.time.Clock()
    carryOn, playerCar_speed, timer, time_second, score = True, 5, 0, 0, 0

    image_list = ["Images/faisca.png", "Images/faisca2.png", "Images/faisca3.png", "Images/faisca4.png"]

    def initialize_car(color, width, height, speed, x, y, image):
        car = Car(color, width, height, speed, image=image)
        car.rect.x = x
        car.rect.y = y
        return car

    playerCar = initialize_car(RED, 69, 150, 0, 200, 300, 'Images/faiscamcqueen.png')
    car1 = initialize_car(PURPLE, 80, 130, 1, 100, -100, "Images/faisca.png")
    car2 = initialize_car(YELLOW, 80, 130, 2, 250, -600, "Images/faisca2.png")
    car3 = initialize_car(CYAN, 80, 130, 4, 400, -300, "Images/faisca3.png")
    car4 = initialize_car(BLUE, 80, 130, 5, 550, -900, "Images/faisca.png")

    invincibility_power_up = InvincibilityPowerUp(YELLOW, 50, 50, 2, image="Images/shield.png")
    double_power_up = DoublePowerUp(GREEN, 50, 50, 2, image="Images/double.png")
    small_power_up = SmallPowerUp(RED, 50, 50, 2, image="Images/size_reduction.png")
    slowdown_power_up = SlowdownPowerUp(BLUE, 50, 50, 2, image="Images/slow_down.png")

    all_sprites_list = pygame.sprite.Group(playerCar, car1, car2, car3, car4)
    all_coming_cars = pygame.sprite.Group(car1, car2, car3, car4)

    font = pygame.font.SysFont("arial black", 30)
    text = font.render("Time: ", True, (255, 255, 255), (0, 0, 0))
    pos_text = text.get_rect()
    pos_text.center = (800, 50)

    timer = 0
    time_second = 0
    score = 0
    power_up_caught = False
    active_power_up = None

    score_font = pygame.font.SysFont("arial black", 30)

    power_up_types = [invincibility_power_up, double_power_up, small_power_up, slowdown_power_up]
    weights = [0.1, 0.1, 0.1, 0.8]
    power_up = random.choices(power_up_types, weights)[0]
    #PC = random.randint(0, 3)
    # power_up = power_ups[PC]
    power_up.rect.x = random.randint(100, 400)
    power_up.rect.y = -300
    all_sprites_list.add(power_up)

    interface_image_1 = pygame.image.load("Images/shield.png")
    interface_image_2 = pygame.image.load("Images/size_reduction.png")
    interface_image_3 = pygame.image.load("Images/double.png")
    interface_image_4 = pygame.image.load("Images/slow_down.png")

    while carryOn:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and playerCar.rect.x > 50:
            playerCar.moveLeft(5)
        if keys[pygame.K_RIGHT] and playerCar.rect.x < 550:
            playerCar.moveRight(5)
        if keys[pygame.K_UP] and playerCar.rect.y > 0 and playerCar_speed < 10:
            playerCar_speed += 0.1
            playerCar.moveForward(playerCar_speed)
        if keys[pygame.K_DOWN] and playerCar.rect.y < SCREENHEIGHT - playerCar.rect.height and playerCar_speed > 0:
            playerCar_speed -= 0.1
            playerCar.moveBackward(playerCar_speed)
        if playerCar.slowdown:
            playerCar_speed = 1
        else:
            playerCar_speed = 5

        if playerCar.small:
            playerCar.resize(69 / 2, 150 / 2)
        else:
            playerCar.resize(69, 150)

        pygame.draw.rect(screen, BLACK, [0, 0, SCREENWIDTH, 5])  # Top barrier
        pygame.draw.rect(screen, BLACK, [0, SCREENHEIGHT - 5, SCREENWIDTH, 5])  # Bottom barrier

        pygame.draw.rect(screen, GREY, [50, 0, 600, 700])

        line_positions = [200, 350, 500]
        line_y_positions = [-50, -150, -250, -350, -450, -550, -650]
        global street_position
        street_position += 3.1
        street_position %= 700

        yellow_line_y = 0
        yellow_line_y_end = SCREENHEIGHT
        pygame.draw.line(screen, YELLOW, [50, yellow_line_y], [50, yellow_line_y_end], 10)
        pygame.draw.line(screen, YELLOW, [650, yellow_line_y], [650, yellow_line_y_end], 10)

        # Draw the lines with the updated position
        for x in line_positions:
            for i, y in enumerate(line_y_positions):
                y_pos = (y + street_position) % 700  # Calculate the position

                # Draw lines above and below the screen to create a continuous effect
                pygame.draw.line(screen, WHITE, [x, y_pos], [x, y_pos + 60], 7)
                pygame.draw.line(screen, WHITE, [x, y_pos - 700], [x, y_pos - 640], 7)
                pygame.draw.line(screen, WHITE, [x, y_pos + 700], [x, y_pos + 760], 7)

        if timer < 60:
            timer += 1
        else:
            time_second += 1
            text = font.render("Time: " + str(time_second), True, (255, 255, 255), (0, 0, 0))
            timer = 0

        for car in all_coming_cars:
            car.moveBackward(playerCar_speed)
            if car.rect.y >= SCREENHEIGHT:

                if power_up == double_power_up and active_power_up == double_power_up:
                    score += 200
                else:
                    score += 100
                car.repaint(random.choice(colorList))
                car.changeSpeed(random.randint(1, 5))
                Si = (random.randrange(60, 100) / 100)
                car.resize(80 * Si, 150 * Si)
                car.rect.y = random.randint(-300, 0)
                all_coming_cars.add(car)
                car.reimage(random.choice(image_list))

        power_up.moveBackward(playerCar_speed)

        if power_up.rect.y >= SCREENHEIGHT:
            if pygame.sprite.collide_rect(playerCar, power_up):
                power_up.apply_power_up(playerCar)
            else:
                if random.random() < 0.003:
                    active_power_up = None
                    power_up.rect.x = random.randint(100, 400)
                    power_up.rect.y = random.randint(-600, -100)

        if pygame.sprite.collide_rect(playerCar, power_up):
            if not power_up_caught:
                active_power_up = power_up
                power_up_caught = True
                if power_up == invincibility_power_up:
                    power_up.apply_power_up_1(playerCar)
                elif power_up == double_power_up:
                    power_up.apply_power_up_2(playerCar)
                elif power_up == slowdown_power_up:
                    power_up.apply_power_up_4(playerCar)
                elif power_up == small_power_up:
                    power_up.apply_power_up_3(playerCar)
                all_sprites_list.remove(power_up)

        if power_up_caught and random.random() < 0.001:
            power_up.rect.x = random.randint(100, 400)
            power_up.rect.y = random.randint(-600, -100)
            all_sprites_list.add(power_up)
            active_power_up = None
            power_up_caught = False

        all_sprites_list.update()

        playerCar.update_invincibility()
        playerCar.update_double()
        playerCar.update_small()
        playerCar.update_slowdown()

        for car in all_coming_cars:
            if not playerCar.invincible and pygame.sprite.collide_mask(playerCar, car) is not None:
                carryOn = False
                pygame.draw.rect(screen, BLACK, [60, 0, 400, 500])

        score_text = score_font.render(f"Score: {score}", True, (255, 255, 255), (0, 0, 0))
        score_rect = score_text.get_rect(center=(800, 100))
        screen.blit(score_text, score_rect)

        T = [0, 0]
        if playerCar.invincible:
            screen.blit(pygame.transform.scale(interface_image_1, (100, 100)), (800, 300))
            color = BLUE
            T.append(time_second)
        elif playerCar.small:
            screen.blit(pygame.transform.scale(interface_image_2, (100, 100)), (800, 300))
            color = PURPLE
            T.append(time_second)

            playerCar.rect.width = 69 // 2
            playerCar.rect.height = 150 // 2
        elif playerCar.double:
            screen.blit(pygame.transform.scale(interface_image_3, (100, 100)), (800, 300))
            color = YELLOW
            T.append(time_second)
        elif playerCar.slowdown:
            screen.blit(pygame.transform.scale(interface_image_4, (100, 100)), (800, 300))
            color = GREEN
            T.append(time_second)
        else:
            color = RED
            playerCar.rect.width = 69
            playerCar.rect.height = 150

        screen.blit(text, pos_text)

        all_sprites_list.update()

        all_sprites_list.draw(screen)

        if playerCar.invincible or playerCar.small or playerCar.double or playerCar.slowdown:
            pygame.draw.rect(screen, color, playerCar.rect, width=4)

        pygame.display.flip()

        screen.blit(background_image, (0, 0))

        clock.tick(60)

    font = pygame.font.SysFont("arial black", 50)
    game_over_text = font.render("Game Over", True, WHITE, BLACK)
    game_over_rect = game_over_text.get_rect(center=(SCREENWIDTH // 2, SCREENHEIGHT // 2 - 100))
    play_again_text = font.render("Play Again (Y)", True, WHITE, BLACK)
    play_again_rect = play_again_text.get_rect(center=(SCREENWIDTH // 2, SCREENHEIGHT // 2 + 100))
    go_to_interface_text = font.render("Go to Interface (N)", True, WHITE, BLACK)
    go_to_interface_rect = go_to_interface_text.get_rect(center=(SCREENWIDTH // 2, SCREENHEIGHT // 2 + 200))

    time_elapsed_text = font.render(f"Time Lived: {time_second} seconds", True, WHITE, BLACK)
    time_elapsed_rect = time_elapsed_text.get_rect(center=(SCREENWIDTH // 2, SCREENHEIGHT // 2))

    score_text_gameover = score_font.render(f"Score: {score}", True, WHITE, BLACK)
    score_rect_gameover = score_text_gameover.get_rect(center=(SCREENWIDTH // 2, SCREENHEIGHT // 2 + 50))

    gameover_rect = gameover_image.get_rect(center=(SCREENWIDTH // 2, SCREENHEIGHT // 2))
    screen.blit(gameover_image, gameover_rect)

    screen.blit(game_over_text, game_over_rect)
    screen.blit(play_again_text, play_again_rect)
    screen.blit(go_to_interface_text, go_to_interface_rect)
    screen.blit(time_elapsed_text, time_elapsed_rect)
    screen.blit(score_text_gameover, score_rect_gameover)
    pygame.display.flip()

    inGameOverScreen = True
    go_to_interface = False

    while inGameOverScreen:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_y:
                    car_racing()
                    inGameOverScreen = False
                elif event.key == pygame.K_n:
                    go_to_interface = True
                    inGameOverScreen = False

    if go_to_interface:
        interface()

    pygame.quit()
