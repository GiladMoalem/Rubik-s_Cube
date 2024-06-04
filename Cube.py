from enum import Enum
from Color import Color


class Face(Enum):
    FRONT = 0
    BACK = 1
    UP = 2
    DOWN = 3
    RIGHT = 4
    LEFT = 5

    def __str__(self):
        return self.name

    def __repr__(self):
        return self.name


class Movement(Enum):
    RIGHT = 0
    LEFT = 1

    def __str__(self):
        return self.name


class Cube:

    def __init__(self):
        print('new cube')
        self.dim = 2
        self.sides_color_order = [
            (Face.UP, Color.WHITE),
            (Face.DOWN, Color.YELLOW),
            (Face.FRONT, Color.BLUE),
            (Face.RIGHT, Color.ORANGE),
            (Face.BACK, Color.GREEN),
            (Face.LEFT, Color.RED)
        ]
        self.matrix = [[[0 for _ in range(self.dim)] for _ in range(self.dim)] for _ in self.sides_color_order]

        for (side, color) in self.sides_color_order:
            for i in range(self.dim):
                for j in range(self.dim):
                    self.matrix[side.value][i][j] = color
                    # self.matrix[side.value][i][j] = (i, j)

    def face_to_string(self, face):
        return f"{self.matrix[face.value][0][0]} {self.matrix[face.value][0][1]}", \
               f"{self.matrix[face.value][1][0]} {self.matrix[face.value][1][1]}"

    def print(self):

        left = self.face_to_string(Face.LEFT)
        front = self.face_to_string(Face.FRONT)
        right = self.face_to_string(Face.RIGHT)
        back = self.face_to_string(Face.BACK)
        up = self.face_to_string(Face.UP)
        down = self.face_to_string(Face.DOWN)
        print(up[0].center(len(f"{left[0]}  |   {front[0]}  |  {right[0]}  ")))
        print(up[1].center(len(f"{left[0]}  |   {front[0]}  |  {right[0]}  ")))
        print(('-' * len(up[1])).center(len(f"{left[0]}  |   {front[0]}  |  {right[0]}  ")))
        print(f"{left[0]}  |   {front[0]}  |  {right[0]}  |  {back[0]}")
        print(f"{left[1]}  |   {front[1]}  |  {right[1]}  |  {back[1]}")
        print(('-' * len(left[1])).center(len(f"{left[0]}  |   {front[0]}  |  {right[0]}  ")))
        print(down[0].center(len(f"{left[0]}  |   {front[0]}  |  {right[0]}  ")))
        print(down[1].center(len(f"{left[0]}  |   {front[0]}  |  {right[0]}  ")))

    def rotate(self, indexes_list: list, movement: Movement = Movement.RIGHT):
        if movement == Movement.LEFT:
            indexes_list = indexes_list[::-1]
        get_value_from_indexes = lambda indexes: self.matrix[indexes[0]][indexes[1]][indexes[2]]

        temp = get_value_from_indexes(indexes_list[-1])
        # rotate right
        for index in range(len(indexes_list))[::-1]:
            cur_face = indexes_list[index][0]
            cur_i = indexes_list[index][1]
            cur_j = indexes_list[index][2]

            self.matrix[cur_face][cur_i][cur_j] = get_value_from_indexes(indexes_list[index - 1])
        self.matrix[indexes_list[0][0]][indexes_list[0][1]][indexes_list[0][2]] = temp

    def move(self, face:Face, movement :Movement):
        # TODO: maybe the directions not Uniform.
        # TODO: need to debug it!
        self.rotate([(face.value, 0, 0), (face.value, 0, 1), (face.value, 1, 1), (face.value, 1, 0)], movement)
        background_faces = []
        if face == Face.FRONT:
            background_faces = [(Face.LEFT.value, 1, 1), (Face.UP.value, 1, 0), (Face.RIGHT.value, 0, 0), (Face.DOWN.value, 0, 1)]
            self.rotate(background_faces, movement)
            background_faces = [(Face.LEFT.value, 0, 1), (Face.UP.value, 1, 1), (Face.RIGHT.value, 1, 0), (Face.DOWN.value, 0, 0)]
            self.rotate(background_faces, movement)

        if face == Face.BACK:
            background_faces = [(Face.LEFT.value, 1, 0), (Face.UP.value, 0, 0), (Face.RIGHT.value, 0, 1),
                                (Face.DOWN.value, 1, 1)]
            self.rotate(background_faces, movement)
            background_faces = [(Face.LEFT.value, 0, 0), (Face.UP.value, 0, 1), (Face.RIGHT.value, 1, 1),
                                (Face.DOWN.value, 1, 0)]
            self.rotate(background_faces, movement)

        elif face == Face.RIGHT:
            background_faces = [(Face.FRONT.value, 0, 1), (Face.UP.value, 0, 1), (Face.BACK.value, 1, 0),
                                (Face.DOWN.value, 0, 1)]
            self.rotate(background_faces, movement)
            background_faces = [(Face.FRONT.value, 1, 1), (Face.UP.value, 1, 1), (Face.BACK.value, 0, 0),
                                (Face.DOWN.value, 1, 1)]
            self.rotate(background_faces, movement)

        elif face == Face.LEFT:
            background_faces = [(Face.FRONT.value, 0, 0), (Face.UP.value, 0, 0), (Face.BACK.value, 1, 1),
                                (Face.DOWN.value, 0, 0)]
            self.rotate(background_faces, movement)
            background_faces = [(Face.FRONT.value, 1, 0), (Face.UP.value, 1, 0), (Face.BACK.value, 0, 1),
                                (Face.DOWN.value, 1, 0)]
            self.rotate(background_faces, movement)

        elif face == Face.UP:
            background_faces = [(Face.FRONT.value, 0, 0), (Face.RIGHT.value, 0, 0), (Face.BACK.value, 0, 0),
                                (Face.LEFT.value, 0, 0)]
            self.rotate(background_faces, movement)
            background_faces = [(Face.FRONT.value, 0, 1), (Face.RIGHT.value, 0, 1), (Face.BACK.value, 0, 1),
                                (Face.LEFT.value, 0, 1)]
            self.rotate(background_faces, movement)

        elif face == Face.DOWN:
            background_faces = [(Face.FRONT.value, 1, 1), (Face.RIGHT.value, 1, 1), (Face.BACK.value, 1, 1),
                                (Face.LEFT.value, 1, 1)]
            self.rotate(background_faces, movement)
            background_faces = [(Face.FRONT.value, 1, 0), (Face.RIGHT.value, 1, 0), (Face.BACK.value, 1, 0),
                                (Face.LEFT.value, 1, 0)]
            self.rotate(background_faces, movement)




c = Cube()
c.print()


c.move(Face.LEFT, Movement.RIGHT)
print()
c.print()

c.move(Face.FRONT, Movement.RIGHT)
print()
c.print()

