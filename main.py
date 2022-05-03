import pygame
BLACK = (0,0,0)
colors = ['black']
mouse = pygame.image.load("mouse.gif")


class App():

  def __init__(self):
    self.mouseX = 50
    self.mouseY = 50
    self.main()
    self.rect = mouse.get_rect(center=(self.mouseX/2,self.mouseY/2))




  def draw_maze(self):

    background_colour = (255,255,255)
    self.screen.fill(background_colour)
    # pygame.draw.line(self.screen, BLACK, [670, 540], [10, 0], 5)

    pygame.draw.line(self.screen, BLACK, [0, 457], [71, 457], 5)
    pygame.draw.line(self.screen, BLACK, [123, 540], [123, 477], 5)
    pygame.draw.line(self.screen, BLACK, [174, 457], [259, 457], 5)
    pygame.draw.line(self.screen, BLACK, [174, 540], [123, 477], 5)
    pygame.draw.line(self.screen, BLACK, [222, 457], [222, 500], 5)
    pygame.draw.line(self.screen, BLACK, [317, 457], [388, 457], 5)
    pygame.draw.line(self.screen, BLACK, [458, 457], [670, 457], 5)
    pygame.draw.line(self.screen, BLACK, [123, 150], [123, 380], 5)
    pygame.draw.line(self.screen, BLACK, [123, 380], [180, 150], 5)
    pygame.draw.line(self.screen, BLACK, [123, 150], [180, 150], 5)
    pygame.draw.line(self.screen, BLACK, [71, 380], [0, 380], 5)
    pygame.draw.line(self.screen, BLACK, [123, 315], [44, 315], 5)
    pygame.draw.line(self.screen, BLACK, [44, 315], [44, 230], 5)
    pygame.draw.line(self.screen, BLACK, [0, 230], [44, 230], 5)
    pygame.draw.line(self.screen, BLACK, [222, 380], [222, 153], 5)
    pygame.draw.line(self.screen, BLACK, [123, 180], [71, 180], 5)
    pygame.draw.line(self.screen, BLACK, [80, 230], [123, 310], 5)
    pygame.draw.line(self.screen, BLACK, [220, 377], [190, 377], 5)

    self.screen.blit(mouse,(self.mouseX,self.mouseY))
    # collide = pygame.Rect.colliderect(mouse, colors)


  def create_screen(self):
    (width, height) = (670, 540)
    self.screen = pygame.display.set_mode((width, height))
    pygame.display.flip()


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

      pygame.display.flip()

      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          running = False



App = App()



