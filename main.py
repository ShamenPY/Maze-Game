import pygame
BLACK = (0,0,0)



class App():

  def __init__(self):
    self.x = 30
    self.y = 30
    self.main()


  def draw_maze(self):
    # pygame.draw.line(self.screen, BLACK, [670, 540], [10, 0], 5)
    pygame.draw.line(self.screen, BLACK, [0, 457], [71, 457], 5)
    pygame.draw.line(self.screen, BLACK, [123, 540], [123, 477], 5) # linia w dol

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






  def create_screen(self):

    (width, height) = (670, 540)
    self.screen = pygame.display.set_mode((width,height))
    background_colour = (255,255,255)
    self.screen.fill(background_colour)
    self.draw_maze()
    pygame.display.flip()



  def main(self):

    self.create_screen()
    running = True
    color = (255,0,0)
    x = pygame.draw.rect(self.screen, color, pygame.Rect(self.x, self.y, 60, 60), 30)

    rect = pygame.Rect(x)



    while running:


      print(self.y)


      pygame.display.flip()




      ev = pygame.event.get()
      for event in ev:
        if event.type == pygame.MOUSEBUTTONUP:
          pos = pygame.mouse.get_pos()
          print(pos)
        if event.type == pygame.KEYDOWN:
          if event.key == pygame.K_LEFT:
            self.x -= 4
          if event.key == pygame.K_RIGHT:
            self.x += 4
          if event.key == pygame.K_UP:
            self.y -= 4
          if event.key == pygame.K_DOWN:
            self.y += 4
      pygame.display.flip()


      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          running = False



App = App()



