from dependencies.parsejson.parse import *

class ShaderProgram:
    def __init__(self, ctx):
        self.ctx = ctx
        self.programs = {}
        self.programs['default'] = self.get_program('default')
        self.programs['metal'] = self.get_program('metal')
        self.programs['skybox'] = self.get_program('skybox')
        self.programs['advanced_skybox'] = self.get_program('advanced_skybox')
        self.programs['shadow_map'] = self.get_program('shadow_map')

    def get_program(self, shader_program_name):
        with open(f'{ASSETS["shaders"]["dir"] + shader_program_name + ASSETS["shaders"]["exts"][0]}') as file:
            vertex_shader = file.read()

        with open(f'{ASSETS["shaders"]["dir"] + shader_program_name + ASSETS["shaders"]["exts"][1]}') as file:
            fragment_shader = file.read()

        program = self.ctx.program(vertex_shader=vertex_shader, fragment_shader=fragment_shader)
        return program

    def destroy(self):
        [program.release() for program in self.programs.values()]
