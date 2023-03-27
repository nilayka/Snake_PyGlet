from Color import Color

class Piton:
    def __init__(self, color=Color.BLUE, piton_length=1, name='Piton', cell_size=10):
        self.__name = name
        self.__color = color
        self.__piton_length = piton_length
        self.__cell_size = cell_size
        self.__rota = 0
        self.__tail = []
        self.__x = 0
        self.__y = 0
        self.__dx = 0
        self.__dy = 0

    def grow(self):
        self.__x += self.__dx
        self.__y += self.__dy
        self.__tail.append((self.__x, self.__y))

    def move(self):
        self.grow()
        self.__tail.pop(0)

    def get_name(self):
        return self.__name

    def get_location(self):
        return (self.__x, self.__y)

    def get_color(self):
        return self.__color

    def get_len(self):
        return len(self.__tail)

    def get_cell_size(self):
        return self.__cell_size

    def set_location(self, location):
        self.__x, self.__y = location




Arbi = Piton(name="Arbi", color=Color.RED, location=(3, 6))
print(Arbi.get_color())