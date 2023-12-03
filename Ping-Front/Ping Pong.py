from pygame import *

# нам нужны такие картинки:
img_1 = "racket.png" # рокетка 1
img_2 = "racket2.png" # рокетка 2
img_Ball = "Ball.png" # мяч
img_Back = "Back.png" # фон


# класс-родитель для других спрайтов
class GameSprite(sprite.Sprite):
  # конструктор класса
    def __init__(self, player_image, player_x, player_y, size_x, size_y, player_speed):
        # Вызываем конструктор класса (Sprite):
        sprite.Sprite.__init__(self)

        # каждый спрайт должен хранить свойство image - изображение
        self.image = transform.scale(image.load(player_image), (100, 100))
        self.speed = player_speed

        # каждый спрайт должен хранить свойство rect - прямоугольник, в который он вписан
        self.rect = self.image.get_rect() 
        self.rect.x = player_x
        self.rect.y = player_y
 
  # метод, отрисовывающий героя на окне
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))

# класс главного игрока
class Player(GameSprite):
    # метод для управления спрайтом стрелками клавиатуры
    def update_r(self):
        keys = key.get_pressed()
        if keys[K_UP] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[K_DOWN] and self.rect.y < win_height - self.rect.height:
            self.rect.y += self.speed
            
    def update_1(self):
        keys = key.get_pressed()
        if keys[K_w] and self.rect.y > 0:
            self.rect.y -= self.speed
        if keys[K_s] and self.rect.y < win_height - self.rect.height:
            self.rect.y += self.speed
            
    # метод для управления спрайтом ботом
    def update_bot(self, ball):
        if ball.rect.y < self.rect.y:
            self.rect.y -= self.speed
        if ball.rect.y > self.rect.y + self.rect.height:
            self.rect.y += self.speed


win_width = 600
win_height = 500
display.set_caption("Пин Понг")
window = display.set_mode((win_width, win_height))
background = transform.scale(image.load(img_Back), (win_width, win_height))

game = True
finish = False
clock = time.Clock()
FPS = 120

racket = Player(img_1, 30, 200, 400, 1000, 10)
racket2 = Player(img_2, 520, 200, 400, 1000, 10)
ball = GameSprite(img_Ball, 200, 200, 4, 50, 50)

font.init()
font = font.Font(None, 35)
lose1 = font.render('Игрок 1 проиграл!', True, (180, 0, 0))
lose2 = font.render('Игрок 2 проиграл!', True, (180, 0, 0))

speed_x = 3
speed_y = 3

while game:
    # событие нажатия на кнопку Закрыть
    for e in event.get():
        if e.type == QUIT:
            game = False

    if finish != True:
        racket.update_1()
        racket2.update_bot(ball)
        ball.update()
        # обновляем фон
        window.blit(background,(0,0))
        ball.rect.x += speed_x
        ball.rect.y += speed_y
        if sprite.collide_rect(racket, ball) or sprite.collide_rect(racket2, ball):
            speed_x *= -1
            speed_y *= 1
        if ball.rect.y > win_height-50 or ball.rect.y < 0:
            speed_y *= -1

        if ball.rect.x < 0:
            finish = True
            window.blit(lose1, (200, 200))
            game_over = True

        if ball.rect.x > win_width:
            finish = True
            window.blit(lose2, (200, 200))
            game_over = True

        racket.reset()
        racket2.reset()
        ball.reset()
    
    display.update()
    clock.tick(FPS)