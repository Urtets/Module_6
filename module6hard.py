import math


class Figure:
    sides_count = 0

    def __init__(self, color, *args):
        self.__color = color
        if len(args) == self.sides_count:
            self.__sides = args
        else:
            self.__sides = []
            value = list(args)
            for i in range(self.sides_count):
                self.__sides.append(value[0][0])

        self.filled = False

    def get_color(self):
        color = self.__color
        return color

    def __is_valid_color(self, r, g, b):
        counter = 0
        if r >= 0 and r <= 255:
            counter += 1
        if g >= 0 and g <= 255:
            counter += 1
        if b >= 0 and b <= 255:
            counter += 1
        if counter == 3:
            return True
        else:
            return False

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]

    def __is_valid_sides(self, *args):
        if len(args) == self.sides_count:  # Возможна ошибка из-за переопределения метода __len__
            counter = 0
            for i in args:
                if int(i).is_integer() and i > 0:
                    counter += 1
            if counter == len(args):
                return True
            else:
                return False
        else:
            return False

    def get_sides(self):
        sides = self.__sides
        return sides

    def __len__(self):
        var = 0
        for i in self.__sides:
            var = var + i
        return var

    def set_sides(self, *new_sides):
        if self.sides_count == len(new_sides):  # Возможна ошибка из-за переопределения метода __len__
            self.__sides = new_sides


class Circle(Figure):
    sides_count = 1

    def __init__(self, color, *args):
        super().__init__(color, args)
        self.__radius = args[0] / (2 * math.pi)

    def get_square(self):
        area = self.__radius ** 2 * math.pi
        return area


class Triangle(Figure):
    sides_count = 3

    def __init__(self, color, *args):
        super().__init__(color, args)

    def get_square(self):
        sides = self.get_sides()
        p = (1/2) * (sides[0] + sides[1] + sides[2])
        square = math.sqrt(p * (p - sides[0]) * (p - sides[1]) * (p - sides[2]))
        return square


class Cube(Figure):
    sides_count = 12

    def __init__(self, color, *args):
        super().__init__(color, args)


    def get_volume(self):
        sides = self.get_sides()
        side = self.get_sides()[0]
        volume = int(side)**3
        return volume


if __name__ == '__main__':
    circle1 = Circle((200, 200, 100), 10)  # (Цвет, стороны)
    cube1 = Cube((222, 35, 130), 6)

    # Проверка на изменение цветов:
    circle1.set_color(55, 66, 77)  # Изменится
    print(circle1.get_color())
    cube1.set_color(300, 70, 15)  # Не изменится
    print(cube1.get_color())

    # Проверка на изменение сторон:
    cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
    print(cube1.get_sides())
    circle1.set_sides(15)  # Изменится
    print(circle1.get_sides())

    # Проверка периметра (круга), это и есть длина:
    print(len(circle1))

    # Проверка объёма (куба):
    print(cube1.get_volume())