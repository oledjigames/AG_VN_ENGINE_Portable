def clear_character(id):
	global id_current, character
	if id_current ==(id):
		character= []
def set_character(id, image_id, x_pos):
	global id_current, character, Do_once, character_files
	if id_current ==(id):
		if Do_once:
			character.append((character_files[image_id], x_pos))
def set_id(id, to_id):
	global id_current
	if id_current ==(id):
		id_current = to_id
def set_background(id, image_id):
	global id_current, background_screen, background, background_id
	if id_current ==(id):
		background_screen  = background[image_id]
		background_id = image_id
def dialog(id, name, text):
	global id_current, background_screen, ui_text_bord, character, Do_once
	if id_current ==(id):
		screen.blit(background_screen)
		for a, b in character:
			screen.blit(a, dx=b, blend=True)
		screen.blit(ui_text_bord, blend=True)
		render_multi_line(name, 4, 174, 15)
		if Do_once:
			final_text = ''
			for i in range(len(text)):
				screen.blit(background_screen)
				for a, b in character:
					screen.blit(a, dx=b, blend=True)
				screen.blit(ui_text_bord, blend=True)
				render_multi_line(name, 4, 174, 15)
				final_text += text[i]
				render_multi_line(final_text, 4, 195, 15)
				psp2d.Timer(0.7)
				screen.swap()
		render_multi_line(text, 4, 195, 15)
		screen.blit(ui_cross, dx=449, dy=241, blend=True)
		Do_once = False
		debug_show()
		screen.swap()
		game_op()
def choice(id, var_index, text1, text2):
	global id_current, background_screen, ui_text_bord, character, Do_once, lastPad, choice_var
	if id_current ==(id):
		run_hueran = True
		select_choice = 0
		while run_hueran:
			if select_choice==(-1):select_choice = 0
			elif select_choice==(2):select_choice = 1
			screen.blit(background_screen)
			for a, b in character:
				screen.blit(a, dx=b, blend=True)
			screen.blit(ui_choice, blend=True)
			if select_choice==(0):
				font.drawText(screen, 110, 73, ">"+text1+"<")
				font.drawText(screen, 110, 121, text2)
			elif select_choice==(1):
				font.drawText(screen, 110, 73, text1)
				font.drawText(screen, 110, 121, ">"+text2+"<")
			pad = psp2d.Controller()
			if pad.cross and (not lastPad or time() - lastPad >= 0.5):
				run_hueran = False
				id_current+=1
				lastPad = time()
			elif pad.down and (not lastPad or time() - lastPad >= 0.35):select_choice+=1;lastPad = time()
			elif pad.up and (not lastPad or time() - lastPad >= 0.35):select_choice-=1;lastPad = time()
			Do_once = False
			debug_show()
			screen.swap()
		choice_var[var_index]  = select_choice
def choice_to_id(id, var_index, id1, id2):
	global id_current, choice_var
	if id_current ==(id):
		if choice_var[var_index]==(0):
			id_current=id1
		elif choice_var[var_index]==(1):
			id_current=id2

def back_dialog(id):
	global id_current, background_screen, character, game_op_run
	if id_current ==(id):
		screen.blit(background_screen)
		for a, b in character:
			screen.blit(a, dx=b, blend=True)
		screen.blit(ui_cross, dx=449, dy=241, blend=True)
		debug_show()
		screen.swap()
		game_op()
def go_to_plot(id, plot_name, to_id):
	global id_current, main_plot
	if id_current ==(id):
		main_plot = "game/plot/"+plot_name+".py"
		id_current=to_id