# -*- coding: utf-8 -*-
def quick_save():
	global id_current, choice_var, background_screen, character, background_id
	savefile = open('savegame/savefile.aves','w+')
	my_string = ''.join(''.join(l) for l in character)
	savefile.write("global id_current, choice_var, background_screen, character, background_id\nid_current="+str(id_current)+"\nchoice_var="+str(choice_var)+"\nbackground_id="+str(background_id)+"\ncharacter="+str(my_string)+"\nbackground_screen  = background[background_id]")
	savefile.close()
def quick_load():
	global id_current, choice_var, background_screen, character, background_id
	execfile("savegame/savefile.aves")
	pass