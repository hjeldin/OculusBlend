import bge
from rift import PyRift
from mathutils import Quaternion, Euler, Vector

def poll():
    bge.logic.rift.pollSensor()
    bge.logic.rotation = Quaternion((bge.logic.rift.headPose[3], bge.logic.rift.headPose[4], bge.logic.rift.headPose[5], bge.logic.rift.headPose[6]))

try:
    poll()
    eu = bge.logic.rotation.to_euler()
except:
    bge.logic.rift = PyRift()
    bge.logic.rift.connect()
    eu = Euler((0, 0, 0), 'XYZ')

scene = bge.logic.getCurrentScene()
cam = scene.active_camera
fix = Euler((-1.57, 0, 0), 'XYZ')

rot = Euler((-eu.z, eu.y, -eu.x), 'XYZ')
rot.rotate(fix)
cam.localOrientation = rot
