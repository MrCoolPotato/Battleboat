from panda3d.core import Point3, Vec3, Geom, GeomNode, GeomTriangles, GeomVertexFormat, GeomVertexData, GeomVertexWriter
from direct.showbase.ShowBase import ShowBase
from direct.task import Task
from math import sin, cos

class MyApp(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)

        self.disableMouse()

        for x in range(2):
            for y in range(2):
                for z in range(2):
                    self.createCube(Point3(x-0.5, y-0.5, z-0.5))

        
        self.cameraHorizAngle = 0
        self.cameraVertAngle = 0

        self.keyMap = {"left": 0, "right": 0, "up": 0, "down": 0}
        self.accept('arrow_left', self.setKey, ["left", 1])
        self.accept('arrow_left-up', self.setKey, ["left", 0])
        self.accept('arrow_right', self.setKey, ["right", 1])
        self.accept('arrow_right-up', self.setKey, ["right", 0])
        self.accept('arrow_up', self.setKey, ["up", 1])
        self.accept('arrow_up-up', self.setKey, ["up", 0])
        self.accept('arrow_down', self.setKey, ["down", 1])
        self.accept('arrow_down-up', self.setKey, ["down", 0])

       
        self.taskMgr.add(self.moveCamera, "moveCameraTask")

    def createCube(self, pos):
        format = GeomVertexFormat.getV3n3c4()
        vdata = GeomVertexData('cube', format, Geom.UHStatic)
        vertex = GeomVertexWriter(vdata, 'vertex')
        normal = GeomVertexWriter(vdata, 'normal')
        color = GeomVertexWriter(vdata, 'color')

        for i in range(8):
            vertex.addData3f(pos + Point3(i&1, (i&2)>>1, (i&4)>>2))
            normal.addData3f(Vec3((i&1)*2-1, ((i&2)>>1)*2-1, ((i&4)>>2)*2-1))
            color.addData4f((i&1), ((i&2)>>1), ((i&4)>>2), 1)

        indices = [
            0, 1, 2, 2, 3, 0,  # Front face
            4, 5, 6, 6, 7, 4,  # Back face
            0, 1, 5, 5, 4, 0,  # Left face
            2, 3, 7, 7, 6, 2,  # Right face
            0, 3, 7, 7, 4, 0,  # Top face
            1, 2, 6, 6, 5, 1   # Bottom face
        ]

        geom = Geom(vdata)
        for i in range(0, len(indices), 3):
            tri = GeomTriangles(Geom.UHStatic)
            tri.addVertices(indices[i], indices[i+1], indices[i+2])
            geom.addPrimitive(tri)

        node = GeomNode('cube')
        node.addGeom(geom)
        self.render.attachNewNode(node)

    def setKey(self, key, value):
        self.keyMap[key] = value

    def moveCamera(self, task):
        dt = globalClock.getDt()

        if self.keyMap["left"]:
            self.cameraHorizAngle += dt
        if self.keyMap["right"]:
            self.cameraHorizAngle -= dt
        if self.keyMap["up"]:
            self.cameraVertAngle += dt
        if self.keyMap["down"]:
            self.cameraVertAngle -= dt

        self.cameraVertAngle = max(min(self.cameraVertAngle, 1.5), -1.5)

        
        radius = 20  
        x = radius * cos(self.cameraHorizAngle) * cos(self.cameraVertAngle)
        y = radius * sin(self.cameraHorizAngle) * cos(self.cameraVertAngle)
        z = radius * sin(self.cameraVertAngle)

        self.camera.setPos(x, y, z)
        self.camera.lookAt(Point3(0, 0, 0))

        return Task.cont

app = MyApp()
app.run()