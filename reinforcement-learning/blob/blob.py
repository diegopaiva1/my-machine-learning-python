import random
from abc import ABC, abstractmethod

class Blob(ABC):
    def __init__(self, width, height):
        self.width = width
        self.height = height

        self.x = random.randint(0, self.width - 1)
        self.y = random.randint(0, self.height - 1)

    def move(self, direction):
        if direction == 'east':
            self.x += 1
        elif direction == 'west':
            self.x -= 1
        elif direction == 'north':
            self.y += 1
        elif direction == 'south':
            self.y -= 1
        elif direction == 'northeast':
            self.move('north')
            self.move('east')
        elif direction == 'northwest':
            self.move('north')
            self.move('west')
        elif direction == 'southeast':
            self.move('south')
            self.move('east')
        elif direction == 'southwest':
            self.move('south')
            self.move('west')
        elif direction == 'stand':
            pass
        else:
            raise ValueError(f'Invalid direction {direction}')

        # If we are out of bounds, fix!
        if self.x < 0:
            self.x = 0
        elif self.x > self.width - 1:
            self.x = self.width - 1

        if self.y < 0:
            self.y = 0
        elif self.y > self.height - 1:
            self.y = self.height - 1

    def same_cell(self, other):
        return self.x == other.x and self.y == other.y

    @abstractmethod
    def color(self):
        pass
