class Figure(ABC):
    classname = None

    @abstractmethod
    def __init__(self, name=None):
        self.name = name
        self._x = 0
        self._y = 0
        self.__color = ''
    @property   #getter
    def x(self):
        return self._x
    @property  # getter
    def y(self):
        return self._y

    @property  # getter
    def color(self):
        return self._color


    @x.setter   #setter
    def x(self, value):
        return value

    @y.setter  # setter
    def y(self, value):
        return value
