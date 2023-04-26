from array import array
import pygame as pg
import moderngl as mgl
import sys
from dependencies.moderngl.model import *
from dependencies.moderngl.camera import Camera
from dependencies.moderngl.light import Light
from dependencies.moderngl.mesh import Mesh
from dependencies.moderngl.scene import Scene
from dependencies.moderngl.scene_renderer import SceneRenderer


class GraphicsEngine:
    def __init__(self, win_size=(1600, 900)):
        # window size
        self.WIN_SIZE = win_size
        # set opengl attr
        pg.display.gl_set_attribute(pg.GL_CONTEXT_MAJOR_VERSION, 3)
        pg.display.gl_set_attribute(pg.GL_CONTEXT_MINOR_VERSION, 3)
        pg.display.gl_set_attribute(pg.GL_CONTEXT_PROFILE_MASK, pg.GL_CONTEXT_PROFILE_CORE)
        # create opengl context
        pg.display.set_mode(self.WIN_SIZE, flags=pg.OPENGL | pg.DOUBLEBUF)
        # mouse settings
        pg.event.set_grab(True)
        pg.mouse.set_visible(False)
        # detect and use existing opengl context
        self.ctx = mgl.create_context()
        # self.ctx.front_face = 'cw'
        self.ctx.enable(flags=mgl.DEPTH_TEST | mgl.CULL_FACE)
        # create an object to help track time
        self.clock = pg.time.Clock()
        self.time = 0
        self.delta_time = 0
        # light
        self.light = Light()
        # camera
        self.camera = Camera(self)
        # mesh
        self.mesh = Mesh(self)
        # scene
        self.scene = Scene(self)
        # renderer
        self.scene_renderer = SceneRenderer(self)



        self.pgTexture = self.ctx.texture(self.WIN_SIZE, 4)
        self.pgTexture.filter = mgl.NEAREST, mgl.NEAREST

        self.pgTexture.swizzle = 'BGRA'

        # Shader UI
        self.texture_program = self.ctx.program(
            vertex_shader="""
                #version 330
                // Vertex shader runs once for each vertex in the geometry
                in vec2 in_vert;
                in vec2 in_texcoord;
                out vec2 uv;
                void main() {
                    // Send the texture coordinates to the fragment shader
                    uv = in_texcoord;
                    // Resolve the vertex position
                    gl_Position = vec4(in_vert, 0.0, 1.0);
                }
            """,
            fragment_shader="""
                #version 330
                // Fragment shader runs once for each pixel in the triangles.
                // We are drawing two triangles here creating a quad.
                // In values are interpolated between the vertices.
                // Sampler reading from a texture channel 0
                uniform sampler2D surface;
                // The pixel we are writing to the screen
                out vec4 f_color;
                // Interpolated texture coordinates
                in vec2 uv;
                void main() {
                    // Simply look up the color from the texture
                    f_color = texture(surface, uv);
                }
            """,
        )
        self.texture_program['surface'] = 0

        buffer = self.ctx.buffer(
            data=array('f', [
                -1.0, 1.0, 0.0, 1.0,  # upper left
                -1.0, -1.0, 0.0, 0.0,  # lower left
                1.0, 1.0, 1.0, 1.0,  # upper right
                1.0, -1.0, 1.0, 0.0,  # lower right
            ])
        )

        self.quad_fs = self.ctx.vertex_array(
            self.texture_program,
            [
                (
                    buffer,
                    "2f 2f",
                    "in_vert", "in_texcoord",
                )
            ],
        )

    def check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                self.mesh.destroy()
                self.scene_renderer.destroy()
                pg.quit()
                sys.exit()

    def render(self, GUI):
        self.ctx.clear()

        texture_data = GUI.get_view('1')
        self.pgTexture.write(texture_data)

        self.ctx.enable(mgl.BLEND)
        # render scene
        self.scene_renderer.render()
        
        self.pgTexture.use(location=0)
        self.quad_fs.render(mode=mgl.TRIANGLE_STRIP)

        self.ctx.disable(mgl.BLEND)


    def get_time(self):
        self.time = pg.time.get_ticks() * 0.001


if __name__ == '__main__':
    app = GraphicsEngine()
    app.run()