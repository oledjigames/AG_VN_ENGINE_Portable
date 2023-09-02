#pspogg.init(2)
def play_music(id, name):
	global id_current, Do_once
	if id_current ==(id):
		if Do_once:
			pspmp3.load("game/music/"+name+".mp3")        # Uncomment this to add a MP3 in backgound
			pspmp3.play()
def stop_music(id):
	global id_current, Do_once
	if id_current ==(id):
		pspmp3.stop()
def play_sound(id, name):
	global id_current, Do_once_sound
	if id_current ==(id):
		if Do_once_sound:
			pspogg.load("game/sound/"+name+".ogg")
			pspogg.play()
			Do_once_sound = False