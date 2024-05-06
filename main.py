from triugolnik import Figure, Point


class Main:
    def __init__(self):
        self.is_exit = False
        self.figure = None
        self.menu = {
            0: (self.exs, 'Выход'),
            1: (self.create_figure, 'Создать фигуру'),
            2: (self.figure_add, 'Сместить фигуру'),
            3: (self.print_figure, 'Вывести фигуру')
        }
        while not self.is_exit:
            self.core = self.get_core()
            func = self.menu.get(self.core, (self.exs, ''))[0]
            func()

    def get_core(self):
        for key, values in self.menu.items():
            print(f'{key} {values[1]}\n')
        return int(input())

    def create_figure(self):
        self.figure = Figure()

    def print_figure(self):
        print(self.figure)

    def figure_add(self):
        if not self.figure:
            return
        print('Введите число для смещения координат')
        inputs = int(input())
        self.figure += inputs

    def exs(self):
        print("Выход из программы")
        self.is_exit = True


a = Main()
