import engine
from engine import EmptyNode, CameraNode, BitmapSpriteNode, Rectangle2DNode, Vector3, Rectangle
import gc
print("dir(engine):",dir(engine))
print("dir(EmptyNode):", dir(EmptyNode))
print("dir(CameraNode):", dir(CameraNode))
print("dir(BitmapSpriteNode):", dir(BitmapSpriteNode))
print("dir(Rectangle2DNode):", dir(Rectangle2DNode))
print("dir(Vector3):", dir(Vector3))
print("dir(Rectangle):", dir(Rectangle))

engine.debug_enable_all()
# engine.debug_enable_setting(engine.debug_setting_performance)


class MyNodeCam(CameraNode):
    def __init__(self):
        super().__init__(self)
    
    def tick(self):
        pass
        # print("hi from camera!")


class MySprite(BitmapSpriteNode):
    def __init__(self):
        super().__init__(self)
        # self.height = 10

    def tick(self):
        pass
        # print("hi from sprite!")


class MyRect2D(Rectangle2DNode):
    def __init__(self):
        super().__init__(self)
        # self.width = 5
        # self.position.x = 10
    
    def tick(self):
        pass
        # print("hi from sprite!")

a = MySprite()
b = MyRect2D()
c = MyNodeCam()
print("Made everything")
b.rect.pos.x = 4
print("Set position")
print(b.rect.pos.x)

class MyRect2DPrimitive(Rectangle):
    def __init__(self):
        pass
        # self.width = 5
        # self.position.x = 10
    
    def tick(self):
        pass
        # print("hi from sprite!")
        

rectPrimitive = MyRect2DPrimitive()

rectPrimitive.pos.x = 5
print(rectPrimitive.pos.x)

# a.position.x = 0
# b.position.x = 10


# print(dir(v))
# print(v, end='')

#engine.start()


# class MyNodeA(EmptyNode):
#     def __init__(self):
#         super().__init__(self)

#     def tick(self):
#         pass
#         # print("hi from tick() A")


# class MyNodeB(EmptyNode):
#     def __init__(self):
#         super().__init__(self)


# class MyNodeC(EmptyNode):
#     def __init__(self):
#         super().__init__(self)


# class MyNodeD(EmptyNode):
#     def __init__(self):
#         super().__init__(self)
    
#     def tick(self):
#         pass
#         # print("hi from tick() D")

# class MyNodeCam(CameraNode):
#     def __init__(self):
#         super().__init__(self)
    
#     def tick(self):
#         pass
#         # print("hi from camera!")

# class MySprite(BitmapSpriteNode):
#     def __init__(self):
#         super().__init__(self)

#     def tick(self):
#         pass
#         # print("hi from sprite!")


# class MyRect2D(Rectangle2DNode):
#     def __init__(self):
#         super().__init__(self)
#         self.height = 10
    
#     def tick(self):
#         pass
#         # print("hi from sprite!")


# a = MyNodeA()
# b = MyNodeB()
# if(True):
#     c = MyNodeC()
#     del c
# d = MyNodeD()
# d.set_layer(7)

# e = MyNodeA()
# e1 = MyNodeA()
# e2 = MyNodeA()
# e3 = MyNodeA()
# e4 = MyNodeA()
# e5 = MyNodeA()
# e6 = MyNodeA()
# e7 = MyNodeA()

# print()


# v = Vector3()
# v.x = 2
# v.y = 2
# v.z = 2
# print(dir(v))
# print(v, end='')


# cam0 = MyNodeCam()
# cam1 = MyNodeCam()
# cam2 = MyNodeCam()
# cam3 = MyNodeCam()


# cam0.viewport.x=0
# cam0.viewport.y=0
# cam0.viewport.width=64
# cam0.viewport.height=64

# cam1.viewport.x=64
# cam1.viewport.y=0
# cam1.viewport.width=64
# cam1.viewport.height=64

# cam2.viewport.x=0
# cam2.viewport.y=64
# cam2.viewport.width=64
# cam2.viewport.height=64

# cam3.viewport.x=64
# cam3.viewport.y=64
# cam3.viewport.width=64
# cam3.viewport.height=64

# spr = MySprite()

# r = MyRect2D()


# gc.collect()

# engine.start()