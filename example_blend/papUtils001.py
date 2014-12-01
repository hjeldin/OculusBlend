#   init
#   ----

import bge
scene = bge.logic.getCurrentScene()


print ("Initializing Camera")
camera = False
if "Camera" in scene.objects:
	print ("Parenting Scene Camera to Player")
	camera = scene.objects["Camera"]
	# parenting scene Camera to Player CameraLocator
	parent = scene.objects["CameraLocator"]
	child = camera
	child.setParent(parent, 1, 0) # http://www.tutorialsforblender3d.com/GameModule/ClassKX_GameObject_31.html
else:
	print ("Object Camera not present in Scene")
	bge.logic.endGame()


#  PLAYER INIT
#  -----------

def papInitPlayer(controller):

	print ("Initializing Player")
	global player
	player = bge.logic.getCurrentController().owner

	# read properties
	global maxSpeed
	maxSpeed = player["Max Speed"]
	print ( "Max Speed = " + str(maxSpeed) )
	global rotAxisSensitivity
	rotAxisSensitivity = player["Joystick Aiming Sensitivity"]
	print ( "Joystick Aiming Sensitivity = " + str(rotAxisSensitivity) )
	global upDownInvert
	if player["Invert Vertical Axis"]:
		upDownInvert = 1
		print ( "Vertical Axis is Inverted" )
	if not player["Invert Vertical Axis"]:
		upDownInvert = -1
		print ( "Vertical Axis is Normal" )

#   Movimento e rotazione del Player tramite Joystick
#   --------------------

joystick = bge.logic.joysticks[0]
if joystick:
	print ( "Joystick [0] detected" )
else:
	print ( "Joystick [0] not detected" )

def papJoystickMoveRot(controller):

	if joystick:
		# questo legge i pulsanti
		#print(joystick.activeButtons)
		#print(joystick.axisValues)
	
		pushX = joystick.axisValues[0] * maxSpeed
		pushY = - joystick.axisValues[1] * maxSpeed
		# sposto il player
		player.applyMovement( [pushX,pushY,0], True )
	
		rotZ = - joystick.axisValues[2] * rotAxisSensitivity
		rotX = upDownInvert * joystick.axisValues[3] * rotAxisSensitivity
		# ruoto il player (orizzontale)
		player.applyRotation( [0,0,rotZ], True )
		# ruoto la camera (verticale)
		camera.applyRotation( [rotX,0,0], True )
	else:
		return


#   Movimento del Player tramite Keyboard
#   --------------------


def papKeyMove(controller):

	moveX = 0
	moveY = 0
	
	if controller.sensors["UP"].positive:
		moveY = maxSpeed
	if controller.sensors["DOWN"].positive:
		moveY = -maxSpeed
	if controller.sensors["RIGHT"].positive:
		moveX = maxSpeed
	if controller.sensors["LEFT"].positive:
		moveX = -maxSpeed

#	if controller.sensors["JUMP"].positive:
#		print("jump")

	# sposto il player
	player.applyMovement( [moveX,moveY,0], True )



# posizionamento dello SkyDome

skyDome = False
if "SkyDome" in scene.objects:
	skyDome = scene.objects["SkyDome"]
else:
	print ("Object SkyDome not present in Scene")

def papUpdateSkyDome(controller):
	if skyDome:
		skyDome.worldPosition = camera.worldPosition
