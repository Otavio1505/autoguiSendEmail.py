import time
import pyautogui as p

dest = str(input('Email do destinatário: ')) # <----- Email que irá receber o arquivo.

time.sleep(0.5)
p.hotkey('win','d')
time.sleep(0.5)
p.press('win')
time.sleep(0.5)
p.write('Email')  # <------- Acesso ao aplicativo
time.sleep(0.5)
p.press('enter')
time.sleep(1)

p.moveTo(x=96, y=106)   # <---- Automação do Mouse
p.click()
time.sleep(0.8)
p.moveTo(x=996, y=195)
p.click()
time.sleep(0.8)
p.write(f'{dest}')  # <---- Inserção do Destinatário
time.sleep(1)

p.hotkey('win','left')
time.sleep(0.5)
p.moveTo(x=1314, y=25)
time.sleep(0.5)
p.drag(xOffset=-770,yOffset=480,duration=1) # <------ Inserção do Arquivo
time.sleep(1)
p.mouseUp()
time.sleep(0.5)

p.moveTo(x=594, y=56) # <----- Envio do Email
time.sleep(0.1)
p.click()



