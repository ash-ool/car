import random
from car import Car
from powerups import *
import sys

street_position = 0
class Label:
    def __init__(self, x, y, text, font=None, font_size=54, color=(255, 0, 0), flag=False):
        if font is None:
            self.font = pygame.font.SysFont("arial black", font_size)
        else:
            self.font = font
        self.text = self.font.render(text, True, color)
        self.position = (x, y)

    def update_text(self, text, color=(255, 0, 0)):
        self.text = self.font.render(text, True, color)

    def draw(self, screen):
        screen.blit(self.text, self.position)


def multi_player():
    pygame.init()
    from interface import interface

    background_image = pygame.image.load("Images/BG.jpg")
    gameover_image = pygame.image.load("Images/crash.png")

    GREEN = (20, 255, 140)
    BLACK = (0, 0, 0)
    GREY = (210, 210, 210)
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)
    RED2 = (220, 50, 100)
    PURPLE = (255, 0, 255)
    YELLOW = (255, 255, 0)
    CYAN = (0, 255, 255)
    BLUE = (100, 100, 255)

    colorList = (RED, RED2, GREEN, PURPLE, YELLOW, CYAN, BLUE, BLACK)

    SCREENWIDTH = 1000
    SCREENHEIGHT = 700

    size = (SCREENWIDTH, SCREENHEIGHT)
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption("Car Racing")

    image_list = ["Images/faisca.png", "Images/faisca2.png", "Images/faisca3.png"]

    # This will be a list that will contain all the sprites we intend to use in our game.
    all_sprites_list = pygame.sprite.Group()

    playerCar = Car(RED, 69, 150, image='Images/faiscamcqueen.png')
    playerCar.rect.x = 100
    playerCar.rect.y = 450

    playerCar2 = Car(RED2, 150, 150, image='Images/faiscamcqueen2.png')
    playerCar2.rect.x = 300
    playerCar2.rect.y = 450

    car1 = Car(PURPLE, 80, 130, 1, image="Images/faisca.png")
    car1.rect.x = 100
    car1.rect.y = -100

    car2 = Car(YELLOW, 80, 130, 2, image="Images/faisca2.png")
    car2.rect.x = 250
    car2.rect.y = -600

    car3 = Car(CYAN, 80, 130, 4, image="Images/faisca3.png")
    car3.rect.x = 400
    car3.rect.y = -300

    car4 = Car(BLUE, 80, 130, 5, image="Images/faisca.png")
    car4.rect.x = 550
    car4.rect.y = -900

    invincibility_power_up = InvincibilityPowerUp(YELLOW, 50, 50, 2, image="Images/shield.png")
    double_power_up = DoublePowerUp(GREEN, 50, 50, 2, image="Images/double.png")
    small_power_up = SmallPowerUp(RED, 50, 50, 2, image="Images/size_reduction.png")

    # Add the car to the list of objects
    all_sprites_list.add(playerCar, playerCar2)
    all_sprites_list.add(car1)
    all_sprites_list.add(car2)
    all_sprites_list.add(car3)
    all_sprites_list.add(car4)

    all_coming_cars = pygame.sprite.Group()
    all_coming_cars.add(car1)
    all_coming_cars.add(car2)
    all_coming_cars.add(car3)
    all_coming_cars.add(car4)

    # Allowing the user to close the window...
    carryOn = True
    playerCar_speed = 5
    playerCar2_speed = 5

    # Creating a time counter
    font = pygame.font.SysFont("arial black", 30)
    text = font.render("Time: ", True, (255, 255, 255), (0, 0, 0))
    pos_text = text.get_rect()
    pos_text.center = (550, 50)

    timer = 0
    time_second = 0

    score_font = pygame.font.SysFont("arial black", 30)
    pygame.font.SysFont("arial black", 70)

    score = 0

    power_up_caught = False
    active_power_up = None

    power_up_types = [invincibility_power_up, double_power_up, small_power_up]
    weights = [0.1, 0.1, 0.8]
    power_up = random.choices(power_up_types, weights)[0]
    power_up.rect.x = random.randint(100, 400)
    power_up.rect.y = -300
    all_sprites_list.add(power_up)

    interface_image_1 = pygame.image.load("Images/shield.png")
    interface_image_2 = pygame.image.load("Images/size_reduction.png")
    interface_image_3 = pygame.image.load("Images/double.png")
    interface_image_4 = pygame.image.load("Images/slow_down.png")

    winner = None

    clock = pygame.time.Clock()

    while carryOn:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        keys = pygame.key.get_pressed()

        # Player 1 controls
        if keys[pygame.K_LEFT] and playerCar.rect.x > 50:
            if not playerCar2.rect.colliderect(playerCar.rect.move(-5, 0)):
                playerCar.moveLeft(5)
        if keys[pygame.K_RIGHT] and playerCar.rect.x < 550:
            if not playerCar2.rect.colliderect(playerCar.rect.move(5, 0)):
                playerCar.moveRight(5)
        if keys[pygame.K_UP] and playerCar.rect.y > 0:
            if not playerCar2.rect.colliderect(playerCar.rect.move(0, -playerCar_speed)):
                playerCar.moveForward(playerCar_speed)
        if keys[pygame.K_DOWN] and playerCar.rect.y < SCREENHEIGHT - playerCar.rect.height:
            if not playerCar2.rect.colliderect(playerCar.rect.move(0, playerCar_speed)):
                playerCar.moveBackward(playerCar_speed)

        # Player 2 controls
        if keys[pygame.K_a] and playerCar2.rect.x > 70:
            if not playerCar.rect.colliderect(playerCar2.rect.move(-5, 0)):
                playerCar2.moveLeft(5)
        if keys[pygame.K_d] and playerCar2.rect.x < 390:
            if not playerCar.rect.colliderect(playerCar2.rect.move(5, 0)):
                playerCar2.moveRight(5)
        if keys[pygame.K_w] and playerCar2.rect.y > 0:
            if not playerCar.rect.colliderect(playerCar2.rect.move(0, -playerCar2_speed)):
                playerCar2.moveForward(playerCar2_speed)
        if keys[pygame.K_s] and playerCar2.rect.y < SCREENHEIGHT - playerCar2.rect.height:
            if not playerCar.rect.colliderect(playerCar2.rect.move(0, playerCar2_speed)):
                playerCar2.moveBackward(playerCar2_speed)

        if playerCar.small:
            playerCar.resize(69 / 2, 150 / 2)
        else:
            playerCar.resize(69, 150)

        if playerCar.slowdown:
            playerCar_speed = 1
        else:
            playerCar_speed = 5

        if playerCar2.small:
            playerCar2.resize(69 / 2, 150 / 2)
        else:
            playerCar2.resize(69, 150)

        if playerCar2.slowdown:
            playerCar2_speed = 1
        else:
            playerCar2_speed = 5

        all_sprites_list.update()
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
                    PC = random.randint(0, 3)
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
                elif power_up == small_power_up:
                    power_up.apply_power_up_3(playerCar)
                all_sprites_list.remove(power_up)

        if pygame.sprite.collide_rect(playerCar2, power_up):
            if not power_up_caught:
                active_power_up = power_up
                power_up_caught = True
                if power_up == invincibility_power_up:
                    power_up.apply_power_up_1(playerCar2)
                elif power_up == double_power_up:
                    power_up.apply_power_up_2(playerCar2)
                elif power_up == small_power_up:
                    power_up.apply_power_up_3(playerCar2)
                all_sprites_list.remove(power_up)

        if power_up_caught and random.random() < 0.001:  # Check probability only when power-up is caught
            power_up.rect.x = random.randint(100, 400)
            power_up.rect.y = random.randint(-600, -100)
            all_sprites_list.add(power_up)  # Re-add the power-up to the sprite group
            active_power_up = None
            power_up_caught = False  # Reset the flag

        all_sprites_list.update()

        playerCar.update_invincibility()
        playerCar.update_double()
        playerCar.update_small()
        playerCar.update_slowdown()

        for car in all_coming_cars:
            if not playerCar.invincible and pygame.sprite.collide_mask(playerCar, car) is not None:
                carryOn = False
                winner = "Player 2"
                pygame.draw.rect(screen, BLACK, [60, 0, 400, 500])

            if not playerCar2.invincible and pygame.sprite.collide_mask(playerCar2, car) is not None:
                carryOn = False
                winner = "Player 1"
                pygame.draw.rect(screen, BLACK, [60, 0, 400, 500])

        score_text = score_font.render(f"Score: {score}", True, (255, 255, 255), (0, 0, 0))
        score_rect = score_text.get_rect(center=(550, 100))
        screen.blit(score_text, score_rect)

        T = [0, 0]
        if playerCar.invincible:
            screen.blit(pygame.transform.scale(interface_image_1, (100, 100)), (730, 160))
            color = BLUE
            T.append(time_second)
        elif playerCar.small:
            screen.blit(pygame.transform.scale(interface_image_2, (100, 100)), (730, 160))
            color = RED
            T.append(time_second)
            playerCar.rect.width = 69 // 2
            playerCar.rect.height = 150 // 2
        elif playerCar.double:
            screen.blit(pygame.transform.scale(interface_image_3, (100, 100)), (730, 160))
            color = YELLOW
            T.append(time_second)
        elif playerCar.slowdown:
            screen.blit(pygame.transform.scale(interface_image_4, (100, 100)), (730, 160))
            color = GREEN
            T.append(time_second)
        else:
            T = [0, 0]
            color = RED

        if playerCar2.invincible:
            screen.blit(pygame.transform.scale(interface_image_1, (100, 100)), (730, 500))
            color2 = BLUE
            T.append(time_second)
        elif playerCar2.small:
            screen.blit(pygame.transform.scale(interface_image_2, (100, 100)), (730, 500))
            color2 = RED
            T.append(time_second)
            playerCar2.rect.width = 69 // 2
            playerCar2.rect.height = 150 // 2

        elif playerCar2.double:
            screen.blit(pygame.transform.scale(interface_image_3, (100, 100)), (730, 500))
            color2 = YELLOW
            T.append(time_second)

        elif playerCar2.slowdown:
            screen.blit(pygame.transform.scale(interface_image_4, (100, 100)), (730, 500))
            color2 = GREEN
            T.append(time_second)
        else:
            color2 = RED
            playerCar2.rect.width = 69
            playerCar2.rect.height = 150

        player1_text = Label(700, 100, "Player 1", font=None, font_size=54, color=RED)
        player1_text.draw(screen)

        player2_text = Label(700, 420, "Player 2", font=None, font_size=54, color=BLUE)
        player2_text.draw(screen)

        all_sprites_list.draw(screen)
        screen.blit(text, pos_text)

        all_sprites_list.update()

        if playerCar.invincible or playerCar.small or playerCar.double or playerCar.slowdown:
            pygame.draw.rect(screen, color, playerCar.rect, width=4)
        if playerCar2.invincible or playerCar2.small or playerCar2.double or playerCar2.slowdown:
            pygame.draw.rect(screen, color2, playerCar2.rect, width=4)

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

    # Display the time elapsed
    time_elapsed_text = font.render(f"Time Lived: {time_second} seconds", True, WHITE, BLACK)
    time_elapsed_rect = time_elapsed_text.get_rect(center=(SCREENWIDTH // 2, SCREENHEIGHT // 2))

    # Display the score
    score_text_gameover = score_font.render(f"Score: {score}", True, WHITE, BLACK)
    score_rect_gameover = score_text_gameover.get_rect(center=(SCREENWIDTH // 2, SCREENHEIGHT // 2 + 50))

    # Center the image on the screen
    gameover_rect = gameover_image.get_rect(center=(SCREENWIDTH // 2, SCREENHEIGHT // 2))
    screen.blit(gameover_image, gameover_rect)

    screen.blit(game_over_text, game_over_rect)
    screen.blit(play_again_text, play_again_rect)
    screen.blit(go_to_interface_text, go_to_interface_rect)
    screen.blit(time_elapsed_text, time_elapsed_rect)  # Display the time
    screen.blit(score_text_gameover, score_rect_gameover)
    if winner:
        winner_text = font.render(f"Winner: {winner}", True, WHITE, BLACK)
        winner_rect = winner_text.get_rect(center=(SCREENWIDTH // 2, SCREENHEIGHT // 2 + 150))
        screen.blit(winner_text, winner_rect)

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
                    multi_player()
                    inGameOverScreen = False
                elif event.key == pygame.K_n:
                    go_to_interface = True
                    inGameOverScreen = False

    if go_to_interface:
        interface()

    pygame.quit()
