from asyncio.windows_events import NULL
from dependencies.Engine.Engine import Engine

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

    def SetModel(self, name, pos=(0, 0, 0), rot=(0, 0, 0), scale=(1, 1, 1)):
        if(Engine.Instance == NULL) : return
        
        text_id = Engine.Instance.graphicEngine.mesh.texture.AddTexture(name)
        Engine.Instance.graphicEngine.mesh.vao.vbo.AddVBO(name)
        Engine.Instance.graphicEngine.mesh.vao.AddVAO(name)
        self.model = ExtendedBaseModel(Engine.Instance.graphicEngine, name, text_id, pos, rot, scale)
        Engine.Instance.graphicEngine.scene.AddObject(self.model)
        

    #Utiliser cette fonction pour avoir les collision
    def Move(self, translation):
        self.position += translation
        if(self.isCollide == False) : return
        #TO-DO test de colllision

    def Update(self, engine):
        pass

