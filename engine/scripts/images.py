intro("LOADING: BACKGROUNDS", 0.1)
background = [psp2d.Image('game/image/background/background0.png')] # background loading
temp_index = 1
temp_run = True
while temp_run:
	try:
		background.extend([psp2d.Image('game/image/background/background'+ str(temp_index) +'.png')])
		temp_index += 1
	except:
		temp_run = False

intro("LOADING: CHARACTERS", 0.1)
character_files = [psp2d.Image("game/image/character/character0.png")] # Character loading
temp_index = 1
temp_run = True
while temp_run:
	try:
		character_files.extend([psp2d.Image('game/image/character/character'+ str(temp_index) +'.png')])
		temp_index += 1
	except:
		temp_run = False
