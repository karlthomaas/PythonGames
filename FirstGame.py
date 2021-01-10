import pygame

pygame.init()
x_res = 500
y_res = 500
win = pygame.display.set_mode((x_res, y_res))
pygame.display.set_caption('First vame v1.0')

x = 250
y = 500

width = 40
height = 60

vel = 10

isJump = False
jumpCount = 10
jumpingSpeed = 0.5

run = True
while run is True:
    # frame delay?
    pygame.time.delay(50)

    for event in pygame.event.get():    # checks is user did something
        if event.type == pygame.QUIT:   # if user clicks close
            run = False                 # ends the while run loop

    # gets the state of all keyboard buttons
    keys = pygame.key.get_pressed()

    if keys[pygame.K_a] and x > 0:
        x -= vel
    if keys[pygame.K_d] and x < x_res - width:
        x += vel

    if not (isJump):
        if keys[pygame.K_w] and y > 0:
            y -= vel
        if keys[pygame.K_s] and y < y_res - height:
            y += vel

        if keys[pygame.K_SPACE]:
            isJump = True
    else:
        #  jumpCount -= 1, gradually makes the y speed slower
        # 1. 10 * 10 * 0.5 = 50
        # 2. 9 * 9 * 0.5 = 40.5
        # 3. 8 * 8 * 0.5 = 32
        # until it be

        # jumpcount >= '-10', chose -10, because the
        # falling can follow the same formula
        # if the jumpCount goes below 0, then the opposite
        # y cords is going to happen

        if jumpCount >= -10:
            neg = 1

            if jumpCount < 0:
                neg = -1

            y -= (jumpCount ** 2) * jumpingSpeed * neg
            jumpCount -= 1

        else:
            isJump = False
            jumpCount = 10
    win.fill((0, 0, 0))
    # pygame draw function (surface (colour), (positon and dimensions)
    pygame.draw.rect(win, (255, 0, 0), (x, y, width, height))
    pygame.display.update()

pygame.quit()
