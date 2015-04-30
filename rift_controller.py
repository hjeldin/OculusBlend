import bge
import time
from rift import PyRift
from mathutils import Quaternion, Euler, Vector

# Functions
def poll():
    bge.logic.rift.pollSensor()
    bge.logic.rotation = Quaternion((bge.logic.rift.headPose[3], bge.logic.rift.headPose[4], bge.logic.rift.headPose[5], bge.logic.rift.headPose[6]))
    bge.logic.position = Vector((bge.logic.rift.headPose[0],bge.logic.rift.headPose[1],bge.logic.rift.headPose[2]))

# Main
try:
    eu = bge.logic.rotation.to_euler()
    fix = Euler((-1.57, 0, 0), 'XYZ')
    rot = Euler((-eu.z, eu.y, -eu.x), 'XYZ')
    rot.rotate(fix)
    
    bge.logic.prev_orientation = rot;
    poll()
    
except:
    bge.logic.rift = PyRift()
    bge.logic.rift.connect()
            
    scene_e = bge.logic.getCurrentScene()
    cam_e = scene_e.active_camera
    bge.logic.init_position = Vector((cam_e.localPosition[0],cam_e.localPosition[1],cam_e.localPosition[2]))
    bge.logic.init_orientation = cam_e.localOrientation.to_euler() 

    eu = Euler()
    fix = Euler((1.57, 0, 0), 'XYZ')
    rot = Euler((-eu.z, eu.y, -eu.x), 'XYZ')
    rot.rotate(fix)

    bge.logic.prev_orientation = rot
    poll()

# From Oculus
eu = bge.logic.rotation.to_euler()
pos = bge.logic.position

# Fix coordinate frame
fix = Euler((-1.57, 0, 0), 'XYZ')
rot = Euler((-eu.z, eu.y, -eu.x), 'XYZ')
rot.rotate(fix)
pos.rotate(rot)

# Indexing
d_rot = Euler((rot.x - bge.logic.prev_orientation.x,
               rot.y - bge.logic.prev_orientation.y,
               rot.z - bge.logic.prev_orientation.z),'XYZ')

# Updating camera
scene = bge.logic.getCurrentScene()
cam = scene.active_camera

bge.logic.init_orientation.x = bge.logic.init_orientation.x + d_rot.x
bge.logic.init_orientation.y = bge.logic.init_orientation.y + d_rot.y
bge.logic.init_orientation.z = bge.logic.init_orientation.z + d_rot.z

cam.localOrientation = bge.logic.init_orientation
cam.localPosition = (pos * 1.0) + bge.logic.init_position
