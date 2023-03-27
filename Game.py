from pyglet import image
from pyglet import app
from pyglet.window import Window
from pyglet.window import key
from pyglet import clock
from pyglet import text

from Snake import Piton
from Color import Color
from Food import Food
from  random import randint

class Game(Window):
    def __init__(self, snake=None, snake_loc=None, window_size=800, score_label="Score:", font_size=18, interval=10):
        super().__init__(window_size, window_size)
        self.__window_size = window_size
        self.__score_label = text.Label(
            score_label,
            font_name='Times New Roman',
            font_size= font_size,
            x=window_size // 100, y=super().window.height,
            anchor_x='left', anchor_y='top'
        )
        self.__snake = snake
        self.__snake_loc = snake_loc
        if not self.__snake:
            self.__snake = Piton()
            if not self.__snake_loc:
                x = super().window.width // self.__snake.get_cell_size() // 2 * self.__snake.get_cell_size()
                y = super().window.height // self.__snake.get_cell_size() // 2 * self.__snake.get_cell_size()
                self.__snake_loc = (x, y)
        self.__snake.set_location(self.__snake_loc)
        self.__snake.grow()
        self.__food = Food()
        self.__game_over = False
        self.__interval = interval

    def place_food(self):
        self.__food.set_location((
            randint(0, (super().window.width // self.__food.cell_size) - 1) * self.__food.cell_size,
            randint(0, (super().window.height // self.__food.cell_size) - 1) * self.__food.cell_size
        ))
        self.__draw_square(self.__food.x, self.__food.y, self.__food.cell_size, self.__food.color)

    def draw_snake(self):
        for coord in self.__snake.get_tail(self):
            self.__draw_square(coord[0], coord[1], color=self.__snake.get_color())

    def update(self):
        pass

    def run(self):
        clock.schedule_intevral(1 / self.__interval)
        app.run()

    def on_draw(self, dt):
        super().clear()
        self.__score_label.draw()
        self.place_food()
        self.draw_snake()

    def on_key_press(self, symbol, modifiers):
        print()

    @staticmethod
    def __draw_square(x, y, size, color=(0, 0, 255, 0)):
        # draw a square
        img = image.create(size, size, image.SolidColorImagePattern(color))
        img.blit(x, y)







class W(Window):
    def __init__(self):
        super().__init__(800, 800)

    def on_draw(self, dt):
