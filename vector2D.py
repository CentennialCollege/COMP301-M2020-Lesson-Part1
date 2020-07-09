class Vector2D(object):
    #constructor
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __add__(self, rhs):
        Xs = self.x + rhs.x
        Ys = self.y + rhs.y

        self.x = Xs
        self.y = Ys