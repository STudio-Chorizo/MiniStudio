from asyncio.windows_events import NULL
import dependencies.engine.engine as Eng
import glm

from dependencies.moderngl.model import ExtendedBaseModel


class GameObject(ExtendedBaseModel):
    def __init__(self, model_name = "cube", pos = (0, 0, 0), rot = (0, 0, 0), scale = (1, 1, 1)):
        self.position = pos
        self.rotation = rot
        self.camera_yaw = self.rotation[1] - 90
        self.camera_pitch = self.rotation[0] - 10
        self.scale = scale
        self.UID = "-1"

        self.isCollide = False
        self.collideBox = NULL

        self.model = NULL
        self.SetModel(model_name, pos, rot, scale)

    def SetModel(self, name, pos=(0, 0, 0), rot=(0, 0, 0), scale=(1, 1, 1)):
        if(Eng.Engine.Instance == NULL) : return
        
        text_id = Eng.Engine.Instance.graphicEngine.mesh.texture.AddTexture(name)
        Eng.Engine.Instance.graphicEngine.mesh.vao.vbo.AddVBO(name)
        Eng.Engine.Instance.graphicEngine.mesh.vao.AddVAO(name)
        self.model = ExtendedBaseModel(Eng.Engine.Instance.graphicEngine, name, text_id, pos, rot, scale)
        Eng.Engine.Instance.graphicEngine.scene.AddObject(self.model)
        
    # Utiliser cette fonction pour avoir les collision
    def Move(self, translation: tuple) -> None:
        """Fonction pour déplacer l'objet et permettre les collision\n
        translation: (x, y, z) déplacement de l'objet"""
        self.position += translation
        self.velocity = translation
        self.model.pos += translation
    
    # Utiliser cette fonction pour avoir la rotation
    def Rotate(self, rotation: tuple, camRotation: tuple = glm.vec2([0, 0])) -> None:
        """Fonction pour touner l'objet\n
        rotation: (x, y, z) rotation de l'objet"""
        self.rotation += rotation
        self.model.rot += rotation
        self.camera_yaw += camRotation[0]
        self.camera_pitch += camRotation[1]
        
    # Utiliser cette fonction pour avoir les collision
    def SetPos(self, position: tuple) -> None:
        """Fonction pour définir un position de l'objet\n
        translation: (x, y, z) position de l'objet"""
        self.position = position
        self.model.pos = position
    
    # Utiliser cette fonction pour avoir la rotation
    def SetRot(self, orientation: tuple, camOrientation: tuple = glm.vec2([-90, -10])) -> None:
        """Fonction pour définir une rotation de l'objet\n
        orientation: (x, y, z) orientation de l'objet"""
        self.rotation = orientation
        self.model.rot = orientation
        self.camera_yaw = camOrientation[0]
        self.camera_pitch = camOrientation[1]
    
    def Update(self):
        pass