import pygame

BLACK = (0, 0, 0)
colors = ['black']
mouse_img = pygame.image.load("mouse.png")
mouse = pygame.transform.scale(mouse_img,(100, 100))


bg_img = pygame.image.load("background.png")
bg = pygame.transform.scale(bg_img, (900,600))
wall1 = pygame.image.load("wall.png")
wall2 = pygame.image.load("wall.png")
wall3 = pygame.image.load("wall.png")
wall4 = pygame.image.load("wall.png")
wall5 = pygame.image.load("wall.png")
wall6 = pygame.image.load("wall.png")
wall7 = pygame.image.load("wall.png")
wall8 = pygame.image.load("wall.png")
wall9 = pygame.image.load("wall.png")
wall10 = pygame.image.load("wall.png")
wall11 = pygame.image.load("wall.png")
wall12 = pygame.image.load("wall.png")
wall13 = pygame.image.load("wall.png")
wall14 = pygame.image.load("wall.png")
wall15 = pygame.image.load("wall.png")


clock = pygame.time.Clock()
clock.tick(5)
class App():

    def __init__(self):
        self.mouseX = 50
        self.mouseY = 50
        (width, height) = (900, 600)
        self.screen = pygame.display.set_mode((width, height))
        self.mouserect = mouse.get_rect(center=(self.mouseX,self.mouseY))
        self.main()

    def draw_maze(self):

        self.screen.blit(wall1, (722, 354))
        self.screen.blit(wall2, (244, 232))
        self.screen.blit(wall3, (354, 354))
        self.screen.blit(wall4, (476, 354))
        self.screen.blit(wall5, (844, 354))#598 720
        self.screen.blit(wall6, (122, 232))
        self.screen.blit(wall7, (122, 476))
        self.screen.blit(wall8, (122, 354))
        self.screen.blit(wall9, (122, 0))
        # self.wall9rect = wall9.get_rect(center=(61,0))


        self.screen.blit(wall10, (476, 110))#//#
        self.screen.blit(wall11, (476, -12))
        self.screen.blit(wall12, (720, -12))
        self.screen.blit(wall13, (720, 110))
        self.screen.blit(wall14, (842, 110))
        self.screen.blit(wall15, (842, -12))

        self.collide = pygame.Rect.colliderect(self.mouserect, self.wall9rect)

        if self.collide:
            print("mysz dotknęła scianę")

    def create_screen(self):
        self.screen.blit(bg,(0,0))
        self.screen.blit(mouse, (self.mouseX, self.mouseY))



    def main(self):

        self.create_screen()

        running = True
        while running:
            print(self.mouserect)

            self.create_screen()


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




            # pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False


App = App()
