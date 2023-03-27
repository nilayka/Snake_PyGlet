from pyglet import image
from pyglet import app
from pyglet.window import Window
from pyglet.window import key
from pyglet import clock
from pyglet import text
from random import randint
import pandas

# make a window and keep it on
window_size = 500

window = Window(window_size, window_size)


@window.event
def on_draw():
    window.clear()
    # draw some text
    label.draw()
    # draw some food
    draw_square(fd_x, fd_y, cell_size, colour=(255, 0, 0, 0))

    # draw the snake
    for cords in tail:
        draw_square(cords[0], cords[1], cell_size, colour=(50, 50, 255, 0))
    draw_square(snk_x, snk_y, cell_size)


def draw_square(x, y, size, colour=(0, 0, 255, 0)):
    # draw a square
    img = image.create(size, size, image.SolidColorImagePattern(colour))
    img.blit(x, y)


def place_food():
    global fd_x, fd_y
    fd_x = randint(0, (window.width // cell_size) - 1) * cell_size
    fd_y = randint(0, (window.height // cell_size) - 1) * cell_size


@window.event
def on_key_press(symbol, modifiers):
    global snk_dx, snk_dy
    if symbol == key.UP:
        if snk_dy == 0:
            snk_dx = 0
            snk_dy = cell_size
    elif symbol == key.DOWN:
        if snk_dy == 0:
            snk_dx = 0
            snk_dy = -cell_size
    elif symbol == key.LEFT:
        if snk_dx == 0:
            snk_dx = -cell_size
            snk_dy = 0
    elif symbol == key.RIGHT:
        if snk_dx == 0:
            snk_dx = cell_size
            snk_dy = 0


def update(dt):
    global snk_x, snk_y, text_content, label, game_over, speed

    # check if the game is over
    if game_over:
        return

    # move the snake
    snk_x += snk_dx
    snk_y += snk_dy

    # grow the tail if the snake eats the food
    tail.append((snk_x, snk_y))
    if snk_x == fd_x and snk_y == fd_y:
        place_food()
        print(fd_x, fd_y)
        speed += 10
    else:
        tail.pop(0)

    # keep in window bounds
    if snk_x < 0:
        snk_x = window.width
    elif snk_x + cell_size > window.width:
        snk_x = 0
    elif snk_y < 0:
        snk_y = window.height
    elif snk_y + cell_size > window.height:
        snk_y = 0

    # print the score
    text_content = text_score + str(len(tail) - 1)
    label = text.Label(text_content,
                       font_name='Times New Roman',
                       font_size=font_size,
                       x=window_size // 100, y=window.height,
                       anchor_x='left', anchor_y='top')

    # check for collision with tail
    if (snk_x, snk_y) in tail[:len(tail) - 1]:
        print("Game Over")
        print("Score: " + str(len(tail) - 1))
        game_over = True


cell_size = 10

snk_dx, snk_dy, speed = 0, 0, 10
snk_x = window.width // cell_size // 2 * cell_size
snk_y = window.height // cell_size // 2 * cell_size

fd_x = randint(0, (window.width // cell_size) - 1) * cell_size
fd_y = randint(0, (window.height // cell_size) - 1) * cell_size

tail = [(snk_x, snk_y)]

font_size = 18
text_score = "Score: "
text_content = text_score + str(len(tail) - 1)
label = text.Label(text_content,
                   font_name='Times New Roman',
                   font_size=font_size,
                   x=window_size // 100, y=window.height,
                   anchor_x='left', anchor_y='top')

game_over = False
clock.schedule_interval(update, 1 / speed)
app.run()
