import pygame

WHITE = (255, 255, 255)


class Car(pygame.sprite.Sprite):
    def __init__(self, color, width, height, speed=0, image="crash.png"):
        super().__init__()

        self.invincible = False
        self.small = False
        self.double = False
        self.slowdown = False

        if image is None:
            self.image = pygame.Surface([width, height])
            self.image.fill(WHITE)
            self.image.set_colorkey(WHITE)
            self.width = width
            self.height = height
            self.color = color
            pygame.draw.rect(self.image, color, [0, 0, width, height])

        else:
            self.image = pygame.image.load(image)
            self.width = width
            self.height = height
            self.image = pygame.transform.scale(self.image, (width, height))

        self.rect = self.image.get_rect()
        self.speed = speed
        self.color = color

    def moveRight(self, pixels):
        self.rect.x += pixels

    def moveLeft(self, pixels):
        self.rect.x -= pixels

    def moveForward(self, speed):
        self.rect.y -= speed

    def moveBackward(self, player_car_speed):
        pixels = self.speed + player_car_speed
        self.rect.y += pixels

    def changeSpeed(self, new_speed):
        self.speed = new_speed

    def repaint(self, color):
        self.color = color
        # pygame.draw.rect(self.image, self.color, [0, 0, self.width, self.height])

    def resize(self, width, height):
        self.width = width
        self.height = height
        self.image = pygame.transform.scale(self.image, (width, height))

    def reimage(self, image_path):
        self.image = pygame.image.load(image_path)
        self.image = pygame.transform.scale(self.image, (self.width, self.height))

    def activate_invincibility(self, duration):
        self.invincible = True
        self.invincibility_duration = duration

    def update_invincibility(self):
        if self.invincible:
            self.invincibility_duration -= 1
            if self.invincibility_duration <= 0:
                self.invincible = False
                self.invincibility_duration = 300  # Reset the duration

    def activate_double(self, duration):
        self.double = True
        self.double_duration = duration  # Use the correct attribute

    def update_double(self):
        if self.double:
            self.double_duration -= 1
            if self.double_duration <= 0:
                self.double = False
                self.double_duration = 300  # Reset the duration for double power-up

    def activate_small(self, duration):
        self.small = True
        # pygame.draw.rect(self.image, self.color,  [0, 0, (self.width)/2, (self.height)/2])
        self.small_duration = duration  # Use the correct attribute

    def update_small(self):
        if self.small:
            self.small_duration -= 1
            if self.small_duration <= 0:
                self.small = False
                self.small_duration = 300  # Reset the duration for small power-up

    def activate_slowdown(self, duration):
        self.slowdown = True
        self.slowdown_duration = duration  # Use the correct attribute

    def update_slowdown(self):
        if self.slowdown:
            self.slowdown_duration -= 1
            if self.slowdown_duration <= 0:
                self.slowdown = False
                self.slowdown_duration = 300  # Reset the duration for slowdown power-up
