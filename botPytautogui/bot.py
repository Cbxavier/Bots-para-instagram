import time
import pyautogui
import random	
import pyperclip

def bot():
	caixatexto = pyautogui.locateOnScreen('caixadetexto.png')
	left, top = caixatexto.left, caixatexto.top
	pyautogui.click(left + 12, top +12)
	time.sleep(3)
	usuario = usuario_aleatorio()
	pyperclip.copy(usuario)
	time.sleep(3)
	pyautogui.hotkey('ctrl', 'v')
	



def usuario_aleatorio():
	users = ['joao', 'pedro', 'maria']
	user = random.choice(users)

	return user



bot()



