from dependencies.moderngl.vbo import VBO
from dependencies.moderngl.shader_program import ShaderProgram


class VAO:
    def __init__(self, ctx):
        self.ctx = ctx
        self.vbo = VBO(ctx)
        self.program = ShaderProgram(ctx)
        self.vaos = {}
        # skybox vao
        self.vaos['skybox'] = self.get_vao(
            program=self.program.programs['skybox'],
            vbo=self.vbo.vbos['skybox'])

        # advanced_skybox vao
        self.vaos['advanced_skybox'] = self.get_vao(
            program=self.program.programs['advanced_skybox'],
            vbo=self.vbo.vbos['advanced_skybox'])

    def AddVAO(self, name, shader = "default"):
        self.vaos[name] = self.get_vao(
            program=self.program.programs["default"],
            vbo=self.vbo.vbos[name])
        self.vaos['shadow_' + name] = self.get_vao(
            program=self.program.programs['shadow_map'],
            vbo=self.vbo.vbos[name])

    def get_vao(self, program, vbo):
        vao = self.ctx.vertex_array(program, [(vbo.vbo, vbo.format, *vbo.attribs)], skip_errors=True)
        return vao

    def destroy(self):
        self.vbo.destroy()
        self.program.destroy()