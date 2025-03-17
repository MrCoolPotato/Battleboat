class Player:
    def __init__(self, name):
        self.name = name

    def get_move(self):
        x, y = map(int, input(f"{self.name}, enter coordinates to attack (x y): ").split())
        return x, y
