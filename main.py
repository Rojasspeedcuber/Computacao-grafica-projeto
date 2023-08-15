from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *
import glfw
import numpy as np

glfw.init()

janela = glfw.create_window(900,700,'Py OpenGL triangle',None,None)
glfw.set_window_pos(janela, 500, 300)
glfw.make_context_current(janela)

vertices = [-0.5, -0.5,0.0,
             0.5, -0.5,0.0,
             0.0, 0.5,0.0]

v = np.array(vertices, dtype = np.float32)

glEnableClientState(GL_VERTEX_ARRAY)
glVertexPointer(3, GL_FLOAT,0,v)
glClearColor(255, 180, 0, 0)

while not glfw.window_should_close(janela):
    glfw.poll_events()
    glClear(GL_COLOR_BUFFER_BIT)
    glDrawArrays(GL_TRIANGLES,0,3)
    glfw.swap_buffers(janela)

glfw.terminate()