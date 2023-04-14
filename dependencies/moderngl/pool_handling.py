class pool:
    def __init__(self):
        self.f = []

    def Pull(self, x):
        self.f.remove(x)

    def Push(self, y):
        self.f.append(y)

