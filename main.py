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
wall1 = pygame.image.load("wall.png")
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
        self.mouseX = 500
        self.mouseY = 500
        (width, height) = (900, 600)
        self.screen = pygame.display.set_mode((width, height))
        self.mouserect = mouse.get_rect(center=(self.mouseX/2,self.mouseY/2))
        self.main()

    def draw_maze(self):

        self.screen.blit(wall1, (722, 354))
        self.wall1rect = wall1.get_rect(center=(722, 354))
        self.screen.blit(wall2, (244, 232))
        self.wall2rect = wall2.get_rect(center=(244, 232))
        self.screen.blit(wall3, (354, 354))
        self.wall3rect = wall3.get_rect(center=(354, 354))
        self.screen.blit(wall4, (476, 354))
        self.wall4rect = wall4.get_rect(center=(476,354))
        self.screen.blit(wall5, (844, 354))#518 720
        self.wall5rect = wall5.get_rect(center=(844, 354))
        self.screen.blit(wall6, (122, 232))
        self.wall6rect = wall6.get_rect(center=(122, 232))
        self.screen.blit(wall7, (122, 476))
        self.wall7rect = wall7.get_rect(center=(122, 476))
        self.screen.blit(wall8, (122, 354))
        self.wall8rect = wall8.get_rect(center=(122, 354))
        self.screen.blit(wall1, (122, 0))
        self.wall9rect = wall1.get_rect(center=(122,0))


        self.screen.blit(wall10, (476, 110))#//#
        self.wall10rect = wall10.get_rect(center=(476, 110))
        self.screen.blit(wall11, (476, -12))
        self.wall11rect = wall11.get_rect(center=(476, -12))
        self.screen.blit(wall12, (720, -12))
        self.wall12rect = wall12.get_rect(center=(720, -12))
        self.screen.blit(wall13, (720, 110))
        self.wall13rect = wall13.get_rect(center=(720, 110))
        self.screen.blit(wall14, (842, 110))
        self.wall14rect = wall14.get_rect(center=(842, 110))
        self.screen.blit(wall15, (842, -12))
        self.wall15rect = wall15.get_rect(center=(842, -12))





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
            self.mouserect = mouse.get_rect(center=(self.mouseX, self.mouseY))

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
            self.collide1 = pygame.Rect.colliderect(self.mouserect, self.wall1rect)
            if self.collide1:
                print("mysz dotknęła scianę")
            self.collide2 = pygame.Rect.colliderect(self.mouserect, self.wall2rect)
            if self.collide2:
                print("mysz dotknęła scianę")
            self.collide3 = pygame.Rect.colliderect(self.mouserect, self.wall3rect)
            if self.collide3:
                print("mysz dotknęła scianę")
            self.collide4 = pygame.Rect.colliderect(self.mouserect, self.wall4rect)
            if self.collide4:
                print("mysz dotknęła scianę")
            self.collide5 = pygame.Rect.colliderect(self.mouserect, self.wall5rect)
            if self.collide5:
                print("mysz dotknęła scianę")
            self.collide6 = pygame.Rect.colliderect(self.mouserect, self.wall6rect)
            if self.collide6:
                print("mysz dotknęła scianę")
            self.collide7 = pygame.Rect.colliderect(self.mouserect, self.wall7rect)
            if self.collide7:
                print("mysz dotknęła scianę")
            self.collide8 = pygame.Rect.colliderect(self.mouserect, self.wall8rect)
            if self.collide8:
                print("mysz dotknęła scianę")
            self.collide9 = pygame.Rect.colliderect(self.mouserect, self.wall9rect)
            if self.collide9:
                print("mysz dotknęła scianę")
            self.collide10 = pygame.Rect.colliderect(self.mouserect, self.wall10rect)
            if self.collide10:
                print("mysz dotknęła scianę")
            self.collide11 = pygame.Rect.colliderect(self.mouserect, self.wall11rect)
            if self.collide11:
                print("mysz dotknęła scianę")
            self.collide12 = pygame.Rect.colliderect(self.mouserect, self.wall12rect)
            if self.collide12:
                print("mysz dotknęła scianę")
            self.collide13 = pygame.Rect.colliderect(self.mouserect, self.wall13rect)
            if self.collide13:
                print("mysz dotknęła scianę")
            self.collide14 = pygame.Rect.colliderect(self.mouserect, self.wall14rect)
            if self.collide14:
                print("mysz dotknęła scianę")
            self.collide15 = pygame.Rect.colliderect(self.mouserect, self.wall15rect)
            if self.collide15:
                print("mysz dotknęła scianę")






            # pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False


App = App()
