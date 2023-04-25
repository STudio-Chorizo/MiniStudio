from dependencies.moderngl.model import *
import glm


class Scene:
    def __init__(self, app):
        self.app = app
        self.objects = []
        # skybox
        self.skybox = AdvancedSkyBox(app)

    def AddObject(self, obj):
        self.objects.append(obj)

    def RemoveObject(self, obj):
        self.objects.remove(obj)
