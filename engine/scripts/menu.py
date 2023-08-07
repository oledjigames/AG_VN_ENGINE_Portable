def menu_render():
	run = True
	menu_text = ["New Game", "Exit"]
	menu_button = 0
	global id_current, lastPad, Game_running, character
	character= []
	pspmp3.load("game/music/menu.mp3")        # Uncomment this to add a MP3 in backgound
	pspmp3.play()
	while run:
		if menu_button==(-1):menu_button = 0
		elif menu_button==(2):menu_button = 1
		screen.clear(psp2d.Color(0,0,0,255))
		screen.blit(ui_menu)
		#render_multi_line("Tailer \npidor", 50, 50, 15)
		if menu_button ==(0):
			font.drawText(screen, 3, 173, ">"+menu_text[0])
			font.drawText(screen, 3, 185, ""+menu_text[1])
		elif menu_button ==(1):
			font.drawText(screen, 3, 173, ""+menu_text[0])
			font.drawText(screen, 3, 185, ">"+menu_text[1])
		screen.swap()
		pad = psp2d.Controller()
		if pad.cross and (not lastPad or time() - lastPad >= 0.5):
			if menu_button==(0):id_current+=1;run=False
			elif menu_button==(1):run=False;Game_running = False
			lastPad = time()
		elif pad.down:menu_button+=1
		elif pad.up:menu_button-=1
		pass
	pspmp3.stop()