from asyncio.windows_events import NULL
from dependencies.Engine.Engine import ENGINE

from dependencies.moderngl.model import ExtendedBaseModel


class GameObject(ExtendedBaseModel):
    def __init__(self, pos = (0, 0, 0), rot = (0, 0, 0), scale = (1, 1, 1)):
        self.position = pos
        self.rotation = rot
        self.scale = scale
        self.UID = "-1"

        self.isCollide = False
        self.collideBox = NULL

        self.model = NULL

    def SetModel(self, name, vbo, tex_id, pos=(0, 0, 0), rot=(0, 0, 0), scale=(1, 1, 1)):
        if(ENGINE == NULL) : return
        ENGINE.graphicEngine.mesh.vao.vbo.AddVBO(name, vbo)
        self.model = ExtendedBaseModel(ENGINE.graphicEngine, name, tex_id, pos, rot, scale)
        ENGINE.graphicEngine.scene.AddObject()
        

    #Utiliser cette fonction pour avoir les collision
    def Move(self, translation):
        self.position += translation
        if(self.isCollide == False) : return
        #TO-DO test de colllision

    def Update(self, engine):
        pass

