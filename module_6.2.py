class Vehicle:
    _COLOR_VARIANTS = ['blue', 'pink', 'yellow']

    def __init__(self, owner, _model, _engine_power, _color):
        self.owner = owner
        self._model = _model
        self._engine_power = _engine_power
        self._color = _color

    def get_model(self):
        return f'Модель:  {self._model}'

    def get_horsepower(self):
        return f'Мощность двигателя: {self._engine_power}'

    def get_color(self):
        return f'Цвет: {self._color}'

    def print_info(self):
        print(self.get_model())
        print(self.get_horsepower())
        print(self.get_color())
        print(f'Владелец: {self.owner}')

    def set_color(self, new_color):
        self._color = new_color
        new_color = new_color.lower()
        if new_color in Vehicle._COLOR_VARIANTS:
            self._color = new_color
        else:
            print(f'Нельзя сменить цвет на {new_color}')


class Sedan(Vehicle):
    _PASSENGERS_LIMIT = 5

    def __init__(self, owner, _model, _engine_power, _color):
        super().__init__(owner, _model, _engine_power, _color)


car = Sedan('Bob', 'Volvo', 150, 'blue')
car.print_info()
car.set_color('WHITE')
car.set_color('PINK')
car.owner = "Nick"
car.print_info()
