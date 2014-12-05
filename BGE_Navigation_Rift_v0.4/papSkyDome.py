import bge
scene = bge.logic.getCurrentScene()

print ("Initializing CameraBGE")
cameraBGE = False
if "CameraBGE" in scene.objects:
	cameraBGE = scene.objects["CameraBGE"]
else:
	print ("Object CameraBGE not present in Scene")
	bge.logic.endGame()

# posizionamento dello SkyDome

skyDome = False
if "SkyDome" in scene.objects:
	skyDome = scene.objects["SkyDome"]
else:
	print ("Object SkyDome not present in Scene")

def papUpdateSkyDome(controller):
	if skyDome:
		skyDome.worldPosition = cameraBGE.worldPosition