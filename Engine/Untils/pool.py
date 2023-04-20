
class Pool:
    def __init__(self):
        self.pool = []

    def Add(self, obj):
        obj.isActive = False
        self.pool.append(obj)

    def Get(self):
        obj = self.pool[0]
        obj.isActive = True
        self.pool.pop(0)
        return obj