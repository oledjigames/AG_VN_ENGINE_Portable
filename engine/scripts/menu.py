def menu_render():
	run = True
	menu_text = ["New Game", "Quick Load","Extra", "Exit"]
	menu_button = 0
	global id_current, lastPad, Game_running, character,main_plot
	character= []
	pspmp3.load("game/music/menu.mp3")        # Uncomment this to add a MP3 in backgound
	pspmp3.play()
	while run:
		if menu_button==(-1):menu_button = 0
		elif menu_button==(4):menu_button = 3
		screen.clear(psp2d.Color(0,0,0,255))
		screen.blit(ui_menu)
		#render_multi_line("Tailer \npidor", 50, 50, 15)
		if menu_button ==(0):
			font.drawText(screen, 3, 173, ">"+menu_text[0])
			font.drawText(screen, 3, 185, ""+menu_text[1])
			font.drawText(screen, 3, 197, ""+menu_text[2])
			font.drawText(screen, 3, 210, ""+menu_text[3])
		elif menu_button ==(1):
			font.drawText(screen, 3, 173, ""+menu_text[0])
			font.drawText(screen, 3, 185, ">"+menu_text[1])
			font.drawText(screen, 3, 197, ""+menu_text[2])
			font.drawText(screen, 3, 210, ""+menu_text[3])
		elif menu_button ==(2):
			font.drawText(screen, 3, 173, ""+menu_text[0])
			font.drawText(screen, 3, 185, ""+menu_text[1])
			font.drawText(screen, 3, 197, ">"+menu_text[2])
			font.drawText(screen, 3, 210, ""+menu_text[3])
		elif menu_button ==(3):
			font.drawText(screen, 3, 173, ""+menu_text[0])
			font.drawText(screen, 3, 185, ""+menu_text[1])
			font.drawText(screen, 3, 197, ""+menu_text[2])
			font.drawText(screen, 3, 210, ">"+menu_text[3])
		screen.swap()
		pad = psp2d.Controller()
		if pad.cross and (not lastPad or time() - lastPad >= 0.5):
			if menu_button==(0):id_current+=1;main_plot = 'game/plot/plot.py';run=False
			elif menu_button==(1):run=False;quick_load()
			elif menu_button==(2):extra_menu()
			elif menu_button==(3):run=False;Game_running = False
			lastPad = time()
		elif pad.down and (not lastPad or time() - lastPad >= 0.5):menu_button+=1;lastPad = time()
		elif pad.up and (not lastPad or time() - lastPad >= 0.5):menu_button-=1;lastPad = time()
		pass
	pspmp3.stop()
def extra_menu():
	global lastPad
	run = True
	sleep(0.3)
	while run:
		screen.clear(psp2d.Color(0,0,0,255))
		screen.blit(background[16])
		screen.swap()
		pad = psp2d.Controller()
		if pad.cross and (not lastPad or time() - lastPad >= 0.5):
			run=False