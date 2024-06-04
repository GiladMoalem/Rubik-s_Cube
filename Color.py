from enum import Enum


class Color(Enum):
    WHITE = 0
    YELLOW = 1
    RED = 2
    BLUE = 3
    ORANGE = 4
    GREEN = 5

    def __str__(self):
        return self.name[0]

    def __repr__(self):
        return self.name[0]

if __name__ == '__main__':
    f = Color.BLUE
    print(f)