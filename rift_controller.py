import bge
import time
from rift import PyRift
from mathutils import Quaternion, Euler, Vector

def poll():
    bge.logic.rift.pollSensor()
    bge.logic.rotation = Quaternion((bge.logic.rift.headPose[3], bge.logic.rift.headPose[4], bge.logic.rift.headPose[5], bge.logic.rift.headPose[6]))
    bge.logic.position = Vector((bge.logic.rift.headPose[0],bge.logic.rift.headPose[1],bge.logic.rift.headPose[2]))
    print(bge.logic.rotation);
try:
    poll()
    
except:
    bge.logic.rift = PyRift()
    bge.logic.rift.connect()
        
    scene_e = bge.logic.getCurrentScene()
    cam_e = scene_e.active_camera
    bge.logic.init_position = Vector((cam_e.localPosition[0],cam_e.localPosition[1],cam_e.localPosition[2]))

    time.sleep(1)
    poll()

eu = bge.logic.rotation.to_euler()
pos = bge.logic.position

fix = Euler((-1.57, 0, 0), 'XYZ')
rot = Euler((-eu.z, eu.y, -eu.x), 'XYZ')

rot.rotate(fix)
pos.rotate(rot)

scene = bge.logic.getCurrentScene()
cam = scene.active_camera
cam.localOrientation = rot    
cam.localPosition = (pos * 1.0) + bge.logic.init_position
