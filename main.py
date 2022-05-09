import pygame
import time
pygame.init()

win_jpg = pygame.image.load("winimg.jpg")
winimg = pygame.transform.scale(win_jpg,(900,600))
win = pygame.image.load("winbutton.png")

bg_img = pygame.image.load("background.png")
bg = pygame.transform.scale(bg_img, (900,600))

mouse_img = pygame.image.load("mouse.png")
mouse = pygame.transform.scale(mouse_img,(100, 100))

font = pygame.font.Font(None, 90)
black = (0, 0, 0)
wintext = font.render("YOU WON!", False,black)



class App():

    def __init__(self):

        (width, height) = (900, 600)
        self.screen = pygame.display.set_mode((width, height))

        self.mouseX = 500  # You starting game from x:500, y:500 coordinates
        self.mouseY = 500

        self.mask = pygame.mask.from_surface(mouse)
        self.rect = pygame.mask.Mask.get_rect(self.mask)
        self.mouserect = mouse.get_rect(center=(self.mouseX / 2, self.mouseY / 2))
        self.rect.center = self.mouseX/2, self.mouseY/2  # Rect of mouse is needed for check collide mouse with walls
        self.main()


    def draw_maze(self):

        for i in range(1, 16):
            globals()[f"wall{i}"] = pygame.image.load("wall.png") #setting image for wall between 1 for 15
        self.screen.blit(wall1, (722, 354))
        self.screen.blit(wall2, (230, 232))
        self.screen.blit(wall3, (354, 354))
        self.screen.blit(wall3, (354, 354))
        self.screen.blit(wall4, (476, 354))
        self.screen.blit(wall3, (354, 354))
        self.screen.blit(wall5, (844, 354))
        self.screen.blit(wall6, (122, 232))
        self.screen.blit(wall7, (122, 476))
        self.screen.blit(wall8, (122, 354))
        self.screen.blit(wall9, (122, 0))
        self.screen.blit(wall10, (476, 110))
        self.screen.blit(wall11, (476, -12))
        self.screen.blit(wall12, (720, -12))
        self.screen.blit(wall13, (720, 110))
        self.screen.blit(wall14, (842, 110))
        self.screen.blit(wall15, (842, -12))
        self.screen.blit(win,(50,448))

        self.wall1rect = wall1.get_rect(center=(730, 362))
        self.wall2rect = wall2.get_rect(center=(238, 240))
        self.wall3rect = wall3.get_rect(center=(362, 362))
        self.wall4rect = wall4.get_rect(center=(484,362))
        self.wall5rect = wall5.get_rect(center=(852, 362))
        self.wall6rect = wall6.get_rect(center=(130, 240))
        self.wall7rect = wall7.get_rect(center=(130, 484))
        self.wall8rect = wall8.get_rect(center=(130, 362))
        self.wall9rect = wall1.get_rect(center=(130,8))
        self.wall10rect = wall10.get_rect(center=(484, 118))
        self.wall11rect = wall11.get_rect(center=(484, -4))
        self.wall12rect = wall12.get_rect(center=(728, -4))
        self.wall13rect = wall13.get_rect(center=(728, 118))
        self.wall14rect = wall14.get_rect(center=(850, 118))
        self.wall15rect = wall15.get_rect(center=(850, -4))
        self.winrect = win.get_rect(center=(32, 430))


    def draw_bg_and_mouse(self):
        """


        She incessantly gives us background and
        image of mouse with new coordinates

        """
        self.screen.blit(bg,(0,0))
        self.screen.blit(mouse, (self.mouseX, self.mouseY))


    def win(self):
        """

        This function is when you win the game

        """

        self.screen.blit(winimg, (0, 0))
        self.screen.blit(wintext, (250, 50))
        pygame.display.flip()
        time.sleep(300)


    def collidecheck(self):

        """

        checking collide mouse with walls and mouse with cheese

        """

        self.collidewin = pygame.Rect.colliderect(self.mouserect, self.winrect) # Collide mouse with walls #
        for i in range(1, 15):
            self.collide = pygame.Rect.colliderect(self.mouserect, eval("self.wall" + str(i) + "rect"))
            if self.collide:
                self.mouseX = 500
                self.mouseY = 500
            elif self.collidewin: # Collide mouse with cheese #
                running = False
                self.win()
    def events_handling(self):
        """

        This function is checking
        do you clicking key left, right, down or up.

        """

        ev = pygame.event.get()
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

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

    def main(self):
        """

        function main have a loop, which elicit all function needed to the game
        """

        self.draw_bg_and_mouse()

        running = True
        while running:
            self.mouserect = mouse.get_rect(center=(self.mouseX, self.mouseY))
            self.draw_bg_and_mouse()
            self.draw_maze()       # Drawing walls
            self.collidecheck()    # Here is Checking do mouse isn't colliding with walls

            pygame.display.flip()

            self.events_handling()



App = App()
