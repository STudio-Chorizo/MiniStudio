import glm

class Pool:
    def __init__(self):
        self.pool = []

    def Add(self, obj):
        obj.isActive = False
        obj.position = glm.vec3([-1000, -1000, -1000])
        obj.Update()
        self.pool.append(obj)

    def Get(self):
        if(len(self.pool) <= 0) : return False
        obj = self.pool[0]
        obj.isActive = True
        self.pool.pop(0)
        return obj