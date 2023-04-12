# Import des dependances
import struct
import moderngl
from dependencies.moderngl.load import *
import numpy as np
from PIL import Image

class loadmg:
    def __init__(self) -> None:
        self.ctx = moderngl.create_context(standalone=True)
        self.buf = self.ctx.buffer(b'Hello World!')  # allocated on the GPU
        
        self.fbo = self.ctx.simple_framebuffer((100, 100), 4)
        self.fbo.use()

    def renderer(self):
        pass