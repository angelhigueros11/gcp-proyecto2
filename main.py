# Angel Higueros
# 20460
# Proyecto 2

from raytracerEngine import Raytracer, Point3
from Utilities import *
from figures import *
import numpy as np


def generateLeaves(origin, rayEngineInstance, leaves):
    rayEngineInstance.objArray.append(
        Cube(Point3(origin[0], origin[1]+1, origin[2]+1), Point3(1, 1, 1), leaves))
    rayEngineInstance.objArray.append(
        Cube(Point3(origin[0]+1, origin[1]+1, origin[2]), Point3(1, 1, 1), leaves))
    rayEngineInstance.objArray.append(
        Cube(Point3(origin[0]-1, origin[1]+1, origin[2]), Point3(1, 1, 1), leaves))
    rayEngineInstance.objArray.append(
        Cube(Point3(origin[0]-1, origin[1]+2, origin[2]+1), Point3(1, 1, 1), leaves))
    rayEngineInstance.objArray.append(
        Cube(Point3(origin[0]+1, origin[1]+2, origin[2]+1), Point3(1, 1, 1), leaves))
    rayEngineInstance.objArray.append(
        Cube(Point3(origin[0], origin[1]+2, origin[2]+1), Point3(1, 1, 1), leaves))


width = 512
height = 512
rayEngineInstance = Raytracer(width, height)
rayEngineInstance.envmap = EnvMap('space.bmp')

# Materiales a utilizar
sand = Material(texture=Texture('sand.bmp'))
water = Material(spec=64, ior=1.33, matType=TRANSPARENT)
water2 = Material(spec=64, ior=1.33, matType=REFLECTIVE)
wood = Material(texture=Texture('madera.bmp'))
leaves = Material(texture=Texture('leaves.bmp'))
moon = Material(diffuse=(0.9, 0.9, 0.9))

# Luz
rayEngineInstance.ambLight = AmbientLight(strength=0.8)


# Objetos
rayEngineInstance.objArray.append(
    Cube(Point3(-6, -3, -12), Point3(8, 0.5, 15), sand))

rayEngineInstance.objArray.append(
    Cube(Point3(-3, -1.5, -8), Point3(1, 1, 1), wood))
rayEngineInstance.objArray.append(
    Cube(Point3(-3, -0.5, -8), Point3(1, 1, 1), wood))
rayEngineInstance.objArray.append(
    Cube(Point3(-3, 0.5, -8), Point3(1, 1, 1), wood))
rayEngineInstance.objArray.append(
    Cube(Point3(-3, 1.5, -8), Point3(1, 1, 1), wood))

rayEngineInstance.objArray.append(
    Cube(Point3(-2, 2.5, -8), Point3(1, 1, 1), leaves))
rayEngineInstance.objArray.append(
    Cube(Point3(-4, 2.5, -8), Point3(1, 1, 1), leaves))
rayEngineInstance.objArray.append(
    Cube(Point3(-3, 2.5, -7), Point3(1, 1, 1), leaves))
rayEngineInstance.objArray.append(
    Cube(Point3(-2, 3.5, -7), Point3(1, 1, 1), leaves))
rayEngineInstance.objArray.append(
    Cube(Point3(-3, 3.5, -7), Point3(1, 1, 1), leaves))
rayEngineInstance.objArray.append(
    Cube(Point3(-4, 3.5, -7), Point3(1, 1, 1), leaves))

rayEngineInstance.objArray.append(
    Cube(Point3(2, -2.8, -15), Point3(20, 0.1, 30), water))

rayEngineInstance.objArray.append(
    Cube(Point3(9, -2.5, -23), Point3(12, 0.1, 15), sand))

rayEngineInstance.objArray.append(
    Cube(Point3(4, -1.5, -14), Point3(1, 1, 1), wood))
rayEngineInstance.objArray.append(
    Cube(Point3(4, -0.5, -14), Point3(1, 1, 1), wood))
rayEngineInstance.objArray.append(
    Cube(Point3(4, 0.5, -14), Point3(1, 1, 1), wood))
rayEngineInstance.objArray.append(
    Cube(Point3(4, 1.5, -14), Point3(1, 1, 1), wood))

generateLeaves([4, 1.5, -14], rayEngineInstance, leaves)


rayEngineInstance.objArray.append(
    Cube(Point3(8, -1.5, -17), Point3(1, 1, 1), wood))
rayEngineInstance.objArray.append(
    Cube(Point3(8, -0.5, -17), Point3(1, 1, 1), wood))
rayEngineInstance.objArray.append(
    Cube(Point3(8, 0.5, -17), Point3(1, 1, 1), wood))
rayEngineInstance.objArray.append(
    Cube(Point3(8, 1.5, -17), Point3(1, 1, 1), wood))
generateLeaves([8, 1.5, -17], rayEngineInstance, leaves)


rayEngineInstance.objArray.append(Sphere(Point3(0, 3, -15), 2, moon))


# generar imagen
rayEngineInstance.glRender()
rayEngineInstance.glFinish('proyecto2.bmp')
