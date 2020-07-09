class Vector2D(object):
    #constructor
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    #overload the binary +
    def __add__(self, rhs):
        Xs = self.x + rhs.x
        Ys = self.y + rhs.y

        self.x = Xs
        self.y = Ys

        return self.x, self.y

    #overload the -
    def __sub__(self, rhs):
        diffXs = self.x - rhs.x
        diffYs = self.y - rhs.y

        self.x = diffXs
        self.y = diffYs

        return self.x, self.y

    #utility function for distance
    '''
    @staticmethod
    def Distance(vector1, vector2):
        diffXs = vector2.x - vector1.x
        diffYs = vector2.y - vector1.y
        return (diffXs * diffXs + diffYs * diffYs) ** 0.5
    '''

    