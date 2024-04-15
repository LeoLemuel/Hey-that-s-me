import pygame

class Game:
    def __init__(self, width, higth):
        pygame.init()
        self.width = width
        self.higth = higth
        self.screen = pygame.display.set_mode((self.width, self.higth))
        pygame.display.set_caption("---In The Edge Of Darkness---")
        self.clock = pygame.time.Clock()
        self.running = True
        self.dark_knight = DarkKnight(self ,0 ,685)

        self.background_img = pygame.image.load("dark background.jpg")

        self.ghost = Ghost(self , 1400, 685)


        while self.running:
            self.clock.tick(60)
            self.screen.blit(self.background_img, (0, 0))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.dark_knight.move(-10, "left")
                    elif event.key == pygame.K_RIGHT:
                        self.dark_knight.move(10, "right")
                    elif event.key == pygame.K_SPACE:
                        self.dark_knight.start_sword_hit()

                elif event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                        self.dark_knight.stop_moving()
                    if event.key == pygame.K_SPACE:
                        self.dark_knight.stop_sword_hit()



            self.dark_knight.update()
            self.ghost.update()
            pygame.display.update()




class DarkKnight:
    def __init__(self, game, x, y):
        self.x = x
        self.y = y
        self.change_x = 0
        self.direction = "right"
        self.game = game
        self.standard_looking_right_img = pygame.image.load("Knight stand without Background small.png")
        self.sword_hit_looking_right_img = pygame.image.load("Knight hit without background small.png")
        self.standard_looking_left_img = pygame.image.load("Knight stand without Background small, left.png")
        self.sword_hit_looking_left_img = pygame.image.load("Knight hit without background small. left.png")
        self.current_img = self.standard_looking_right_img

    def move(self, speed, direction):
        self.change_x = speed
        self.direction = direction
        if direction == "left":
            self.current_img = self.standard_looking_left_img
        elif direction == "right":
            self.current_img = self.standard_looking_right_img

    def update(self):
        self.x += self.change_x
        if self.x < 0:
            self.x = 0
        #elif self.x > 1350:
        #    self.x = 1350
        elif self.x > self.game.width - self.current_img.get_width():
            self.x = self.game.width - self.current_img.get_width()
        self.game.screen.blit(self.current_img, (self.x, self.y))

    def start_sword_hit(self):
        if self.direction == "left":
            self.current_img = self.sword_hit_looking_left_img
        elif self.direction == "right":
            self.current_img = self.sword_hit_looking_right_img

    def stop_sword_hit(self):
        if self.direction == "left":
            self.current_img = self.standard_looking_left_img
        elif self.direction == "right":
            self.current_img = self.standard_looking_right_img


    def stop_moving(self):
        self.change_x = 0
        self.stop_sword_hit()




class Ghost:
    def __init__(self, game, x, y):
        self.x = x
        self.y = y
        self.game = game
        self.speed = 5
        self.direction = -1
        self.ghost_looking_right_img = pygame.image.load("Ghost without background, small, looking right.png")
        self.ghost_looking_left_img = pygame.image.load("Ghost without background small, looking left.png")
        self.current_img = self.ghost_looking_left_img





    def update(self):
        self.x += self.speed * self.direction

        if self.x <= 0:
            self.direction = 1  # Wechsel die Richtung nach rechts
            self.current_img = self.ghost_looking_right_img
        elif self.x + self.current_img.get_width() >= self.game.width:
            self.direction = -1  # Wechsel die Richtung nach links
            self.current_img = self.ghost_looking_left_img

        self.game.screen.blit(self.current_img, (self.x, self.y))






if __name__ == "__main__":
    game = Game(1700, 900)
