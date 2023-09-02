def exec_line(id, text):
	global id_current
	if id_current ==(id):
		exec(text)
		id_current+=1
