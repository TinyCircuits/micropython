import engine
from engine import EmptyNode, CameraNode, BitmapSpriteNode, Rectangle2DNode, Vector3, Rectangle
import gc
import math
print("dir(engine):",dir(engine))
print("dir(EmptyNode):", dir(EmptyNode))
print("dir(CameraNode):", dir(CameraNode))
print("dir(BitmapSpriteNode):", dir(BitmapSpriteNode))
print("dir(Rectangle2DNode):", dir(Rectangle2DNode))
print("dir(Vector3):", dir(Vector3))
print("dir(Rectangle):", dir(Rectangle))

engine.debug_enable_all()
# engine.debug_enable_setting(engine.debug_setting_performance)


b = Rectangle2DNode()


# class MyRect2D(Rectangle2DNode):
#     def __init__(self):
#         super().__init__(self)

#         self.color = 0b1111100000011111
    
#     def tick(self):
#         print("TEST")

# a = MyRect2D()
# print(dir(a))
# print(a)


# for i in range(10):
#     test0 = Rectangle2DNode()
#     test0.position.x = test0.position.x + i*2
#     test0.position.y = test0.position.y + i*2
#     print(test0.width)

# class MyRect2D(Rectangle2DNode):
#     def __init__(self):
#         super().__init__(self)

#         self.width = 5
#         self.color = 0b1111100000011111
#         self.position.x = 10
#         self.angle = 0
    
#     def tick(self):
#         self.angle = self.angle + 0.1
#         self.position.x = self.position.x + (5 * math.cos(self.angle))
#         self.position.y = self.position.y + (5 * math.sin(self.angle))


# test1 = MyRect2D()
# print(test1.width)


class MyNodeCam(CameraNode):
    def __init__(self):
        super().__init__(self)
    
    def tick(self):
        print("hi from camera!")

cam = MyNodeCam()


# class MyNodeC(EmptyNode):
#     def __init__(self):
#         super().__init__(self)
    
#     def tick(self):
#         pass

# if(True):
#     c = MyNodeC()
#     del c

#     d = MyRect2D()
#     del d

# gc.collect()




engine.start()

# # class MySprite(BitmapSpriteNode):
# #     def __init__(self):
# #         super().__init__(self)
# #         # self.height = 10

# #     def tick(self):
# #         pass
# #         # print("hi from sprite!")


# class MyRect2D(Rectangle2DNode):
#     def __init__(self):
#         super().__init__(self)

#         # self.width = 5
#         # self.position.x = 10
    
#     def tick(self):
#         pass
#         # print("hi from sprite!")

# # a = MySprite()
# b = MyRect2D()
# c = MyNodeCam()
# b.set_width(5)
# # print(b.width)
# # b.width = 10
# # print(b.width)

# # a.position.x = 0
# # b.position.x = 10


# # print(dir(v))
# # print(v, end='')

# engine.start()


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