import random
import math

class GameBoard:
    def __init__(self, size):
        self.size = size
        self.board = [['*' for i in range(size)] for i in range(size)]

    def display(self):
        for row in self.board:
            print(' '.join(row))
        print()

class Spaceship:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.symbol = 'S'

    def move(self, x, y):
        self.x = x
        self.y = y

class Planet:
    def __init__(self, x, y, size):
        self.x = x
        self.y = y
        self.size = size
        self.symbol = 'P'

    def is_in_atmosphere(self, x, y):
        return math.sqrt((self.x - x) ** 2 + (self.y - y) ** 2) <= self.size + 1

    def occupy_area(self, board):
        for i in range(self.size):
            for j in range(self.size):
                if 0 <= self.x + i < board.size and 0 <= self.y + j < board.size:
                    board.board[self.x + i][self.y + j] = self.symbol

class Obstacle:
    def __init__(self, x, y, size):
        self.x = x
        self.y = y
        self.size = size
        self.symbol = 'O'

    def occupy_area(self, board):
        for i in range(self.size):
            for j in range(self.size):
                if 0 <= self.x + i < board.size and 0 <= self.y + j < board.size:
                    board.board[self.x + i][self.y + j] = self.symbol

    def is_collision(self, x, y):
        for i in range(self.size + 2): 
            for j in range(self.size + 2):
                if 0 <= self.x + i < self.size and 0 <= self.y + j < self.size:
                    if math.sqrt((self.x + i - x) ** 2 + (self.y + j - y) ** 2) <= 1: #це рівняння довжини вектора
                        return True
        return False

class SpaceGame:
    def __init__(self, board_size):
        self.board = GameBoard(board_size)
        self.spaceship = None
        self.planet = None
        self.obstacles = []
        self.create_game_elements()

    def create_game_elements(self):
        planet_size = random.choice([4, 5])
        planet_x = random.randint(0, self.board.size - planet_size)
        planet_y = random.randint(0, self.board.size - planet_size)
        self.planet = Planet(planet_x, planet_y, planet_size)
        
        #перешкоди
        num_obstacles = random.randint(1, 4)
        for _ in range(num_obstacles):
            obstacle_size = random.randint(1, 3)
            obstacle_x = random.randint(0, self.board.size - obstacle_size)
            obstacle_y = random.randint(0, self.board.size - obstacle_size)
            new_obstacle = Obstacle(obstacle_x, obstacle_y, obstacle_size)
            self.obstacles.append(new_obstacle)

        self.spaceship = Spaceship(random.randint(0, self.board.size - 1), random.randint(0, self.board.size - 1))

    def display(self):
        for row in range(self.board.size):
            for col in range(self.board.size):
                self.board.board[row][col] = '*'

        self.planet.occupy_area(self.board)
        for obstacle in self.obstacles:
            obstacle.occupy_area(self.board)
        self.board.board[self.spaceship.x][self.spaceship.y] = self.spaceship.symbol
        self.board.display()

    def move_spaceship(self, x, y):
        if self.planet.is_in_atmosphere(x, y):
            print("Перемога")
            return True

        for obstacle in self.obstacles:
            if obstacle.is_collision(x, y):
                print("Бам! Поразка")
                return True

        self.spaceship.move(x, y)
        self.display()
        return False

    def play(self):
        self.display()
        while True:
            try:
                x, y = map(int, input("Рух (x y): ").split())
                if self.move_spaceship(x, y):
                    break
            except ValueError:
                print("Введіть два числа")

if __name__ == "__main__":
    n = int(input("Введіть розмір поля:"))
    game = SpaceGame(n)
    game.play()
1