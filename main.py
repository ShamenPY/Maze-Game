import pygame

BLACK = (0, 0, 0)
colors = ['black']
mouse = pygame.image.load("mouse.gif")

bg_img = pygame.image.load("background.png")
bg = pygame.transform.scale(bg_img, (900,600))
wall1 = pygame.image.load("wall.png")
clock = pygame.time.Clock()
clock.tick(60)
class App():

    def __init__(self):
        self.mouseX = 50
        self.mouseY = 50
        (width, height) = (900, 600)
        self.screen = pygame.display.set_mode((width, height))
        self.main()

        # self.rect = mouse.get_rect(center=(self.mouseX / 2, self.mouseY / 2))

    def draw_maze(self):

        self.screen.blit(wall1, (0, 0))
        self.screen.blit(wall1, (122, 476))
        self.screen.blit(wall1, (122, 354))





        # collide = pygame.Rect.colliderect(mouse, colors)

    def create_screen(self):
        self.screen.blit(bg,(0,0))
        self.screen.blit(mouse, (self.mouseX, self.mouseY))



    def main(self):

        self.create_screen()

        running = True
        while running:


            self.draw_maze()

            pygame.display.flip()

            ev = pygame.event.get()
            for event in ev:
                if event.type == pygame.MOUSEBUTTONUP:
                    pos = pygame.mouse.get_pos()
                    print(pos)

            for event in ev:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        self.mouseX -= 4
                    if event.key == pygame.K_RIGHT:
                        self.mouseX += 4
                    if event.key == pygame.K_UP:
                        self.mouseY -= 4
                    if event.key == pygame.K_DOWN:
                        self.mouseY += 4

            self.create_screen()
            # pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False


App = App()
