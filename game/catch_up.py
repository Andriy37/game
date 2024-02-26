from pygame import *
x1 = (100)
x2 = (300)
y1 = (100)
y2 = (300)

window = display.set_mode((700, 500))

display.set_caption("Доганялки ")

backround = transform.scale(image.load("fon.jpg"), (700, 500))   #створи вікно гри

game = True

while game:
    window.blit(backround,(0, 0))  #задай фон сцени

    for e in event.get():
        if e.type == QUIT:
            game = False


sprite1= transform.scale(
    image.load("smoll pak.jpg")
    (100, 100)
)

sprite2= transform.scale(
    image.load("pink.jpg")
    (100, 100)    
)
speed = 10 

run = True
clock = time.Clock()
FPS = 60

while run:
    window.blit(backround, (0, 0))
    window.blit(sprite1, (x1 , y1 ))
    window.blit(sprite2, (x2, y2))

    keys_presed = key.get_pressed()

    if keys_presed[K_LEFT] and x1>5:
        x1 -= speed
    if keys_presed[K_RIGHT] and x1<595:
        x1 += speed
    if keys_presed[K_UP] and x1>5:
        y1 -= speed
    if keys_presed[K_DOWN] and x1<395:
        y1 += speed

    if keys_presed[K_a] and x2>5:
        x2 -= speed
    if keys_presed[K_d] and x2<595:
        x2 += speed
    if keys_presed[K_w] and x2>5:
        y2 -= speed
    if keys_presed[K_s] and x2<395:
        y2 += speed


for e in event.get():
    if e.type == QUIT:
        run = False

display.update()
clock.tick(FPS)
#створи 2 спрайти та розмісти їх на сцені

#оброби подію «клік за кнопкою "Закрити вікно"»